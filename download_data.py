# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 18:30:40 2018

@author: Jan
"""

import pandas_datareader.data as web
import pandas_datareader
import datetime
import os


start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2017, 12, 31)


failed_again = []
ticker = ''


for stock in failed:
    try:
        ticker = stock# stock[0].lower()
        filename = ticker + '.csv'
        path = 'Data/SnP500/' + filename
        
        if not os.path.exists(path):
            f = web.DataReader(ticker, 'yahoo', start, end)
            f.to_csv(path_or_buf=path, sep=';')
        
    except pandas_datareader._utils.RemoteDataError:
        failed_again.append(ticker)

failed = failed_again
