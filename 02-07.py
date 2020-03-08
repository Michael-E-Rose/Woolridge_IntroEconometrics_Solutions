"""Python script for C7, Chapter 2 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/charity.dta"
df = pd.read_stata(file)
#print(df.head())
print(">>>>")

# i)
print("The mean values is:")
print(df.describe()['gift'])
print("# of people that gave no gift is:")
print(len(df.loc[df['gift'] == 0]))
print("In percent:")
print((len(df.loc[df['gift'] == 0])/4268)*100)
print(">>>>")

# ii)
print("The mean, min and max values of mailings per year are:")
print(df.describe()['mailsyear'])
print(">>>>")

# iii) - iv)
lm = smf.ols('gift ~ mailsyear', data=df).fit()
print(lm.summary())
print(">>>>")

# v)
print("The smallest predicted value of gifts is:")
print(2.01 + 2.65 * 0.25)
print(">>>>")
