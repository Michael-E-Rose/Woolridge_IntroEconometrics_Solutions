"""Python script for C9, Chapter 4 of Wooldridge: Intr. Economometrics"""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/discrim.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
lm = smf.ols('np.log(psoda) ~ prpblck + np.log(income) + prppov', data=df).fit()
print(lm.summary())
print(">>>>")

# ii)
print("The sample correlation between log(income) and prppov is:")
print(df['prppov'].corr(np.log(df['income']))) 
print(">>>>")

# iii) - v)
lm = smf.ols('np.log(psoda) ~ prpblck + np.log(income) + prppov + np.log(hseval)', data=df).fit()
print(lm.summary())
print(lm.f_test('(np.log(income) = 0), (prppov = 0)'))
print(">>>>")