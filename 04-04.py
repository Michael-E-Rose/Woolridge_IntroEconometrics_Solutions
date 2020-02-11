"""Python script for C4, Chapter 4 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/bwght.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
formula_r = 'bwght ~ cigs + parity + faminc + motheduc + fatheduc'
lm_r = smf.ols(formula_r, data=df).fit()
formula_u = 'bwght ~ cigs + parity + faminc'
lm_u = smf.ols(formula_u, data=df).fit()
print("R-squared of restricted and unrestricted model:")
print("restricted:", lm_r.rsquared)
print("unrestricted:", lm_u.rsquared)
print(">>>>")
