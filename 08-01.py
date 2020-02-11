"""Python script for C1, Chapter 8 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/sleep75.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# ii - iii)
formula1 = "sleep ~ totwrk + educ + age + agesq + yngkid + male"
lm1 = smf.ols(formula1, data=df).fit()
df['residsq'] = lm1.resid**2
formula2 = "residsq ~ male"
lm2 = smf.ols(formula2, data=df).fit()
print(lm2.summary())

