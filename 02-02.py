"""Python script for C2, Chapter 2 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/ceosal2.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
print("Mean values are:")
print(df.mean(axis=0)[:2])
print(">>>>")

# ii)
print("# of values in ceoten that are equal to 0:")
print(len(df.loc[df['ceoten'] == 0]))
print(">>>>")

# iii)
lm = smf.ols('lsalary ~ ceoten', data=df).fit()
print(lm.summary())
print(">>>>")
