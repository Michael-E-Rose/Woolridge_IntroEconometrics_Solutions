"""Python script for C4, Chapter 2 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/wage2.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
print(df[['wage', 'IQ']].describe())
print(">>>>")

# ii)
lm = smf.ols('wage ~ IQ', data=df).fit()
print(lm.summary())
print(">>>>")

# iii)
lm = smf.ols('lwage ~ IQ', data=df).fit()
print(lm.summary())
print(">>>>")
