"""Python script for C5, Chapter 3 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/wage1.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# Partialling out
formula1 = 'educ ~ exper + tenure'
lm1 = smf.ols(formula1, data=df).fit()
df['res'] = lm1.resid
formula2 = 'lwage ~ res'
lm2 = smf.ols(formula2, data=df).fit()
print("Coefficient of residuals from 'educ ~ exper + tenure' on 'lwage':")
print(lm2.params['res'])
formula3 = 'lwage ~ educ + exper + tenure'
lm3 = smf.ols(formula3, data=df).fit()
print("Coefficient of educ on 'lwage':")
print(lm3.params['educ'])