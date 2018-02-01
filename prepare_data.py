# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 17:47:36 2018

@author: Jan

Select data
"""
import os, fnmatch
import pandas
import numpy as np
import statsmodels.api as sm

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
def read_data(path, sep: str, usecols=None):
    data_frames = []
    file_names = []
    for file in os.listdir(path):
        if file[-4:] == '.csv':
            file_names.append(file[:-4])
            data_frames.append(pandas.read_csv(path + '/' + file, sep=sep, usecols=usecols))
            
    data_frame = pandas.concat(data_frames, axis=1)
    data_frame.columns = file_names
    
    return data_frame, file_names
        
# converts a list of data frames to a numpy array
# uses 2D if column
def convert_dataset(data_frames: list, df_columns: list) -> np.array:
    num_rows = len(data_frames)
    num_cols = data_frames[0].shape[0]
    
    # if there's more than one column per data frame use 3D array
    if len(df_columns) > 1:
        n_array = np.zeros((num_rows, num_cols, len(df_columns)))
    else:
        n_array = np.zeros((num_rows, num_cols))
    
    for i, data_frame in enumerate(data_frames):
        if len(df_columns) > 1:
            n_array[i] = data_frame.as_matrix(df_columns).reshape((num_cols, len(df_columns)))
        else:
            n_array[i] = data_frame.as_matrix(df_columns).reshape(num_cols)
            
    return n_array
