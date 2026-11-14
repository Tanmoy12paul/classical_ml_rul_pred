# Team Afterburner — DS5006 Project Code

## Folder contents
- `notebooks/`: Q1 temporal-order experiments, Q2 operating-condition experiments, Ridge/Lasso comparison, and FD001/FD002 feature-budget notebooks.
- `scripts/q2_core.py`: Q2 preprocessing and feature-construction functions extracted from the team's Q2 notebook.
- `run.py`: entry point for executing the included experiment notebooks.
- `requirements.txt`: Python dependencies.
- `notebook_evidence/`: saved notebook-output panels referenced in the report appendix.

## Data requirements
The NASA C-MAPSS FD001/FD002 datasets are **not included**. Download the dataset from the NASA PCoE repository and place the files where the notebooks expect them, or update the data-path variables at the beginning of the relevant notebooks.

Do not add large raw datasets, trained model checkpoints, virtual environments, or cache folders to the submission ZIP.

## Environment
Recommended: Python 3.10 or 3.11.

Install dependencies:
```bash
python -m pip install -r requirements.txt
```

Install Jupyter if it is not already available (it is listed in requirements).

## Entry point
From this `code/` directory:
```bash
python run.py
```

The entry point executes the notebooks in this order:
1. `Q1_primary_experiments.ipynb`
2. `Q2_primary_experiments.ipynb`
3. `FD001_feature_budget.ipynb`
4. `FD002_feature_budget.ipynb`

It writes executed copies with `_executed` suffixes beside the source notebooks.

## Reproducibility note
This is a convenience entry point, not a claim that a clean machine can reproduce every report table without setup. The C-MAPSS data files must be supplied locally and notebook data paths may need adjustment. Some report tables were assembled from saved experiment outputs; full end-to-end regeneration of every reported result was not established during report preparation. The Ridge/Lasso and ordered-vs-shuffled notebooks are included for inspection and can be run separately after their data paths are configured.
