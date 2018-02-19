# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 22:55:36 2018

@author: Jan
"""
import pandas as pd
import scipy.stats as stats
import sklearn.metrics as metrics


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


# returns a dataframe with tickers, cluster centers and the gics sectors
def sectors(cluster_center, tickers, gics: dict) -> pd.DataFrame:
    gics_ordered = []
    
    for ticker in tickers:
        gics_ordered.append(gics[ticker.upper()])
    
    return pd.DataFrame(data=[tickers, cluster_center, gics_ordered]).transpose()


# runs all current tests on the data
def run_tests(reference, cluster):
    # compute crosstab of reference data and cluster
    crosstab = pd.crosstab(reference, cluster)
    # chi squared contingency test with chi sq statistic
    chi_sq = stats.chi2_contingency(crosstab)
    # G-test
    g_test = stats.chi2_contingency(crosstab, lambda_="log-likelihood")
    # Ajusted Rand Index
    adi = metrics.adjusted_rand_score(reference, cluster)
    
    hom_completeness_v_measure = metrics.homogeneity_completeness_v_measure(reference, cluster)
    
    ami = metrics.adjusted_mutual_info_score(reference, cluster)
    
    fms = metrics.fowlkes_mallows_score(reference, cluster)
        
    return chi_sq, g_test, (adi, hom_completeness_v_measure[0], hom_completeness_v_measure[1], hom_completeness_v_measure[2], ami, fms)