"""Python script for C2, Chapter 10 of Wooldridge: Intr. Economometrics"""
import pandas as pd
import statsmodels.formula.api as smf


# Read in df
file = "./data/barium.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# i)
trend = []
for i in range(0, len(df)):
    trend.append(i)
df['trend'] = trend
formula1 = 'lchnimp ~ lchempi + lgas + lrtwex + befile6 + affile6 + afdec6 + trend'
lm1 = smf.ols(formula1, data=df).fit()
print(lm1.summary())
print(">>>>")

# ii)
# See above

# iii)
df['spring'] = df['feb'] + df['mar'] + df['apr']
df['summer'] = df['may'] + df['jun'] + df['jul']
df['fall'] = df['aug'] + df['sep'] + df['oct']
formula2 = formula1 + ' + spring + summer + fall'
lm2 = smf.ols(formula2, data=df).fit()
print(lm2.summary())
print(">>>>")
