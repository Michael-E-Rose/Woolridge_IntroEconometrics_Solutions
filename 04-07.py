"""Python script for C7, Chapter 4 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/twoyear.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
print(df.describe()['phsrank'][['mean', 'min', 'max']])
print(">>>>")

# ii)
formula1 = 'lwage ~ jc + totcoll + exper + phsrank'
lm1 = smf.ols(formula1, data=df).fit()
print(lm1.summary())
print(">>>>")

# iii)
formula2 = 'lwage ~ jc + totcoll + exper'
lm2 = smf.ols(formula2, data=df).fit()
print(lm2.summary())
print(">>>>")

# iv)
formula3 = formula1 + " + id"
lm3 = smf.ols(formula3, data=df).fit()
print(lm3.summary())
print(">>>>")
