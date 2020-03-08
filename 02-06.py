"""Python script for C6, Chapter 2 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf


# Read in df
file = "./data/meap93.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# iii) - iv)
lm = smf.ols('math10 ~ np.log(expend)', data=df).fit()
print(lm.summary())
print(">>>>")

# v)
print("# of values in math10 that are bigger than 100")
print(len(df.loc[df['math10'] > 100]))
print(">>>>")