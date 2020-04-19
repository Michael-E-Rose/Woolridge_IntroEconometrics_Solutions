"""Python script for C5, Chapter 5 of Wooldridge: Intr. Economometrics"""

import pandas as pd
import seaborn


# i)
# Read in df
file = "./data/htv.dta"
df = pd.read_stata(file)
print(df.head())
print(">>>>")

# We want to see how many different values are in the educ column 
df.educ.unique()

# There are 15 different values taken by educ in the sample

# Educ does not have a continuous distribution since the values of
# this variable are all discrete positive integers. 

# ii) Now we plot a histogram with an overlaying normal distribution curve 
educ = df.educ
seaborn.distplot(educ, bins=None, hist=True, kde=True)

# The variable educ does not seem to follow a normal distribution.
