# Wheat Yield Optimization Analysis

This repository contains a biostatistical analysis aimed at optimizing wheat production by evaluating the combined effects of **Genotype** (Wheat Variety) and **Fertilizer Type** on yield.

This project was initially carried out as part of my **Bachelor's degree in Biology (Grenoble Alpes University)** using R, then reproduced in Python to develop my data science skills.

## Project structure

* `data/`: Contains the cleaned dataset (`.csv`).
* `r_analysis/`: Original analysis script (academic methodology).
* `python_reproduction/`: Counter-expertise and automation performed in Python (Pandas/Statsmodels).

## Statistical Methodology

The study utilizes a **Two-Way ANOVA** (Analysis of Variance) to investigate interaction effects.

1.  **Assumption Checking**: Verification of homoscedasticity ($H_0$: Equal variances) using **Bartlett's test**.
2.  **Modeling**: Assessment of main effects and interaction term ($Yield \sim Wheat \times Fertilizer$).
3.  **Validation**: Analysis of the interaction significance to determine the biological conclusion.

## Main Results

| Test | P-value | Interpretation |
| :--- | :--- | :--- |
| **Bartlett Test** | $0.103$ | **Homogeneity Accepted** (ANOVA is valid) |
| **ANOVA (Interaction)** | $< 0.001$ | **Significant Interaction** |

**Biological conclusion:**
The analysis reveals a highly significant interaction between the factors. The efficiency of a specific fertilizer depends heavily on the wheat variety used. Therefore, no generalized recommendation can be made; the fertilizer strategy must be adapted to the specific wheat strain.

## Tools Used

* **R**: `aov`, `bartlett.test` (Academic standard)
* **Python**: `pandas`, `statsmodels`, `scipy` (Automation & Engineering)

---

*Author: Ismaël PHILIPPE - Biology Student*
