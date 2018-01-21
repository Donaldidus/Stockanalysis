# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 17:47:36 2018

@author: Jan

Select data
"""
import os, fnmatch
import shutil

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def find_patterns(patterns, path):
    result = []
    for pattern in patterns:
        result.append(find(pattern, path))
    return result
    
def ticker2fn(ticker):
    ticker.lower();
    ticker = ticker + ".*"
    return ticker

tickers = []

for stock in SnP500:
    ticker = stock[0];
    ticker = ticker2fn(ticker);
    tickers.append(ticker)
    

# paths = find_patterns(tickers, 'Data/')

for path in paths:
    shutil.copy2(path[0], 'Data/SnP500/')



