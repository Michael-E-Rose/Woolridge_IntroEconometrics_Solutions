"""Python script for C7, Chapter 10 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/consump.dta"
df = pd.read_stata(file)
print(df.head())
print(df.columns)
print(">>>>")

# i)
formula1 = 'gc ~ gy'
lm1 = smf.ols(formula1, data=df).fit()
print(lm1.summary())
print(">>>>")

# ii)
formula2 = formula1 + '+ gy_1'
lm2 = smf.ols(formula2, data=df).fit()
print(lm2.summary())

# iii)
formula3 = formula1 + '+ r3'
lm3 = smf.ols(formula3, data=df).fit()
print(lm3.summary())
