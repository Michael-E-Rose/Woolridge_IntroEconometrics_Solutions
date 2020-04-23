"""Python script for C12, Chapter 7 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
pd.set_option('display.max_columns', None)


# Read in df
file = "./data/beauty.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
dfmen = df.loc[df['female'] == 0]
print("Fraction of men with above average looks:")
print(len(dfmen[dfmen['abvavg'] == 1]) / len(dfmen))
print("Fraction of men with below average looks:")
print(len(dfmen[dfmen['belavg'] == 1]) / len(dfmen))

dfwomen = df.loc[df['female'] == 1]
print("Fraction of women with above average looks:")
print(len(dfwomen[dfwomen['abvavg'] == 1]) / len(dfwomen))
print("Fraction of women with below average looks:")
print(len(dfwomen[dfwomen['belavg'] == 1]) / len(dfwomen))
print(">>>>")

# ii)
lm1 = smf.ols('abvavg ~ female', data=df).fit()
print(lm1.summary())
print(">>>>")

# iii)
print("Results for men:")
lm2 = smf.ols('lwage ~ belavg + abvavg', data=dfmen).fit()
print(lm2.summary())

print("Results for women:")
lm3 = smf.ols('lwage ~ belavg + abvavg', data=dfwomen).fit()
print(lm3.summary())
print(">>>>")

# v)
print("Results for men:")
lm4 = smf.ols('lwage ~ belavg + abvavg + educ + exper + expersq + union + goodhlth + black + married + south + bigcity + smllcity + service', data=dfmen).fit()
print(lm4.summary())

print("Results for women:")
lm5 = smf.ols('lwage ~ belavg + abvavg + educ + exper + expersq + union + goodhlth + black + married + south + bigcity + smllcity + service', data=dfwomen).fit()
print(lm5.summary())
print(">>>>")

# vi)
# CHECK AGAIN (similar to ssr from C7.11)

