"""Python script for C6, Chapter 3 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/wage2.DTA"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
lm1 = smf.ols('IQ ~ educ', data=df).fit()
delta_1_t = lm1.params['educ']
print("delta_1 tilde is:")
print(delta_1_t)
print(">>>>")

# ii)
lm2 = smf.ols('lwage ~ educ', data=df).fit()
beta_1_t = lm2.params['educ']
print("beta_1 tilde is:")
print(beta_1_t)
print(">>>>")

# iii)
lm3 = smf.ols('lwage ~ educ + IQ', data=df).fit()
beta_1_h, beta_2_h = lm3.params[['educ', 'IQ']]
print("beta_1 tilde and beta_2 tilde are:")
print(beta_1_h, beta_2_h)
print(">>>>")

# iv)
print("beta_1_t", beta_1_t)
print("beta_1_h + beta_2_h*delta_1_t", beta_1_h + beta_2_h*delta_1_t)
print(round(beta_1_t, 16) == round(beta_1_h + beta_2_h*delta_1_t, 16))
