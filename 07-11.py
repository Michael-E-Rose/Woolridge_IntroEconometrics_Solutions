"""Python script for C11, Chapter 7 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import statsmodels
pd.set_option('display.max_columns', None)


# Read in df
file = "./data/401ksubs.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
print(df.describe()['nettfa'])
print(">>>>")

# ii)
lm1 = smf.ols('nettfa ~ e401k', data=df).fit()
print(lm1.summary())
print(">>>>")

# iii)
lm2 = smf.ols('nettfa ~ inc + age + e401k + incsq + agesq', data=df).fit()
print(lm2.summary())
print(">>>>")

# iv)
#CHECK AGAIN
df['agenew'] = df['age'] - 41
lm3 = smf.ols('nettfa ~ inc + age + e401k + incsq + agesq + e401k * agenew + e401k * np.power(agenew, 2)', data=df).fit()
print(lm3.summary())
print(">>>>")

# vi)
fsize2 = df['fsize'] == 2
fsize3 = df['fsize'] == 3
fsize4 = df['fsize'] == 4
fsize5 = df['fsize'] >= 5
lm4 = smf.ols('nettfa ~ inc + age + e401k + incsq + agesq + fsize2 + fsize3 + fsize4 + fsize5', data=df).fit()
print(lm4.summary())
print(">>>>")

# vii)
print("The Chow statistic is:")
# CHECK AGAIN
# print((lm2.ssr() − lm4.ssr())/ lm4.ssr()] * (9245/20))







