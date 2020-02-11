"""Python script for C6, Chapter 10 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/fertil3.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
formula1 = 'gfr ~ t + tsq'
lm1 = smf.ols(formula1, data=df).fit()
print(lm1.summary())
df['resid'] = lm1.resid
print(">>>>")

# ii)
formula2 = formula1 + '+ pe + ww2 + pill'
lm2 = smf.ols(formula2, data=df).fit()
print(lm2.summary())
print(">>>>")

# iii)
formula3 = formula2 + '+t3'
df['t3'] = df['t']**3
lm3 = smf.ols(formula3, data=df).fit()
print(lm3.summary())
print(">>>>")
