"""Python script for C8, Chapter 7 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf
import numpy as np
pd.set_option('display.max_columns', None)


# Read in df
file = "./data/loanapp.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")


# ii)
lm1 = smf.ols('approve ~ white', data=df).fit()
print(lm1.summary())
print(">>>>")

# iii)
lm2 = smf.ols('approve ~ white + hrat + obrat + loanprc + unem + male + married + dep + sch + cosign + chist + pubrec + mortlat1 + mortlat2 + vr', data=df).fit()
print(lm2.summary())
print(">>>>")

# iv)
lm3 = smf.ols('approve ~ white + white * obrat + hrat + obrat + loanprc + unem + male + married + dep + sch + cosign + chist + pubrec + mortlat1 + mortlat2 + vr', data=df).fit()
print(lm3.summary())
print(">>>>")

# v)
# CHECK AGAIN
#lm4 = smf.ols('approve ~ white + white * (obrat - 32) + hrat + obrat + loanprc + unem + male + married + dep + sch + cosign + chist + pubrec + mortlat1 + mortlat2 + vr', data=df).fit()
#print(lm4.summary())
#print(">>>>")