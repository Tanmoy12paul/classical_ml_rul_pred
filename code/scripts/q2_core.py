import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from sklearn.cluster import KMeans

class Normalizer:
    """Per-condition scaling. k = 1 gives one overall mean/spread (condition ignored)."""
    def __init__(self, k): self.k = k
    def _regime(self, df):
        if self.k == 1: return np.zeros(len(df), int)
        S = (df[self.settings].values - self.s_mu) / self.s_sd
        return ((S[:, None, :] - self.centers[None]) ** 2).sum(2).argmin(1)
    def fit(self, df, sensors, settings, seed=42):
        self.sensors, self.settings = list(sensors), list(settings)
        if self.k > 1:
            S = df[self.settings].values; self.s_mu, self.s_sd = S.mean(0), S.std(0) + 1e-9
            self.centers = KMeans(self.k, n_init=10, random_state=seed).fit((S - self.s_mu) / self.s_sd).cluster_centers_
        reg, X = self._regime(df), df[self.sensors].values
        gm, gs = X.mean(0), X.std(0) + 1e-9
        self.mu, self.sd = np.zeros((self.k, len(sensors))), np.ones((self.k, len(sensors)))
        for r in range(self.k):
            m = reg == r
            if m.sum() > 10:
                self.mu[r] = X[m].mean(0); s = X[m].std(0); self.sd[r] = np.where(s < 1e-9, 1.0, s)
            else:
                self.mu[r], self.sd[r] = gm, gs
        return self
    def transform(self, df):
        reg = self._regime(df)
        return (df[self.sensors].values - self.mu[reg]) / self.sd[reg]
    def state(self):
        return dict(k=self.k, mu=self.mu, sd=self.sd, sensors=self.sensors, settings=self.settings,
                    s_mu=getattr(self, "s_mu", None), s_sd=getattr(self, "s_sd", None), centers=getattr(self, "centers", None))
    @classmethod
    def from_state(cls, st):
        n = cls(st["k"]); n.__dict__.update({k: v for k, v in st.items() if k != "k"}); return n

def rebuild_path(Wd):
    # Wd: scaled one-step changes inside a window, shape (m, S, L-1). Returns a path of length L that starts at 0.
    return np.concatenate([np.zeros_like(Wd[:, :, :1]), np.cumsum(Wd, axis=2)], axis=2)

def feats_C(Wl, Wt):
    # Wl: window levels -> mean/std/min/max/median.  Wt: window used for slope and change features.  Both (m, S, L).
    L = Wl.shape[2]; t = np.arange(L) - (L - 1) / 2
    dW = np.diff(Wt, axis=2)
    return np.concatenate([Wl.mean(2), Wl.std(2), Wl.min(2), Wl.max(2), np.median(Wl, 2),
                           (Wt * t).sum(2) / (t ** 2).sum(), Wt[:, :, -1] - Wt[:, :, 0], dW.std(2), np.abs(dW).mean(2)], axis=1)

def raw_diffs(df, sensors):
    X = df[list(sensors)].values; dX = np.zeros_like(X); dX[1:] = X[1:] - X[:-1]
    first = np.r_[True, df["unit_id"].values[1:] != df["unit_id"].values[:-1]]; dX[first] = 0      # no change across engines
    return dX

def arm_inputs(arm, df, sensors, norm1, normk):
    """returns (levels, scaled raw changes or None, extra columns or None)"""
    if arm == "N":  return norm1.transform(df), None, None
    if arm == "R":  return norm1.transform(df), None, np.eye(normk.k)[normk._regime(df)]
    if arm == "AF": return normk.transform(df), None, None
    if arm == "DF": return normk.transform(df), raw_diffs(df, sensors) / normk.sd[normk._regime(df)], None
    raise ValueError(arm)

def build(Xlev, Xdiff, extra, groups, units, L, start, stride):
    """one feature row per window ending at cycle t (t >= max(L, start)); only cycles up to t are used."""
    feats, rows = [], []
    for u in units:
        idx = groups[u]; n = len(idx)
        ends = np.arange(max(L, start) - 1, n, stride)
        if len(ends) == 0: continue
        sel = ends - (L - 1)
        Wl = sliding_window_view(Xlev[idx], L, axis=0)[sel]
        Wt = Wl if Xdiff is None else rebuild_path(sliding_window_view(Xdiff[idx], L, axis=0)[sel][:, :, 1:])
        f = feats_C(Wl, Wt)
        if extra is not None: f = np.hstack([f, extra[idx[ends]]])
        feats.append(f); rows.append(idx[ends])
    return np.vstack(feats), np.concatenate(rows)

def last_window_features(Xlev, Xdiff, extra, groups, units, L):
    """one row per engine: the last L cycles. Short engines are padded by repeating the first reading (changes padded with 0)."""
    out = []
    for u in units:
        idx = groups[u]; a = Xlev[idx]
        if len(a) < L: a = np.vstack([np.repeat(a[:1], L - len(a), 0), a])
        Wl = a[-L:].T[None]
        if Xdiff is None: Wt = Wl
        else:
            d = Xdiff[idx]
            if len(d) < L: d = np.vstack([np.zeros((L - len(d), d.shape[1])), d])
            Wt = rebuild_path(d[-L:].T[None][:, :, 1:])
        f = feats_C(Wl, Wt)
        if extra is not None: f = np.hstack([f, extra[idx[-1]][None]])
        out.append(f[0])
    return np.array(out)

def nasa_terms(y, p):
    d = p - y
    return np.where(d < 0, np.exp(-d / 13) - 1, np.exp(d / 10) - 1)

def predict_from_bundle(bundle, df, rul_cap=125):
    """df: raw readings (unit_id, cycle, settings, sensors) of one or more engines. Returns {unit_id: predicted RUL}."""
    df = df.sort_values(["unit_id", "cycle"]).reset_index(drop=True)
    n1, nk = Normalizer.from_state(bundle["norm1"]), Normalizer.from_state(bundle["normk"])
    lev, dif, ex = arm_inputs(bundle["arm"], df, bundle["sensors"], n1, nk)
    groups = df.groupby("unit_id").indices; units = sorted(groups)
    p = np.clip(bundle["model"].predict(last_window_features(lev, dif, ex, groups, units, bundle["L"])), 0, rul_cap)
    return dict(zip(units, p))