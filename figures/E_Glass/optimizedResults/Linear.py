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
fileName = 'E_GlassOldLinearNominal_0_cone_Mass.csv'
df = pd.read_csv(fileName, skiprows=0)
dfMassNorminal = df[['# Time [s]',' Mass [Kg]']]  # select time and MLR for 1D plot
dfMassNorminal = np.transpose(np.array(dfMassNorminal))

fileName = 'E_GlassOldLinearWide_0_cone_Mass.csv'
df = pd.read_csv(fileName, skiprows=0)
dfMassWide = df[['# Time [s]',' Mass [Kg]']]  # select time and MLR for 1D plot
dfMassWide = np.transpose(np.array(dfMassWide))

fileName = 'E_GlassOldLinearTight_0_cone_Mass.csv'
df = pd.read_csv(fileName, skiprows=0)
dfMassTight = df[['# Time [s]',' Mass [Kg]']]  # select time and MLR for 1D plot
dfMassTight = np.transpose(np.array(dfMassTight))

# %%
# Data processing
# Normalizing mass
dfMassNorminal[1,:] = dfMassNorminal[1,:]/dfMassNorminal[1,0]
dfMassTight[1,:] = dfMassTight[1,:]/dfMassTight[1,0]
dfMassWide[1,:] = dfMassWide[1,:]/dfMassWide[1,0]

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
plt.plot(dfMassTight[0], dfMassTight[1], '--', marker='^', markerfacecolor='none', markevery=30, color=colors[0], linewidth=1.0)
plt.plot(dfMassWide[0], dfMassWide[1], '-.', marker='v', markerfacecolor='none', markevery=30, color=colors[1], linewidth=1.0)
plt.xlabel('Time (s)', fontname='Times New Roman', fontsize=fsize)
plt.ylabel(r'Normalized Mass', fontname='Times New Roman', fontsize=fsize)
leg = ('Virtual', 'Tight', 'Wide')
H = plt.legend(leg, loc='upper right', prop={'size': 16}, numpoints=1,
               frameon=False)
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
plt.axis([0, 1000, 0.70, 1.05])
# Save figures
plt.tight_layout()
plt.savefig('E_Glass_Old_Linear_Mass_Comparison.png', dpi=300)
plt.show()
plt.close()

# %%
# Zoom in
low = 500
high = 700
fig1 = plt.figure(figsize=(fwidth, fheight))
plt.plot(dfMassNorminal[0][low:high], dfMassNorminal[1][low:high], '-k', marker='o', markerfacecolor='none', markevery=30, markersize=15, markeredgewidth=2, linewidth=2.0)
plt.plot(dfMassTight[0][low:high], dfMassTight[1][low:high], '--', marker='^', markerfacecolor='none', markevery=30, color=colors[0], markersize=15, markeredgewidth=2, linewidth=2.0)
plt.plot(dfMassWide[0][low:high], dfMassWide[1][low:high], '-.', marker='v', markerfacecolor='none', markevery=30, color=colors[1], markersize=15, markeredgewidth=2, linewidth=2.0)
# plt.xlabel('Time (s)', fontname='Times New Roman', fontsize=fsize)
# plt.ylabel(r'Normalized Mass', fontname='Times New Roman', fontsize=fsize)
# leg = ('Virtual', 'Tight', 'Full')
# H = plt.legend(leg, loc='upper right', prop={'size': 16}, numpoints=1,
               # frameon=False)
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
plt.tick_params(axis=u'both', which=u'both',length=0,colors='w')
plt.axis([low, high, 0.75, 0.90])
# Save figures
plt.tight_layout()
plt.savefig('E_Glass_Old_Linear_Mass_Comparison_ZoomIn.png', dpi=300)
plt.show()
plt.close()
