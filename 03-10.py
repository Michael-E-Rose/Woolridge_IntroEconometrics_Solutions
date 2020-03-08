"""Python script for C10, Chapter 3 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt


# Read in df
file = "./data/htv.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
print("Educ ranges from to: / Mean values for education and parents' education are:")
print(df.describe()[['educ', 'motheduc','fatheduc']])
print(">>>>")
print("Percentage of men that completed 12th grade:")
print((len(df.loc[df['educ'] == 12])/1230)*100)
print(">>>>")

# ii)
lm = smf.ols('educ ~ motheduc + fatheduc', data=df).fit()
print(lm.summary())
print(">>>>")

# iii)
lm = smf.ols('educ ~ motheduc + fatheduc + abil', data=df).fit()
print(lm.summary())
print(">>>>")

# iv)
lm = smf.ols('educ ~ motheduc + fatheduc + abil + np.power(abil, 2)', data=df).fit()
print(lm.summary())
print(">>>>")

# v)
print("Fraction of men that have “ability” less than the value calculated in the prev part")
print((len(df.loc[df['abil'] < - 4.01])))
print(">>>>")

# vi)
x = np.array(range(-10,6))
y = 8.2402 + 0.1901*12.18 + 0.1089*12.45 + 0.4015*x + 0.0506*x*x
plt.plot(x,y)
plt.xlabel('abil')
plt.ylabel('yhat')
plt.show()
print(">>>>")


