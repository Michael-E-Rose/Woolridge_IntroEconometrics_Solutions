"""Python script for C9, Chapter 3 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf


# Read in df
file = "./data/charity.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i) - iii)
lm = smf.ols('gift ~ mailsyear + giftlast + propresp', data=df).fit()
print(lm.summary())
print(">>>>")

lm = smf.ols('gift ~ mailsyear', data=df).fit()
print(lm.summary())
print(">>>>")

# iv) -v)
lm = smf.ols('gift ~ mailsyear + giftlast + propresp + avggift', data=df).fit()
print(lm.summary())
print(">>>>")
