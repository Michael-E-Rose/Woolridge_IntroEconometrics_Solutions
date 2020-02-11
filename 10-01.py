"""Python script for C1, Chapter 10 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/intdef.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# Example regression
formula1 = 'i3 ~ Q("inf") + Q("def")'
lm1 = smf.ols(formula1, data=df).fit()
print(lm1.summary())

# Define dummy variable
df['post_1979'] = (df['year'] > 1979)*1
print(df.head())
print(">>>>")

# Run regression
formula2 = formula1 + ' + post_1979'
lm2 = smf.ols(formula2, data=df).fit()
print(lm2.summary())
print(">>>>")
