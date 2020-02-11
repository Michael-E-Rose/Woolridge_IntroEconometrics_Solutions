"""Python script for C2, Chapter 7 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/wage2.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
formula1 = 'lwage ~ educ + exper + tenure + not_married + black + south + urban'
lm1 = smf.ols(formula1, data=df).fit()
print(lm1.summary())
print(">>>>")

# ii)
df['exper2'] = df['exper']**2
df['tenure2'] = df['tenure']**2
formula2 = formula1 + " + exper2 + tenure2"
lm2 = smf.ols(formula2, data=df).fit()
R = [[0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
print("F-test of joint statistical significance:")
print(lm2.f_test(R))
print(">>>>")
