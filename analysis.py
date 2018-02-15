# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 17:28:04 2018

@author: Jan
"""
import numpy as np


# scales a series of data points by it's mean
def rm_offset(a: np.ndarray) -> np.ndarray:
    b = np.subtract(a, np.mean(a, axis=0))
    return b

# scales a series of data points by it's standard deviation
def scale_amplitude(a: np.ndarray) -> np.ndarray:
    b = np.divide(a, np.std(a, axis=0))
    return b

# performs both rm_offset and then scale_amplitude
def rm_off_amp(a: np.ndarray) -> np.ndarray:
    b = rm_offset(a)
    b = scale_amplitude(b)
    return b