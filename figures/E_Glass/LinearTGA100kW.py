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
fileName = 'Linear/E_GlassOldLinearNominal100KW_0_cone_Mass.csv'
df = pd.read_csv(fileName, skiprows=0)
dfMassNorminal = df[['# Time [s]',' Mass [Kg]']]  # select time and MLR for 1D plot
dfMassNorminal = np.transpose(np.array(dfMassNorminal))

fileName = 'Linear/E_GlassOldLinearTGA100KW_0_cone_Mass.csv'
df = pd.read_csv(fileName, skiprows=0)
dfMassTGA = df[['# Time [s]',' Mass [Kg]']]  # select time and MLR for 1D plot
dfMassTGA = np.transpose(np.array(dfMassTGA))

fileName = 'Linear/E_GlassOldLinearHybrid100KW_0_cone_Mass.csv'
df = pd.read_csv(fileName, skiprows=0)
dfMassHybrid = df[['# Time [s]',' Mass [Kg]']]  # select time and MLR for 1D plot
dfMassHybrid = np.transpose(np.array(dfMassHybrid))

# %%
# Data processing
# Normalizing mass
dfMassNorminal[1,:] = dfMassNorminal[1,:]/dfMassNorminal[1,0]
dfMassHybrid[1,:] = dfMassHybrid[1,:]/dfMassHybrid[1,0]
dfMassTGA[1,:] = dfMassTGA[1,:]/dfMassTGA[1,0]

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
plt.plot(dfMassNorminal[0], dfMassNorminal[1], '-k', marker='o', markerfacecolor='none', markevery=30, linewidth=1.0)
plt.plot(dfMassHybrid[0], dfMassHybrid[1], '--', marker='^', markerfacecolor='none', markevery=30, color=colors[0], linewidth=1.0)
plt.plot(dfMassTGA[0], dfMassTGA[1], '-.', marker='v', markerfacecolor='none', markevery=30, color=colors[1], linewidth=1.0)
plt.xlabel('Time (s)', fontname='Times New Roman', fontsize=fsize)
plt.ylabel(r'Normalized Mass', fontname='Times New Roman', fontsize=fsize)
leg = ('Virtual', 'Hybrid TGA DSC', 'Hybrid TGA')
H = plt.legend(leg, loc='upper right', prop={'size': 16}, numpoints=1,
               frameon=False)
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
plt.axis([0, 300, 0.70, 1.05])
# Save figures
plt.tight_layout()
plt.savefig('E_Glass_Linear_100kW_Mass_Comparison_TGA.png', dpi=300)
plt.show()
plt.close()
