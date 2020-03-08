"""Python script for C10, Chapter 4 of Wooldridge: Intr. Economometrics"""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/elem94_95.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
lm = smf.ols('lavgsal ~ bs', data=df).fit()
print(lm.summary())
print(">>>>")

# ii) - iv)
lm = smf.ols('lavgsal ~ bs + lenrol + lstaff', data=df).fit()
print(lm.summary())
print(">>>>")

# v)
lm = smf.ols('lavgsal ~ bs + lenrol + lstaff + lunch', data=df).fit()
print(lm.summary())
print(">>>>")