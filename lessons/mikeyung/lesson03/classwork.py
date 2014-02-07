#!/usr/bin/env python

"""

Classwork for Lesson 03
Michael Yung

"""

from __future__ import division
import numpy as np
import pandas as pd

"""
Function to create the CTR for each group
"""

def Click_thru(imp, click):
    if imp > 0:
        return click / imp
    else:
        return 0

"""
df is the data frame, append from the CSV files of New York Times
"""

df = pd.DataFrame()

# 1 to 31
# http://stat.columbia.edu/~rachel/datasets/nyt1.csv

for i in range(1,31):
    path ='http://stat.columbia.edu/~rachel/datasets/nyt%d.csv' % i
    print "Processing :", path
    frame = pd.read_csv(path)
    print 'Obtained', len(frame), 'records'
    df = df.append(frame)

print "=== df ==="
print df
print "=== describe df ==="
print df.describe()

"""
dfg is the data frame grouped by Age, Gender and Signed_In
"""

dfg = df[['Age', 'Gender', 'Signed_In', 'Impressions', 'Clicks']].groupby(['Age', 'Gender', 'Signed_In']).sum()

print "=== Sum of impression and clicks for each age, gender, signed_in ==="
print dfg[:10]

"""
Add extra column with CTR
"""

dfg['CTR'] = map(Click_thru, dfg['Impressions'], dfg['Clicks'])

print "=== Dataframe with CTR for each age, gender, signed_in ==="
print dfg[:10]

"""
Output the data frame to CSV files
"""

dfg.to_csv('nytimes_aggregation.csv')
