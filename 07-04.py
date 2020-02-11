"""Python script for C4, Chapter 7 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/gpa2.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# ii)
formula1 = "colgpa ~ hsize + hsizesq + hsperc + sat + female + athlete"
lm1 = smf.ols(formula1, data=df).fit()
print(lm1.summary())

# iii)
formula2 = "colgpa ~ hsize + hsizesq + hsperc + female + athlete"
lm2 = smf.ols(formula2, data=df).fit()
print(lm2.summary())

# iv)
formula3 = "colgpa ~ hsize + hsizesq + hsperc + female*athlete + (1-female)*athlete + (1-female)*(1-athlete)"
lm3 = smf.ols(formula3, data=df).fit()
print(lm3.summary())

# v)
# -
