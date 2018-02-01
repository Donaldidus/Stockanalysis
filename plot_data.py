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
mpl.rcParams.update(pgf_with_rc_fonts)


plt.figure(figsize=(4.5,2.5))
plt.plot(days, stocks['aapl'], '#4CAF50', label='Apple')
plt.plot(days, stocks['msft'], '#673AB7', label='Microsoft')
plt.fill_between(days, stocks['aapl'], stocks['msft'], facecolor='#E1F5FE')
plt.tight_layout()
plt.xlabel("Days")
plt.ylabel(r"Stock Prize [\$]")
plt.legend(bbox_to_anchor=(0.95, 0.65))
plt.savefig('appl-vs-msft.pgf')