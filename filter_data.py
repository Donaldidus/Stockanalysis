# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 17:47:36 2018

@author: Jan

Select data
"""
import os, fnmatch
import pandas
import numpy as np

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
    
# reads all csv files in the given directory and returns a list of the data 
# frames
def read_data(path, sep: str):
    data_frames = []
    for file in os.listdir(path):
        if file[-4:] == '.csv':
            data_frames.append(pandas.read_csv(path + '/' + file ,sep=sep))
    
    return data_frames
    
        
# converts a list of data frames to a numpy array
def convert_dataset(data_frames: list, columns: list) -> np.array:
    num_rows = len(data_frames)
    num_cols = data_frames[0].shape[0]
    
    if len(columns) > 1:
        n_array = np.zeros((num_rows, num_cols, len(columns)))
    else:
        n_array = np.zeros((num_rows, num_cols))
    
    for i, data_frame in enumerate(data_frames):
        n_array[i] = data_frame.as_matrix(columns).reshape(num_cols)
    
    return n_array

