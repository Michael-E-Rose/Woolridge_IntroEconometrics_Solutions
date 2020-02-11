"""Python script for C1, Chapter 2 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/401k.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
print("Mean values are:")
print(df.describe())[['prate', 'mrate']])
print(">>>>")

# ii) - v)
lm = smf.ols('prate ~ mrate', data=df).fit()
print(lm.summary())
print(">>>>")
