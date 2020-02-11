"""Python script for C1, Chapter 4 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/vote1.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# iii)
formula1 = 'voteA ~ lexpendA + lexpendB + prtystrA'
lm1 = smf.ols(formula1, data=df).fit()
print(lm1.summary())
print(">>>>")

# iv)
df['test'] = df['lexpendB'] - df['lexpendA']
formula2 = 'voteA ~ lexpendA + test + prtystrA'
lm2 = smf.ols(formula2, data=df).fit()
print(lm2.summary())
print(">>>>")
