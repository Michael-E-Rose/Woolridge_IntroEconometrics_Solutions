"""Python script for C5, Chapter 2 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/rdchem.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# ii)
formula = 'lrd ~ lsales'
lm = smf.ols(formula, data=df).fit()
print(lm.summary())
print(">>>>")
