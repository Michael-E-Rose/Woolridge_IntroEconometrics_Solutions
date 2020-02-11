"""Python script for C2, Chapter 8 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/hprice1.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
formula = 'price ~ lotsize + sqrft + bdrms'
lm = smf.ols(formula, data=df).fit()
print(lm.summary())
print(lm.HC0_se)

# ii)
# -