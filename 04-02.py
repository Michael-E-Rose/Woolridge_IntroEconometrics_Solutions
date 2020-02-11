"""Python script for C2, Chapter 4 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/lawsch85.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
formula1 = 'lsalary ~ LSAT + GPA + llibvol + lcost + rank'
lm1 = smf.ols(formula1, data=df).fit()
print(lm1.summary())
print(">>>>")

# ii)
R1 = [[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0]]
print("F-test of joint statistical significance:")
print(lm1.f_test(R1))
print(">>>>")

# iii)
formula2 = formula1 + ' + clsize + faculty'
lm2 = smf.ols(formula2, data=df).fit()
print(lm2.summary())
R2 = [[0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
print("F-test of joint statistical significance:")
print(lm2.f_test(R2))
print(">>>>")
