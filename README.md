# Remaining Useful Life (RUL) Prediction Using Classical Machine Learning

**Team Afterburner | DS5006 – Machine Learning Project**

## 1. Overview

Remaining Useful Life (RUL) prediction is an important task in predictive maintenance. It aims to estimate the number of operational cycles remaining before a machine or component reaches failure.

Accurate RUL estimation allows maintenance teams to schedule repairs proactively, reduce unexpected equipment failures, and improve operational efficiency.

In this project, we investigate the effectiveness of **classical machine learning algorithms** for predicting the Remaining Useful Life of aircraft turbofan engines using NASA's C-MAPSS dataset.

Rather than relying on deep learning architectures, we explore how temporal feature engineering, operating-condition adjustment, and feature selection influence the predictive performance of traditional machine learning models.

## 2. Objectives

The primary objectives of this project are:

- Investigate the effectiveness of classical ML algorithms for RUL prediction.
- Understand the importance of temporal information in sensor measurements.
- Examine whether preserving the order of sensor observations improves prediction.
- Investigate the impact of operating-condition adjustment on predictive performance.
- Compare different feature engineering and normalization strategies.
- Evaluate the effect of feature selection and dimensionality reduction.

## 3. Dataset

We use the **NASA C-MAPSS (Commercial Modular Aero-Propulsion System Simulation)** dataset.

The dataset contains simulated run-to-failure trajectories of turbofan engines. Each engine is monitored over multiple operational cycles, with sensor measurements recording its changing condition.

### Dataset subsets

We focus on FD001 and FD002.

| Property | FD001 | FD002 |
|---|---|---|
| Training engines | 100 | 260 |
| Test engines | 100 | 259 |
| Operating conditions | 1 | 6 |
| Fault modes | 1 | 1 |
| Degradation mode | HPC degradation | HPC degradation |

**Why FD001 and FD002?**

Both datasets contain the same primary fault mode (High-Pressure Compressor degradation), but differ in their operating conditions.

- **FD001:** Single operating condition.
- **FD002:** Six different operating conditions.

This allows us to investigate how operating-condition variability affects RUL prediction while keeping the degradation mode fixed.

### Dataset features

Each observation contains:

- Engine ID
- Operational cycle
- 3 operational setting variables
- 21 sensor measurements

The target variable is Remaining Useful Life (RUL), measured in the number of operational cycles remaining before engine failure.

## 4. Methodology

Our approach converts sequential sensor measurements into a supervised tabular learning problem.

For each engine and operational cycle, we construct a temporal window containing the current observation and its preceding observations.

Let the temporal window length be \(L\).

\[
X_t = [x_{t-L+1},\ldots,x_{t-1},x_t]
\]

We then extract different types of features from this window and use them to train classical machine learning models.

### 4.1 Temporal Feature Engineering

We investigate four experimental conditions.

**Condition A: Current-cycle features**

Uses only the sensor measurements from the current operational cycle.

**Condition B: Statistical features**

Extracts statistical information from the temporal window:

- Mean
- Standard deviation
- Minimum
- Maximum
- Median

**Condition C: Statistical + Temporal features**

Extends Condition B by incorporating temporal trend information:

- Slope
- Last-minus-first difference
- Standard deviation of first differences
- Mean absolute first difference

**Condition D: Shuffled temporal features**

Randomly shuffles observations within each temporal window before computing the features in Condition C.

This experiment helps determine whether the improvement comes from temporal ordering or simply from the distribution of sensor observations.

### 4.2 Window Lengths

We experiment with different temporal window lengths:

\[
L \in \{5,10,20,30,50\}
\]

This helps us understand how much historical information is useful for RUL estimation.

### 4.3 Operating-Condition Adjustment

FD002 contains six operating conditions, which introduce variations in sensor measurements.

These variations can make it difficult to distinguish changes caused by operating conditions from changes caused by engine degradation.

We investigate three approaches:

- **N – No adjustment:** Uses the original sensor measurements.
- **AF – Adjustment First:** Adjusts sensor measurements for operating conditions before computing temporal features.
- **DF – Difference First:** Computes temporal differences first and subsequently applies operating-condition adjustment.

The objective is to understand whether operating-condition adjustment improves prediction and whether the order of adjustment and temporal feature extraction matters.

## 5. Machine Learning Models

We investigate the performance of the following classical machine learning algorithms:

| Algorithm | Description |
|---|---|
| Ridge Regression | Linear regression with L2 regularization |
| Lasso Regression | Linear regression with L1 regularization |
| Random Forest | Ensemble of decision trees using bagging |
| AdaBoost | Adaptive boosting ensemble |
| XGBoost | Gradient boosting framework |

The models are evaluated using engineered sensor features to identify which algorithms perform best for RUL estimation.

## 6. Feature Selection and Dimensionality Reduction

We further investigate the impact of feature dimensionality on prediction performance.

Our experiments include:

- Feature selection using different numbers of features.
- Variance-based removal of zero-variance features.
- Principal Component Analysis (PCA).
- Comparison of predictive performance across different feature dimensions.

The objective is to understand whether reducing the feature space can retain predictive information while improving computational efficiency.

## 7. Evaluation Metrics

We use two evaluation metrics.

### 7.1 Root Mean Squared Error (RMSE)

RMSE measures the average magnitude of prediction errors, with higher penalties for larger errors.

\[
RMSE = \sqrt{\frac{1}{N}\sum_{i=1}^{N}(y_i-\hat{y}_i)^2}
\]

Lower RMSE indicates better predictive accuracy.

### 7.2 NASA Prognostics Score

The NASA scoring function evaluates the cost of prediction errors, assigning a higher penalty to late predictions than early predictions.

\[
s_i =
\begin{cases}
e^{-\frac{d_i}{13}}-1, & d_i < 0\\
e^{\frac{d_i}{10}}-1, & d_i \geq 0
\end{cases}
\]

where:

\[
d_i = \hat{y}_i-y_i
\]

The total score is:

\[
Score = \sum_{i=1}^{N}s_i
\]

A lower NASA score indicates better prognostic performance.

## 8. Key Experimental Findings

Our experiments investigate the following research questions:

### Q1: Does the order of sensor observations matter?

We compare statistical features, temporal features, and shuffled temporal features.

Key observations:

- Incorporating temporal trend information improves prediction, particularly for longer windows.
- Condition C generally outperforms Condition B when the window length is sufficiently large.
- Shuffling temporal observations removes much of the improvement obtained from temporal features.
- Longer temporal windows generally improve performance, although the improvement varies between datasets.

### Q2: Does operating-condition adjustment improve RUL prediction?

We compare N, AF, and DF approaches.

Key observations:

- For FD001, operating-condition adjustment provides little improvement because the dataset contains only one operating condition.
- For FD002, AF provides a substantial improvement over the unadjusted and difference-first approaches.
- The results highlight the importance of accounting for operating-condition variability in multi-condition environments.

*Note: Numerical results and additional experiment-specific findings should be added here as the final experiments are consolidated.*

## 9. Repository Structure

TeamAfterburner_DS5006_project/
│
├── .git/
├── .gitignore
│
├── code/
│   ├── notebooks/
│   │   ├── FD001_feature_budget.ipynb
│   │   ├── FD002_feature_budget.ipynb
│   │   ├── Q1_primary_experiments.ipynb
│   │   ├── Q2_primary_experiments.ipynb
│   │   ├── ridge-lasso-rul.ipynb
│   │   └── Ordered_vs_Shuffled_Window_Experiment.ipynb
│   │
│   ├── scripts/
│   │   ├── q2_core.py
│   │   └── run_notebooks.sh
│   │
│   ├── notebook_evidence/
│   │   ├── notebook_evidence_1.png
│   │   ├── notebook_evidence_2.png
│   │   ├── notebook_evidence_3.png
│   │   └── notebook_evidence_4.png
│   │
│   ├── run.py
│   ├── requirements.txt
│   └── README.md
│
├── presentation/
│   └── team_afterburner_ml_project.pdf
│
├── report_src/
│   ├── figures/
│   │   ├── methodology_workflows.png
│   │   ├── q1_trend_gain.png
│   │   ├── q2_fd002_cv.png
│   │   └── notebook_evidence_*.png
│   │
│   ├── main.tex
│   └── README.md
│
├── AI_USE_LOG.md
├── README.md
└── report.pdf

*The structure above represents the intended organization; adjust it to match the actual repository.*

## 10. Installation and Setup

### Prerequisites

- Python 3.9+
- Jupyter Notebook / JupyterLab
- Git

### Clone the repository

```bash
git clone https://github.com/Tanmoy12paul/classical_ml_rul_pred.git

cd classical_ml_rul_pred
```

### Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the notebooks

```bash
jupyter notebook
```

Open the relevant notebooks to reproduce the experiments.

## 11. Technologies and Libraries

- **Programming Language:** Python
- **Data Processing:** NumPy, Pandas
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn, XGBoost
- **Dimensionality Reduction:** PCA
- **Development Environment:** Jupyter Notebook
- **Version Control:** Git and GitHub

## 12. References

1. Saxena, A., Goebel, K., Simon, D., & Eklund, N. (2008). *Damage Propagation Modeling for Aircraft Engine Run-to-Failure Simulation*. International Conference on Prognostics and Health Management.

2. NASA Prognostics Data Repository – C-MAPSS Turbofan Engine Degradation Simulation Dataset.

   https://www.nasa.gov/intelligent-systems-division/

3. NASA Prognostics Center of Excellence Data Repository.

   https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/

## 13. Contributors

**Team Afterburner**

DS5006 – Machine Learning

IIT Palakkad

---

*This project explores the potential of classical machine learning methods for predictive maintenance through temporal feature engineering and operating-condition-aware RUL estimation.*