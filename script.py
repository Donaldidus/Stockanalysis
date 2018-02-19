# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 20:50:19 2018

@author: Jan
"""

import validate_data as val
import pandas as pd


# cluster_gics = val.sectors(cluster, stocks.columns, gics_dict)

crosstab = pd.crosstab(cluster_gics[2], cluster_gics[1])

test_stats = val.run_tests(cluster_gics[2], cluster_gics[1])
