"""Python script for C11, Chapter 4 of Wooldridge: Intr. Economometrics"""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/htv.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
lm = smf.ols('educ ~ motheduc + fatheduc + abil + np.power(abil, 2)', data=df).fit()
print(lm.summary())
print(">>>>")

# ii)
print(lm.t_test('motheduc = fatheduc'))
print(">>>>")

# iii)
lm = smf.ols('educ ~ motheduc + fatheduc + abil + np.power(abil, 2) + tuit17 + tuit18', data=df).fit()
print(lm.summary())
print(lm.f_test('(tuit17 = 0), (tuit18 = 0)'))
print(">>>>")

# iv) - v)
print("The correlation between tuit17 and tuit18 is:")
print(df['tuit17'].corr(df['tuit18'])) 
print(">>>>")
avgtuit = (df['tuit17'] + df['tuit18'])/2
lm = smf.ols('educ ~ motheduc + fatheduc + abil + np.power(abil, 2) + avgtuit', data=df).fit()
print(lm.summary())
print(">>>>")

