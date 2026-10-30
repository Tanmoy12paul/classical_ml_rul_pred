# Classical Machine Learning for Remaining Useful Life (RUL) Prediction

A research-oriented study of classical Machine Learning approaches for Remaining Useful Life (RUL) estimation of turbofan engines using the NASA C-MAPSS dataset.

## Overview

Remaining Useful Life (RUL) prediction is an important component of predictive maintenance. It aims to estimate the number of operational cycles remaining before a machine or component reaches the end of its useful life.

This project investigates classical Machine Learning techniques for RUL prediction using multivariate sensor data from the NASA Commercial Modular Aero-Propulsion System Simulation (C-MAPSS) dataset.

The primary objective is to investigate the effectiveness of classical regression and ensemble learning algorithms in estimating engine degradation and predicting remaining useful life.

## Dataset

**NASA C-MAPSS Turbofan Engine Degradation Simulation Dataset**

This study focuses on two subsets:

| Dataset | Operating Conditions | Fault Modes |
|---|---|---|
| FD001 | 1 | HPC degradation |
| FD002 | 6 | HPC degradation |

The selection allows an investigation of model performance under single and multiple operating conditions while keeping the fault mode consistent.

### Dataset Characteristics

- Multivariate time-series sensor measurements.
- Multiple engine operating trajectories.
- Operational settings and sensor readings.
- RUL estimation based on engine operating cycles.

## Research Objectives

1. Investigate classical Machine Learning approaches for RUL estimation.
2. Analyze the effects of operating conditions on predictive performance.
3. Study time-series preprocessing and sensor feature engineering.
4. Evaluate the effectiveness of different regression and ensemble learning algorithms.
5. Compare model generalization across FD001 and FD002.

## Methodology

The experimental workflow consists of the following stages:

1. **Exploratory Data Analysis:** Analyze sensor distributions, operating conditions, and degradation patterns.
2. **Preprocessing:** Perform sensor analysis, normalization, and appropriate time-series preprocessing.
3. **Feature Engineering:** Construct temporal features and statistical representations from sensor measurements.
4. **Model Development:** Implement and evaluate classical Machine Learning regression algorithms.
5. **Evaluation:** Compare predictive performance using appropriate RUL evaluation metrics.

## Machine Learning Approaches

The study focuses on classical Machine Learning methods, including regression and ensemble-based approaches.

Candidate models include:

- Linear Regression
- Ridge and Lasso Regression
- Support Vector Regression (SVR)
- Random Forest Regression
- Gradient Boosting Regression
- XGBoost
- LightGBM

## Experimental Design

The primary experimental comparison involves:

- **FD001:** Model evaluation under a single operating condition.
- **FD002:** Model evaluation under multiple operating conditions.

Both subsets share the HPC degradation fault mode, allowing the influence of operating-condition variability to be investigated.

## Evaluation Metrics

Model performance will be evaluated using:

- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- RUL-specific NASA Scoring Function

## Repository Structure

```text
├── data/
├── notebooks/
├── src/
├── experiments/
├── results/
├── models/
├── requirements.txt
└── README.md
```

## Technologies

- Python
- NumPy
- Pandas
- SciPy
- Scikit-learn
- Matplotlib
- Seaborn
- XGBoost
- LightGBM

## Dataset Reference

NASA Prognostics Center of Excellence (PCoE).

**Dataset:** Commercial Modular Aero-Propulsion System Simulation (C-MAPSS).

## Research Scope

This repository focuses exclusively on classical Machine Learning approaches. Deep Learning architectures are outside the scope of the primary experimental comparison.

---

**Author:** Tanmoy Paul  
**M.Tech Data Science, IIT Palakkad**

[GitHub](https://github.com/Tanmoy12paul) | [LinkedIn](https://www.linkedin.com/in/tanmoypaul2002/) | [ORCID](https://orcid.org/0009-0005-9843-2091)
