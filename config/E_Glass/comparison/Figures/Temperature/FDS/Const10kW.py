################################################################################
'''
Purpose: Plot 1D line figures
Author: Fengchang Yang
Date: 06/06/2018
'''
################################################################################
# Import useful modules
from __future__ import division
import numpy as np
import numba as nb
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

################################################################################
# Program space
# %%
# Read data from csv files
fileName = 'Const/E_GlassOldConstNominal10KW_s0_devc.csv'
df = pd.read_csv(fileName, skiprows=1)
dfTempNorminal = df[['Time','Wall_temperature','Back_wall_temperature']]  # select time and MLR for 1D plot
dfTempNorminal = np.transpose(np.array(dfTempNorminal))

fileName = 'Const/E_GlassOldConstWide10KW_s0_devc.csv'
df = pd.read_csv(fileName, skiprows=1)
dfTempWide = df[['Time','Wall_temperature','Back_wall_temperature']]  # select time and MLR for 1D plot
dfTempWide = np.transpose(np.array(dfTempWide))

fileName = 'Const/E_GlassOldConstHybrid10KW_s0_devc.csv'
df = pd.read_csv(fileName, skiprows=1)
dfTempHybrid = df[['Time','Wall_temperature','Back_wall_temperature']]  # select time and MLR for 1D plot
dfTempHybrid = np.transpose(np.array(dfTempHybrid))

# %%
# Data processing
# Normalizing Temp

################################################################################
# %%
# Custom greek font in label
plt.rc('font', family='serif')
plt.rc('font', serif='Times New Roman')
mpl.rcParams['mathtext.fontset'] = 'custom'
mpl.rcParams['mathtext.rm'] = 'Times New Roman'

# RGB color schemes from matlab
colors = [(0, 0.447, 0.7410), (0.8500, 0.3250, 0.0980),
          (0.9290, 0.6940, 0.1250)]

# Figure parameters
fsize = 20
hsize = 16
fwidth = 6.5
fwidthlong = 6.5 * 2
fheight = 5
fwidthlong = 6.5 * 2

# %%
# Figure #1
fig1 = plt.figure(figsize=(fwidth, fheight))
plt.plot(dfTempNorminal[0], dfTempNorminal[1], '-k', marker='o', markerfacecolor='none', markevery=150, linewidth=1.5)
plt.plot(dfTempHybrid[0], dfTempHybrid[1], '-', marker='^', markerfacecolor='none', markevery=150, color=colors[0], linewidth=1.5)
plt.plot(dfTempWide[0], dfTempWide[1], '-', marker='v', markerfacecolor='none', markevery=150, color=colors[1], linewidth=1.5)
plt.plot(dfTempNorminal[0], dfTempNorminal[2], '--k', marker='o', markerfacecolor='none', markevery=150, linewidth=1.5)
plt.plot(dfTempHybrid[0], dfTempHybrid[2], '--', marker='^', markerfacecolor='none', markevery=150, color=colors[0], linewidth=1.5)
plt.plot(dfTempWide[0], dfTempWide[2], '--', marker='v', markerfacecolor='none', markevery=150, color=colors[1], linewidth=1.5)
plt.xlabel('Time (s)', fontname='Times New Roman', fontsize=fsize)
plt.ylabel(r'Temperature ($^o$C)', fontname='Times New Roman', fontsize=fsize)
leg = ('Virtual', 'Hybrid', 'Full')
H = plt.legend(leg, loc='lower right', prop={'size': 16}, numpoints=1,
               frameon=False)
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
plt.axis([0, 3500, 20, 350])
# Save figures
plt.tight_layout()
plt.savefig('E_Glass_Old_Const_10kW_Temp_Comparison.png', dpi=300)
plt.show()
plt.close()
