"""Python script for C10, Chapter 7 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/nbasal.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
lm1 = smf.ols('points ~ exper + expersq + + guard + forward', data=df).fit()
print(lm1.summary())
print(">>>>")

# iv)
lm2 = smf.ols('points ~ exper + expersq + guard + forward + marr', data=df).fit()
print(lm2.summary())
print(">>>>")

# v)
df['marr_exper'] = df['marr'] * df['exper']
df['marr_expersq'] = df['marr'] * df['expersq']
lm3 = smf.ols('points ~ exper + expersq + guard + forward + marr + marr_exper + marr_expersq', data=df).fit()
print(lm3.summary())
print("F-test of joint statistical significance:")
print(lm3.f_test('(marr = 0), ( marr_exper = 0), ( marr_expersq = 0)'))
print(">>>>")

# v)
lm4 = smf.ols('assists ~ exper + expersq + + guard + forward + marr', data=df).fit()
print(lm4.summary())
print(">>>>")