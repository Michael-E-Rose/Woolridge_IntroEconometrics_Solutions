"""Python script for C14, Chapter 7 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf

# Read in df
file = "./data/fertil2.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# NO DATA!

# i)
print(df.describe()['children'])
print(">>>>")
