"""Python script for C8, Chapter 4 of Wooldridge: Intr. Economometrics"""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy import stats


# Read in df
file = "./data/401ksubs.dta"
df = pd.read_stata(file)
df = df.loc[df['fsize'] == 1]
print(df.head())
print(">>>>")

# i)
print("Number of single-person households:")
print(df.shape[0])

# ii)
formula = 'nettfa ~ inc + age'
lm1 = smf.ols(formula, data=df).fit()
print(lm1.summary())
print(">>>>")

# iv)
beta_2 = 1
t_statistic = (lm1.params['age'] - beta_2) / lm1.bse['age']
p_val = stats.t.sf(np.abs(t_statistic), lm1.nobs-1)
print("T-Statistic and p-value are:")
print(t_statistic, p_val)
print(">>>>")

# v)
formula1 = 'nettfa ~ inc'
lm2 = smf.ols(formula2, data=df).fit()
print(lm2.params)
print(">>>>")
