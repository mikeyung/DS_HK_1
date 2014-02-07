#!/usr/bin/env python

from __future__ import division
import pandas as pd

def get_nytimes_datasets(n):
    """
    request NYT datasets
    @param int n     number of CSVs to obtain
    @return list      list of CSVs
    """
    assert n < 21
    df = pd.DataFrame()
    for i in range(1,n+1):
        url = 'http://stat.columbia.edu/~rachel/datasets/nyt'+str(i)+'.csv'
        print 'Retrieving...', url
        csv = pd.read_csv(url)
        print 'Obtained', len(csv), 'records'
        df = df.append(csv)
    return df

def ratio(x,y):
    if y != 0:
        return x/y
    else:
        return 0

df = get_nytimes_datasets(2)

df["CTR"] = map(ratio, df["Clicks"], df["Impressions"])

df.to_csv('nytimes_aggregation.csv')