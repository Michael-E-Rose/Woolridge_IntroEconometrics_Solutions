"""Python script for C3, Chapter 4 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/hprice1.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
formula1 = 'lprice ~ sqrft + bdrms'
lm1 = smf.ols(formula1, data=df).fit()
print(lm1.summary())
print(">>>>")

# ii) - iii)
df['test'] = df['sqrft'] - 150*df['bdrms']
formula2 = 'lprice ~ test + bdrms'
lm2 = smf.ols(formula2, data=df).fit()
print(lm2.summary())
print(">>>>")
