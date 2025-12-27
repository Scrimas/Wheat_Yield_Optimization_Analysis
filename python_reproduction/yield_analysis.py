"""
Wheat Yield ANOVA Pipeline
Automates a Two-Way Analysis of Variance (ANOVA) to assess the impact of genotype (Wheat) and environment (Fertilizer).
"""

from pathlib import Path
from typing import Dict
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy import stats

# --- Configuration ---
ALPHA = 0.05

def load_data(relative_path: str) -> pd.DataFrame:
    """Loads CSV data relative to the script location."""
    base_path = Path(__file__).resolve().parent
    data_path = base_path / relative_path
    
    print(f"DEBUG: Looking for data at: {data_path}")
    
    if not data_path.exists():
        raise FileNotFoundError(f"Dataset not found at: {data_path}")
    
    return pd.read_csv(data_path)

def check_assumptions(df: pd.DataFrame) -> Dict:
    """
    Verifies homogeneity of variances (Bartlett's Test).
    Required before performing standard ANOVA.
    """
    # Group data by the combination of factors
    groups = [g['yield'].values for _, g in df.groupby(['wheat_type', 'fertilizer'])]
    
    stat, p_val = stats.bartlett(*groups)
    
    return {
        "test": "Bartlett's Test",
        "statistic": stat,
        "p_value": p_val,
        "homogeneity_accepted": p_val > ALPHA
    }

def run_two_way_anova(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fits an OLS model and computes the Type II ANOVA table.
    """
    # FIX: We use Q("yield") because 'yield' is a reserved keyword in Python.
    # Q() allows us to quote the variable name safely.
    model = ols('Q("yield") ~ C(wheat_type) * C(fertilizer)', data=df).fit()
    
    # Type 2 ANOVA is standard for balanced designs
    anova_table = sm.stats.anova_lm(model, typ=2)
    return anova_table

def print_portfolio_report(assumptions: Dict, anova_results: pd.DataFrame):
    """Formats the technical results into a clear decision report."""
    print("-" * 50)
    print("WHEAT YIELD ANALYSIS REPORT (Two-Way ANOVA)")
    print("-" * 50)
    
    # 1. Assumption Check
    print(f"Assumption Check ({assumptions['test']}):")
    print(f"P-value: {assumptions['p_value']:.4f}")
    
    if assumptions['homogeneity_accepted']:
        print("Result: Variances are homogeneous. Proceeding with ANOVA.")
    else:
        print("WARNING: Variances are NOT homogeneous. ANOVA may be invalid.")
    
    print("-" * 50)
    
    # 2. ANOVA Results
    print("ANOVA Table (Significant effects):")
    print(anova_results[['F', 'PR(>F)']])
    
    print("-" * 50)
    
    # 3. Automated Conclusion
    p_inter = anova_results.loc['C(wheat_type):C(fertilizer)', 'PR(>F)']
    
    if p_inter < ALPHA:
        print(f"CONCLUSION: Significant INTERACTION detected (p={p_inter:.2e}).")
        print("Interpretation: The effect of the fertilizer DEPENDS on the wheat variety.")
    else:
        print("CONCLUSION: No interaction. Main effects can be interpreted independently.")
    print("-" * 50)

if __name__ == "__main__":
    try:
        df = load_data('../data/wheat_yield_data.csv')
        
        assumptions = check_assumptions(df)
        anova_res = run_two_way_anova(df)
        print_portfolio_report(assumptions, anova_res)
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected Analysis Error: {e}")
