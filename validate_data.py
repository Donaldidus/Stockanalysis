# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 22:55:36 2018

@author: Jan
"""


def stock_sectors(df, ticker='Ticker symbol', gics='GICS Code') -> dict:
    gics_stocks = {}
    
    for _, row in df.iterrows():
        if row[gics] in gics_stocks:
            gics_stocks[row[gics]].append(row[ticker].lower())
        else:
            gics_stocks[row[gics]] = [row[ticker].lower()]
        
    return gics_stocks

# computes the conformatiy of the clusters (n) and the validation data (m) to 
# the keys
# returns number of same datapoints for each combination (n * m) values
def validate_cl(cluster: dict, validation: dict):
    conformity = []
    
    for key_cl in cluster:
        for key_val in validation:
            conformity.append(len(set(cluster[key_cl]).intersection(validation[key_val])))
            
    return conformity