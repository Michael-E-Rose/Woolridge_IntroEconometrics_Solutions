"""Python script for C3, Chapter 3 of Wooldridge: Intr. Economometrics"""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/ceosal2.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
formula1 = "lsalary ~ lsales + lmktval"
lm1 = smf.ols(formula1, data=df).fit()
print(lm1.summary())
print(">>>>")

# ii)
print("Summary of 'profits':")
print(df.describe()['profits']) # contains negative values
df['lprofits'] = np.log(df['profits'])
print("Number of NaN in 'lprofits':")
print(df['lprofits'].isnull().sum()) # contains NaN's
formula2 = formula1 + ' + profits'
lm2 = smf.ols(formula2, data=df).fit()
print(lm2.summary())
print(">>>>")

# iii)
formula3 = formula2 + '+ ceoten'
lm3 = smf.ols(formula3, data=df).fit()
print(lm3.summary())
print(">>>>")

# iv)
corr = df['mktval'].corr(df['profits'])
print("Correlation between 'lmktval' and 'profits' is:")
print(corr)
