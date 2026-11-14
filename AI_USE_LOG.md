# AI-Use Log — DS5006 Machine Learning Project

**Project title:** Exploring Temporal Degradation Patterns for Turbofan Engine Remaining Useful Life (RUL) Prediction 
**Team name:** Team Afterburner

**Members**
- Anesu Kabuku — 142602026
- Rajorshi Adhikary — 142602017
- Tanmoy Paul — 142602020

---
## Summary

| Tool (name + version/model) | Members who used it | Main purposes |
| --- | --- | --- |
| ChatGPT| Tanmoy Paul| Refining project ideas, explaining concepts, refining scientific questions, code generation, explaining data representation, debugging, plotting, and discussing experimental choices.|
| Claude Tanmoy Paul
| Code generation, debugging, explaining experimental design, and plotting.|
| ChatGPT| Anesu Kabuku| Initial data analysis, report drafting, and experimental analysis and interpretation.|
| ChatGPT| Rajorshi Adhikary| Project result analysis, report review, and presentation development.|

## Entries

### Entry 001 — Project formulation and scientific questions

- **Date:** 2026-10-15 to 2026-11-04
- **Member:** Tanmoy Paul
- **Tool:** ChatGPT 
- **Purpose:** Refining a project idea; explaining concepts; refining scientific questions
- **Prompt:**
  - “can we find RUL of a jet engine using classical ML”
  - “can u find some of the sota preprocessing paper for rul”
  - “why are we calculating the temporal data and how does it ansring our Q of Does removing the effect of operating conditions help, and does it matter when we do it?”
  - "Find the rul preprocessing SOTA papers"
- **Chat link / transcript file:** 
  - https://chatgpt.com/share/6af201af-c8d8-83ee-8119-b7d9b9cea122, 
  - https://chatgpt.com/share/6af201ed-ac94-83e8-bb3a-075895ec411d, 
  - https://chatgpt.com/share/6af202b4-74dc-83ee-ba53-995176784ce0
- **What we used:** Discussion used to shape the project around classical-ML-based RUL prediction using NASA C-MAPSS, temporal-window features, and the two project questions: (Q1) whether the order of readings within a window matters, and (Q2) whether operating-condition adjustment helps and whether its order relative to differencing matters.
- **What we changed:** The team retained its approved questions, datasets and experimental design in the project proposal. AI suggestions were treated as discussion material, not as experimental findings.
- **How we verified it:** Compare the final questions and hypotheses with the approved project proposal and implemented experimental protocol. Add the proposal/notebook references and record the team's actual review.
### Entry 002 — Initial data analysis, report drafting, and experimental analysis and interpretation.

- **Member:** Anesu Kabuku — 142602026
- **Tool:** ChatGPT
- **Purpose:** Initial data analysis, report drafting, and experimental analysis and interpretation.
- **Work performed:**
  - Performed the initial exploratory data analysis on the FD001 and    FD002 datasets (shape, null/duplicate checks, constant and near-constant columns, per-unit cycle summaries, RUL alignment, sensor–RUL correlations).
  - Drafted the report structure and body text following the project template, including the introduction, scientific questions, data description, methodology, experimental design, results, failure analysis, discussion, and conclusion sections.
  - Analysed and interpreted the Q1 and Q2 experimental results, including the C-minus-B trend-feature comparison, the AF/DF/N operating-condition comparison, hypothesis tests, and engine-life-stage breakdowns.
  - Wrote the LaTeX code for the report, including the tables and TikZ/pgfplots figures regenerated from the reported numerical results.
  - Prepared the reproducibility statement, AI-use summary, and appendix configuration tables.
- **Verification:** Cross-checked every numerical value in the report against the executed notebooks, the Q1 and Q2 source PDFs, and the saved fold results; confirmed that all tables and figures are consistent with the reported cross-validation and test metrics before final submission.

### Entry 003 — C-MAPSS data handling, RUL construction and visualisation

- **Date:** 2026-10-15 to 2026-11-01 
- **Member:** Tanmoy Paul
- **Tool:** ChatGPT 
- **Purpose:** Code generation; explaining data representation; debugging and plotting
- **Prompt:**
  - “can u give me a script where i can make zip file out of the models”
  - Other project prompts requested conversion of NASA C-MAPSS TXT files to CSV, sensor-versus-cycle visualisations, and preprocessing/feature visualisation.
- **Chat link / transcript file:** 
  - https://chatgpt.com/share/6af202b4-74dc-83ee-ba53-995176784ce0
- **What we used:** Assistance with code and explanations for working with C-MAPSS files, handling RUL targets, inspecting sensor trajectories, and saving project outputs. Specify the exact scripts, functions and notebook cells retained before submission.
- **What we changed:** Adapted paths, column names, dataset subsets and output locations to the team's FD001/FD002 files and notebook environment. Record the exact changes to retained code.
- **How we verified it:** Check row counts, engine counts, cycle ordering, sensor columns and RUL values against the source data and project specification. Run the scripts and inspect generated CSV files and plots. Enter only checks actually completed.

### Entry 004 — Q1 temporal-feature experiments and notebook updates

- **Date:** 2026-11-04 to 2026-11-08 (confirm exact dates)
- **Member:** Tanmoy Paul
- **Tool:** Claude 
- **Purpose:** Code generation; debugging; explaining experimental design; plotting
- **Prompt:**
  - “so what are we trying ans form the Q” (about the Q2 hypothesis text)
  - “So what kind of experiment we do need to perform for Q1 we do some exps have a look” (with the Q1 notebook)
  - “lets design a experiment where a 5 fold experiment, window will be fixed as 50, set all conditions as C, use Random forest, Adaboost and XGBoost, test on the test dataset, experiment in different call for all 3 conditions, do the hypoothesis tetsing, and save the .pth model and make a zip file out of that”
  - “can u compare all results like which conditions gives better performance including conditions in Q1 and Q2”
- **Chat link / transcript file:** 
  - https://claude.ai/share/9a5fca0c-3be8-4dd3-8548-144b0408a178
- **What we used:** Feedback on the Q2 design (condition adjustment, order of steps, leakage, the extra “R” strategy) and plain-language explanations of the formulas. A review of the Q1 results with suggestions for further experiments (longer windows, which trend feature does the work, early-life behaviour). Claude did not change the Q1 code. Q2 notebooks: a first draft and the final nine-cell notebook (N, AF and DF, each with RF, XGBoost and AdaBoost), which we ran on Kaggle. An implementation plan document and the Q2 experiment report, including interpretation of our results and a comparison of the Q1 and Q2 conditions.
Later notebooks: a feature-analysis (EDA) notebook and a simplified feature-selection notebook. Planning only (no code): tuning the AF + C model, and predicting RUL when fewer than 50 cycles are available.
- **What we changed:** Adapted generated code to the team's notebook, variable names, dataset paths and result-file structure. List the exact cells/functions retained and any further local modifications.
- **How we verified it:** Claude tested its notebooks on made-up data in its own environment, not on C-MAPSS. This only shows that the code runs. We ran the final Q2 notebook on Kaggle (CPU). Its checks passed: FD001 features identical across N, AF and DF; FD002 strategies differ; no future leakage; DF path check; test-time and training-time features match; short test engines padded; folds cover every engine once; slope matches a straight-line fit.
We compared the notebook with Q1 using the same seed and folds. Random Forest and AdaBoost matched Q1’s condition C results exactly on FD001 and FD002. XGBoost differed by at most 0.11 cycles (cause not confirmed, possibly a different XGBoost device or version). Three saved models were reloaded and reproduced their stored test predictions; 18 model files were saved. Every number in the written report was checked against the notebook outputs. They matched. One item is not an actual separate check in the notebook: “engine-boundary differences handled”. Known limits of the AI output: the explanation of why DF is worse than AF was not measured in the final notebook, and the later notebooks and the tuning and short-history plans have not been run or tested on the real data. 

### Entry 005 — Feature reduction and classical regression models

- **Date:** 2026-11-07 to 2026-11-09 (confirm exact dates)
- **Member:** Tanmoy Paul
- **Tool:** ChatGPT 
- **Purpose:** Explaining concepts; discussing experimental choices; code generation
- **Prompt :**
  - “Btw there are lots of features should we have to deal with that like PCA or feature reduction”
  - “what should we done for feature reduction. can we use corr”
- **Chat link / transcript file:** 
  - https://chatgpt.com/share/6af20b79-0398-83ee-98af-1d1adfc6348e
  - https://chatgpt.com/share/6af20b79-0398-83ee-98af-1d1adfc6348e
- **What we used:** Discussion of feature dimensionality and feature-reduction options, and assistance creating a separate Ridge/Lasso experiment notebook for FD001 and FD002 with a fixed global seed, engine-wise five-fold validation and official test-set evaluation.
- **What we changed:** The notebook was revised after review to include Condition D in official test evaluation and plots. Record which final cells were retained and any local changes. State alpha values as fixed settings unless a tuning experiment was actually performed.
- **How we verified it:** Run the notebook from a clean kernel. Check that only Ridge and Lasso are fitted; confirm engine-wise folds are disjoint; confirm the same fold-generation rule and seed are used for both datasets; verify window selection uses CV only and the official test set is reserved for final evaluation. Confirm A/B/C/D appear in test results and plots. Record actual results and any unresolved issues.



### Entry 006 — Project result analysis, report review and presentation development

- **Member:** Rajorshi Adhikary — 142602017
- **Tool:** ChatGPT
- **Purpose:** Project result analysis, report review and presentation development.
- **Work performed:**
  - Reviewed Q1 and Q2 experimental results and their interpretation.
  - Integrated Ridge and Lasso results into the Q1 comparison.
  - Prepared and refined the final project presentation.
  - Checked result consistency and corrected presentation errors.
  - Improved slide design, visualisation and readability.
- **Verification:** Cross-checked reported values with the project results and reviewed the final presentation for accuracy and clarity.




---

## Declaration

We confirm that this log records the AI use declared by the members listed below, that every member has reviewed the entries relevant to them, and that each of us can explain any work listed here. We will add any missing AI interactions before submission.

| Member | Roll No. | Initials |
|---|---:|---|
| Anesu Kabuku | 142602026 | |
| Rajorshi Adhikary | 142602017 | |
| Tanmoy Paul | 142602020 | |

---

