# Wheat_Yield_Optimization_Analysis

# Wheat Yield Optimization Analysis

This repository contains a biostatistical analysis aimed at optimizing wheat production by evaluating the impact of two factors: **Genotype** (Wheat Variety) and **Fertilizer Type**.

Originally conducted using R during my **L3 Biology degree (Université Grenoble Alpes)**, this project has been reproduced in Python to demonstrate workflow automation and statistical modeling skills.

## Project Structure

* `data/` : Cleaned dataset in CSV format (long format).
* `r_analysis/` : Original Academic script (ANOVA methodology).
* `python_reproduction/` : Implementation using `statsmodels` and `pandas`.

## Statistical Methodology

We investigate three biological questions:
1. Does the wheat variety influence yield?
2. Does the fertilizer type influence yield?
3. **Is there an interaction between the variety and the fertilizer?**

**Method:** Two-Way ANOVA (Analysis of Variance) with interaction term.
**Prerequisites:** Normality (Shapiro-Wilk) and Homoscedasticity (Bartlett test) were validated ($p > 0.05$).

## Key Results

* **Bartlett Test:** Variances are homogeneous ($p = 0.103$).
* **ANOVA Results:**
    * Effect of Wheat Type: **Highly Significant** ($p < 0.001$).
    * Effect of Fertilizer: **Highly Significant** ($p < 0.001$).
    * **Interaction Effect:** **Significant** ($p < 0.001$).

**Biological Conclusion:**
The analysis reveals a strong interaction. The efficiency of a specific fertilizer depends heavily on the wheat variety used. A generalized recommendation cannot be made; the fertilizer must be adapted to the specific wheat strain.

## Tech Stack

* **R** : `aov`, `bartlett.test`
* **Python** : `pandas`, `statsmodels` (OLS Regression & ANOVA table), `scipy`

---
*Author: Ismaël PHILIPPE - Biology Student*
