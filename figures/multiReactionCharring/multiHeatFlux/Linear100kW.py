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
fileName = 'multiReacCharLinearNominal100KW_0_cone_Mass.csv'
df = pd.read_csv(fileName, skiprows=0)
dfMassNorminal = df[['# Time [s]',' Mass [Kg]']]  # select time and MLR for 1D plot
dfMassNorminal = np.transpose(np.array(dfMassNorminal))

fileName = 'multiReacCharLinearWide100KW_0_cone_Mass.csv'
df = pd.read_csv(fileName, skiprows=0)
dfMassWide = df[['# Time [s]',' Mass [Kg]']]  # select time and MLR for 1D plot
dfMassWide = np.transpose(np.array(dfMassWide))

fileName = 'multiReacCharLinearHybrid100KW_0_cone_Mass.csv'
df = pd.read_csv(fileName, skiprows=0)
dfMassHybrid = df[['# Time [s]',' Mass [Kg]']]  # select time and MLR for 1D plot
dfMassHybrid = np.transpose(np.array(dfMassHybrid))

fileName = 'multiReacCharLinearNominal100KW_0_cone_FT.csv'
df = pd.read_csv(fileName, skiprows=0)
dfFTNorminal = df[['# Time [s]',' Temperature [C]']]  # select time and MLR for 1D plot
dfFTNorminal = np.transpose(np.array(dfFTNorminal))

fileName = 'multiReacCharLinearWide100KW_0_cone_FT.csv'
df = pd.read_csv(fileName, skiprows=0)
dfFTWide = df[['# Time [s]',' Temperature [C]']]  # select time and MLR for 1D plot
dfFTWide = np.transpose(np.array(dfFTWide))

fileName = 'multiReacCharLinearHybrid100KW_0_cone_FT.csv'
df = pd.read_csv(fileName, skiprows=0)
dfFTHybrid = df[['# Time [s]',' Temperature [C]']]  # select time and MLR for 1D plot
dfFTHybrid = np.transpose(np.array(dfFTHybrid))

# %%
# Data processing
# Normalizing Mass

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
markStep = 20

# %%
# Figure #2
fig1 = plt.figure(figsize=(fwidth, fheight))
plt.plot(dfMassNorminal[0], dfMassNorminal[1], '-k', marker='o', markerfacecolor='none', markevery=markStep, linewidth=1.5)
plt.plot(dfMassHybrid[0], dfMassHybrid[1], '-', marker='^', markerfacecolor='none', markevery=markStep, color=colors[0], linewidth=1.5)
plt.plot(dfMassWide[0], dfMassWide[1], '-', marker='v', markerfacecolor='none', markevery=markStep, color=colors[1], linewidth=1.5)
plt.xlabel('Time (s)', fontname='Times New Roman', fontsize=fsize)
plt.ylabel(r'Normalized Mass', fontname='Times New Roman', fontsize=fsize)
leg = ('Virtual', 'Hybrid', 'Full')
H = plt.legend(leg, loc='upper right', prop={'size': 16}, numpoints=1,
               frameon=False)
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
plt.axis([0, 200, 0.5, 1.05])
# Save figures
plt.tight_layout()
plt.savefig('multi_Reaction_Linear_100KW_Mass_Comparison.png', dpi=300)
plt.show()

# Figure #2
fig1 = plt.figure(figsize=(fwidth, fheight))
plt.plot(dfFTNorminal[0], dfFTNorminal[1], '-k', marker='o', markerfacecolor='none', markevery=markStep, linewidth=1.5)
plt.plot(dfFTHybrid[0], dfFTHybrid[1], '-', marker='^', markerfacecolor='none', markevery=markStep, color=colors[0], linewidth=1.5)
plt.plot(dfFTWide[0], dfFTWide[1], '-', marker='v', markerfacecolor='none', markevery=markStep, color=colors[1], linewidth=1.5)
plt.xlabel('Time (s)', fontname='Times New Roman', fontsize=fsize)
plt.ylabel(r'Temperature ($^o$C)', fontname='Times New Roman', fontsize=fsize)
leg = ('Virtual', 'Hybrid', 'Full')
H = plt.legend(leg, loc='lower right', prop={'size': 16}, numpoints=1,
               frameon=False)
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
plt.axis([0, 1200, 20, 910])
# Save figures
plt.tight_layout()
plt.savefig('multi_Reaction_Linear_100KW_Temp_Comparison.png', dpi=300)
plt.show()
plt.close()
