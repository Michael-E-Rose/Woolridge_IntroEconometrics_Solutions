"""Python script for C8, Chapter 3 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf


# Read in df
file = "./data/discrim.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
print("Mean values are:")
print(df.describe()[['prpblck', 'income']])
print(">>>>")

# ii)
lm = smf.ols('psoda ~ prpblck + income', data=df).fit()
print(lm.summary())
print(">>>>")

# iii)
lm = smf.ols('psoda ~ prpblck', data=df).fit()
print(lm.summary())
print(">>>>")

# iv)
lm = smf.ols('np.log(psoda) ~ prpblck + np.log(income)', data=df).fit()
print(lm.summary())
print(">>>>")

# v)
lm = smf.ols('np.log(psoda) ~ prpblck + np.log(income) + prppov', data=df).fit()
print(lm.summary())
print(">>>>")

# vi) -vii)
print("The sample correlation between log(income) and prppov is:")
print(df['prppov'].corr(np.log(df['income']))) 
print(">>>>")