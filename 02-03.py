"""Python script for C3, Chapter 2 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/sleep75.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
formula = 'sleep ~ totwrk'
lm = smf.ols(formula, data=df).fit()
print(lm.summary())
print(">>>>")

# ii)
x = lm.params['totwrk']*2*60
print("Decrease in sleep (in minutes) for additional two hours work:")
print(x)
print(">>>>")
