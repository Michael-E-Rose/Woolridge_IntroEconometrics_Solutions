"""Python script for C7, Chapter 3 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf


# Read in df
file = "./data/meap93.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
lm = smf.ols('math10 ~ np.log(expend) + lnchprg', data=df).fit()
print(lm.summary())
print(">>>>")

# iii)
lm = smf.ols('math10 ~ np.log(expend)', data=df).fit()
print(lm.summary())
print(">>>>")

# iv)
print("The sample correlation between lexpend and lnchprg is:")
print(df['lnchprg'].corr(np.log(df['expend']))) 
print(">>>>")
