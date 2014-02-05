#!/usr/bin/env python

import numpy
import pandas as pd

"""
df is the data frame
"""

df = pd.read_csv('../lesson02/nytimes.csv')

print "=== df ==="
print df
print "=== describe df ==="
print df.describe()
print "=== get the first 10 record ==="
print df[:10]

print "====="

# Create the average impressions and clicks for each age.

print "=== average impression and clicks for each age ==="

dfg = df[ ['Age', 'Impressions', 'Clicks'] ].groupby(['Age']).agg([numpy.mean])
print dfg[:10]

print "=== log impression ==="
df['log_impressions'] = df['Impressions'].apply(numpy.log)
print df.log_impressions

# Function that groups users by age.
def map_age_category(x):
    if x < 18:
        return '1'
    elif x < 25:
        return '2'
    elif x < 32:
        return '3'
    elif x < 45:
        return '4'
    else:
        return '5'

print "=== age category ==="
df['age_categories'] = df['Age'].apply(map_age_category)
print df.age_categories

