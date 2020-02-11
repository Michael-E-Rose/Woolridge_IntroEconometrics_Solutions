"""Python script for C3, Chapter 7 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/mlb1.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
formula = "lsalary ~ years + gamesyr + bavg + hrunsyr + rbisyr + runsyr + "\
          "fldperc + allstar + frstbase + scndbase + thrdbase + shrtstop + catcher"
lm = smf.ols(formula, data=df).fit()
print(lm.summary())

# ii)
R = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
print("F-test of joint statistical significance:")
print(lm.f_test(R))
