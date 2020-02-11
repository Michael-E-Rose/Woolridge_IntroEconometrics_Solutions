"""Python script for C1, Chapter 3 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "/home/MichaelERose/data/bwght.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# ii)
print("Pearson correlation between 'cigs' and 'faminc'")
corr = df['cigs'].corr(df['faminc'])
print(corr)
print(">>>>")

# iii)
formula1 = 'bwght ~ cigs'
lm1 = smf.ols(formula1, data=df).fit()
print(lm1.summary())
formula2 = formula1 + ' + faminc'
lm2 = smf.ols(formula2, data=df).fit()
print(lm2.summary())
print(">>>>")
