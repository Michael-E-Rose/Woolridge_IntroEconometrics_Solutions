"""Python script for C4, Chapter 5 of Wooldridge: Intr. Economometrics"""

import numpy as np
import pylab as p  
import scipy
import pandas as pd

# i)
# Read in df
file = "./data/401ksubs.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# We only want to keep observations with fsize = 1 
is_fsize1 =  df['fsize']==1
df_fsize1 = df[is_fsize1]

# Now we have to find the skewness of inc and the logarithm of inc

from sklearn import preprocessing

# Skewness of inc
scipy.stats.skew(df_fsize1.inc)

# Skewness of the logarithm of inc

inc = df_fsize1.inc
log_income = np.log(inc)
scipy.stats.skew(log_income)

# The measure of skewness for inc is around 1.86 and the measure of skewness
# for the logarithm of inc is around 0.36. Inc has more skewness and is
# hence less likely to follow a normal distribution compared
# to the logarithm of inc.

# ii) Now we want to use bwght2.dta to find 
# the skewness measures of bwght and log(bwght). 

# Read in df
next_file = "./data/bwght2.dta"
df2 = pd.read_stata(next_file)
print(df2.head())
print(">>>>")

# Find the skewness measure for bwght
bwght = df2.bwght
scipy.stats.skew(bwght)

# Find the skewness measure for log(bwght)
log_bwght=np.log(bwght)
scipy.stats.skew(log_bwght)

# Here the skewness of bwght is around -0.6 and the skewness of
# log(bwght) is around -2.95. In this case there is more skewness
# after taking the natural logarithm of bwght. 

# iii) The example in part ii) demonstrates that this statement does
# not hold generally. It is possible to introduce skewness by taking
# the natural logarithm of a variable. 

# iv) For the purposes of regression analysis, we should be studying the
# conditional distributions; that is, the distributions of y and log(y)
# conditional on the explanatory variables, x1, ..., xk . If we think the mean
# is linear, as in Assumptions MLR.1 and MLR.3, then this is equivalent to
# studying the distribution of the population error, u. In fact, the skewness
# measure studied in this question often is applied to
# the residuals from and OLS regression.
