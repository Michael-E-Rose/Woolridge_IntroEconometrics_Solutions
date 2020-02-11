"""Python script for C1, Chapter 7 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/gpa1.dta"
df = pd.read_stata(file)
print(df.head())
print(list(df.columns.values))
print(">>>>")

# i)
formula1 = 'colGPA ~ PC + hsGPA + ACT'
lm1 = smf.ols(formula1, data=df).fit()
formula2 = formula1 + '+ mothcoll + fathcoll'
lm2 = smf.ols(formula2, data=df).fit()
print(lm1.summary())
print(lm2.summary())
print(">>>>")

# ii)
R = [[0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]
print("F-test of joint statistical significance:")
print(lm2.f_test(R))
print(">>>>")

# iii)
df['hsGPA2'] = df['hsGPA']**2
formula3 = formula2 + ' + hsGPA2'
lm3 = smf.ols(formula3, data=df).fit()
print(lm3.summary())
print(">>>>")
