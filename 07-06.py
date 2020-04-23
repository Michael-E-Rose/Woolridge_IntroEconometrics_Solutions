"""Python script for C6, Chapter 7 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf
import numpy as np
import statsmodels.api as sm


# Read in df
file = "./data/sleep75.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
print("Results for men:")
dfmen = df.loc[df['male'] == 1]
lm1 = smf.ols('sleep ~ totwrk + educ + age + agesq + yngkid', data=dfmen).fit()
print(lm1.summary())

print("Results for women:")
dfwomen = df.loc[df['male'] == 0]
lm2 = smf.ols(' sleep ~ totwrk + educ + age + agesq + yngkid', data=dfwomen).fit()
print(lm2.summary())
print(">>>>")

# ii)
df['totwrk_male'] = df['totwrk'] * df['male']
df['educ_male'] = df['educ'] * df['male']
df['age_male'] = df['age'] * df['male']
df['agesq_male'] = df['agesq'] * df['male']
df['yngkid_male'] = df['yngkid'] * df['male']
lm3 = smf.ols('sleep ~ totwrk + educ + age + agesq + yngkid + male + totwrk_male + educ_male + age_male + agesq_male + yngkid_male', data=df).fit()
print("F-test of joint statistical significance:")
# CHECK AGAIN
# Normaler F-Test nicht möglich -> Anova Alternative?
#print(sm.stats.anova_lm(lm3))
#print(lm3.f_test('(male = 0), (totwrk_male = 0), (educ_male = 0), (age_male = 0), (male_agesq = 0), (yngkid_male = 0)'))
print(">>>>")

# iii)
print("F-test of joint statistical significance:")
print(lm3.f_test('(totwrk_male = 0), (educ_male = 0), (age_male = 0), (agesq_male = 0), (yngkid_male = 0)'))
print(">>>>")