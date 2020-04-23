"""Python script for C14, Chapter 7 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf

# Read in df
file = "./data/charity.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
lm1 = smf.ols('respond ~ resplast + avggift', data=df).fit()
print(lm1.summary())
print(">>>>")

# iii)
lm2 = smf.ols('respond ~ resplast + avggift + propresp', data=df).fit()
print(lm2.summary())
print(">>>>")

# v)
lm3 = smf.ols('respond ~ resplast + avggift + propresp + mailsyear', data=df).fit()
print(lm3.summary())
print(">>>>")