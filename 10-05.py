"""Python script for C5, Chapter 10 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/ezanders.dta"
df = pd.read_stata(file)
print(df.head())
print(df.columns)
print(">>>>")

# i)
df['trend'] = range(0, len(df))
formula1 = "luclms ~ trend"
months = df.columns[-12:-1]
print(months)
dummies = ' + '.join(months)
formula += dummies
print(formula1)
lm1 = smf.ols(formula1, data=df).fit()
print(lm1.summary())
print(">>>>")

# ii)
formula2 = formula2 + '+ ez'
lm2 = smf.ols(formula2, data=df).fit()
print(lm2.summary())
