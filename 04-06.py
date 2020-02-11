"""Python script for C6, Chapter 4 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/wage2.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# ii)
df['test'] = df['exper'] + df['tenure']
formula3 = 'lwage ~ educ + exper + test'
lm = smf.ols(formula, data=df).fit()
print(lm.summary())
print(">>>>")

