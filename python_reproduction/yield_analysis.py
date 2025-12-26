import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy import stats
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', 'data', 'wheat_yield_data.csv')

df = pd.read_csv(file_path)

print("--- DATA PREVIEW ---")
print(df.head())
print("-" * 30)

print("\n--- BARTLETT TEST (HOMOGENEITY OF VARIANCES) ---")
groups = [group['yield'].values for name, group in df.groupby(['wheat_type', 'fertilizer'])]
bartlett_stat, bartlett_p = stats.bartlett(*groups)

print(f"Statistic: {bartlett_stat:.4f}")
print(f"P-value:   {bartlett_p:.4f}")

if bartlett_p > 0.05:
    print("Result: Variances are homogeneous.")
else:
    print("Result: Variances are NOT homogeneous.")

print("\n--- TWO-WAY ANOVA WITH INTERACTION ---")
model = ols('yield ~ C(wheat_type) * C(fertilizer)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)

p_interaction = anova_table.loc['C(wheat_type):C(fertilizer)', 'PR(>F)']

if p_interaction < 0.05:
    print("\nCONCLUSION: Significant interaction detected between Wheat Type and Fertilizer.")
    print("The effect of the fertilizer depends on the wheat variety.")
else:
    print("\nCONCLUSION: No significant interaction.")
