"""Python script for C13, Chapter 7 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf
pd.set_option('display.max_columns', None)


# Read in df
file = "./data/apple.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

#NO DATA

# i)
df['ecobuy'] = (df.ecolbs > 0).astype(int)

# ii)
lm1 = smf.ols('ecobuy ~ ecoprc + regprc + faminc + hhsize + educ + age', data=df).fit()
print(lm1.summary())
print(">>>>")

# iii)
print("F-test of joint statistical significance:")
print(lm.f_test('(faminc = 0), (hhsize = 0), (educ = 0), (age = 0)'))
print(">>>>")

# iv)
lm2 = smf.ols('ecobuy ~ ecoprc + regprc + np.log(faminc) + hhsize + educ + age', data=df).fit()
print(lm2.summary())
print(">>>>")

# v)
# CHECK AGAIN

# vi)
# CHECK AGAIN