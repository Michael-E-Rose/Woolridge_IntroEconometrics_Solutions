"""Python script for C5, Chapter 4 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/mlb1.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
formula2 = 'lsalary ~ years + gamesyr + bavg + hrunsyr'
lm1 = smf.ols(formula2 + " + rbisyr", data=df).fit()
lm2 = smf.ols(formula2, data=df).fit()
print(lm1.summary())
print(lm2.summary())
print(">>>>")

# ii)
formula3 = formula2 + " + runsyr + fldperc + sbasesyr"
lm3 = smf.ols(formula3, data=df).fit()
print(lm3.summary())
print(">>>>")

# iii)
R = [[0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 1]]
print("F-test of joint statistical significance:")
print(lm3.f_test(R))
print(">>>>")
