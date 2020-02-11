"""Python script for C2, Chapter 3 of Wooldridge: Intr. Economometrics"""
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.graphics.api as smg


# Read in df
file = "/home/MichaelERose/data/hprice1.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
formula = 'price ~ sqrft + bdrms'
lm = smf.ols(formula, data=df).fit()
print(lm.summary())
print(">>>>")

# ii)
print("Coefficient b_2 is:")
print(lm.params['bdrms'])
print(">>>>")

# iii)
x = 140*lm.params['sqrft'] + lm.params['bdrms']
print("Estimated increase in price for a house:")
print(x)
print(">>>>")

# iv)
print("Explained variation is:")
print(lm.rsquared)
print(">>>>")

# v)
print("Estimated price for first house:")
print(lm.predict()[0])
fig = plt.figure(figsize=(12,8))
fig = smg.plot_partregress_grid(lm, fig=fig)
plt.show()
print(">>>>")
