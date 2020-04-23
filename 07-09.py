"""Python script for C9, Chapter 7 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf
import numpy as np


# Read in df
file = "./data/401ksubs.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
print("Fraction of families eligible for 401k:")
print(len(df[df['e401k'] == 1]) / len(df['e401k']))
print(">>>>")

# ii)
lm1 = smf.ols('e401k ~ inc + incsq + age + agesq + male', data=df).fit()
print(lm1.summary())
print(">>>>")

# iv)
print("Smallest and largest fitted values")
print(lm1.fittedvalues.min())
print(lm1.fittedvalues.max())

# v)
print("Number of families eligible for 401k:")
df['fittedvalues'] = lm1.fittedvalues
def func(x):
    if x >= 0.5:
        return 1
    else:
        return 0
df['e401k_i'] = df['fittedvalues'].apply(func)
print(len(df[df['e401k_i'] == 1]))
print(">>>>") 

# vi)
# CHECK AGAIN

# vii)
lm2 = smf.ols('e401k ~ inc + incsq + age + agesq + male + pira', data=df).fit()
print(lm2.summary())
print(">>>>")