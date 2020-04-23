"""Python script for C5, Chapter 7 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf
import numpy as np


# Read in df
file = "./data/ceosal1.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
df['rosneg'] = (df.ros < 0).astype(int)
lm = smf.ols('np.log(salary) ~ np.log(sales) + roe + rosneg', data=df).fit()
print(lm.summary())
print(">>>>")

