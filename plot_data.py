# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 22:43:56 2018

@author: Jan
"""

import matplotlib as mpl
import matplotlib.pyplot as plt


mpl.use("pgf")
pgf_with_rc_fonts = {
    "font.family": "serif",
    "font.serif": [],                   # use latex default serif font
    "font.sans-serif": ["DejaVu Sans"], # use a specific sans-serif font
}
plt.rcParams['axes.unicode_minus'] = False
mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams.update(pgf_with_rc_fonts)


plt.figure(figsize=(4.5,2.5))
plt.plot(days, stocks_adj['aapl'], '#4CAF50', label='Apple')
plt.plot(days, stocks_adj['msft'], '#673AB7', label='Microsoft')
plt.fill_between(days, stocks_adj['aapl'], stocks_adj['msft'], facecolor='#E1F5FE')
plt.tight_layout()
plt.xlabel("days")
plt.ylabel(r"stock prize in dollar")
plt.legend(bbox_to_anchor=(0.98, 0.35))
plt.savefig('appl-vs-msft_adj.pgf')