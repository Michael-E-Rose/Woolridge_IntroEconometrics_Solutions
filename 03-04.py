"""Python script for C4, Chapter 3 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/attend.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
print(df.describe()[['atndrte', 'priGPA', 'ACT']])
print(">>>>")

# ii)
formula = 'atndrte ~ priGPA + ACT'
lm = smf.ols(formula, data=df).fit()
print(lm.summary())
print(">>>>")

# iii)
p1 = pd.DataFrame({'intercept': 1, 'priGPA': [3.65], 'ACT': [20]})
print("Predicted attendance:")
print(lm.predict(p1))
print("Observations with these values:")
print(df[(df.priGPA == 3.65) & (df.ACT == 20)])
print(">>>>")

# iv)
p2 = pd.DataFrame({'intercept': 1, 'priGPA': [3.1, 2.1], 'ACT': [21, 26]})
preds = lm.predict(p2)
print("Difference in predicted attendance:")
print(preds[0] - preds[1])
