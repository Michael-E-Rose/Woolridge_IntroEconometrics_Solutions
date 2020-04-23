"""Python script for C7, Chapter 7 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf
import numpy as np


# Read in df
file = "./data/wage1.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
lm1 = smf.ols('lwage ~ female + educ + female * educ + exper + expersq + tenure + tenursq', data=df).fit()
print(lm1.summary())
print("The approximate proportionate difference in estimated wage between women and men is:")
print("when educ = 12.5:")
print(- 0.2268 - 0.0056 * 12.5)
print("when educ = 0:")
print(- 0.2268 - 0.0056 * 0)
print(">>>>")

# ii)
# CHECK AGAIN
df['educnew'] = df['educ'] - 12.5
lm2 = smf.ols('lwage ~ female + educ + female * educnew + exper + expersq + tenure + tenursq', data=df).fit()
print(lm2.summary())
print(">>>>")

