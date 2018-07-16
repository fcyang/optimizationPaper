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
# file name components
fileName = 'data/charLinear3Reac'
figureName = 'charLinear3Reac'
massCol = ['# Time [s]',' Mass [Kg]']
tempCol = ['# Time [s]',' Temperature [C]']
dfMass = []
dfFT = []
dfBT = []
fileSeq = ['Nominal', 'TGADSC', '3Mass']
heatFlux = ['10kW', '100kW']
tempSeq = ['FT', 'BT']

# Read data from csv files
for idx, i in enumerate(heatFlux):
    dfMass.append([])
    dfFT.append([])
    dfBT.append([])
    for j in fileSeq:
        # read mass data
        fileNameTmp = fileName + j + i + '_0_cone_Mass.csv'
        df = pd.read_csv(fileNameTmp, skiprows=0)
        dfTmp = df[massCol]
        dfTmp = np.transpose(np.array(dfTmp))
        dfMass[idx].append(dfTmp)
        # read temperature data
        for k in tempSeq:
            fileNameTmp = fileName + j + i + '_0_cone_' + k +'.csv'
            df = pd.read_csv(fileNameTmp, skiprows=0)
            dfTmp = df[tempCol]
            dfTmp = np.transpose(np.array(dfTmp))
            if k == 'FT':
                dfFT[idx].append(dfTmp)
            else:
                dfBT[idx].append(dfTmp)

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
markStep = [200, 20]
markerList = ['o', '^', 'v', 's']
legList = ['Virtual', 'M+TGA+DSC', '3 M']
axisList = [6000, 400]

# %%
for idx1,i in enumerate(heatFlux):
    for j in ['Mass', 'Temp']:
        fig = plt.figure(figsize=(fwidth, fheight))
        if j == 'Mass':
            for idx2,k in enumerate(dfMass[idx1]):
                if idx2 == 0:
                    plt.plot(k[0], k[1], '-k', marker=markerList[idx2], markerfacecolor='none', markevery=markStep[idx1], linewidth=1.5)
                else:
                    plt.plot(k[0], k[1], '-', marker=markerList[idx2], markerfacecolor='none', markevery=markStep[idx1], color=colors[idx2-1], linewidth=1.5)
            plt.xlabel('Time (s)', fontname='Times New Roman', fontsize=fsize)
            plt.ylabel(r'Normalized Mass', fontname='Times New Roman', fontsize=fsize)
            leg = ('Virtual', 'M+TGA+DSC', '3 M')
            H = plt.legend(leg, loc='upper right', prop={'size': 16}, numpoints=1,
                           frameon=False)
            plt.rc('xtick', labelsize=16)
            plt.rc('ytick', labelsize=16)
            plt.axis([0, axisList[idx1], 0.3, 1.05])
            # save figures
            plt.tight_layout()
            plt.savefig(figureName + i + j +'.png', dpi=300)
            plt.show()
        if j == 'Temp':
            for idx2, (p,q) in enumerate(zip(dfFT[idx1], dfBT[idx1])):

                if idx2 == 0:
                    plt.plot(p[0], p[1], '-k', marker=markerList[idx2], markerfacecolor='none', markevery=markStep[idx1], linewidth=1.5, label=legList[idx2])
                    plt.plot(q[0], q[1], '--k', marker=markerList[idx2], markerfacecolor='none', markevery=markStep[idx1], linewidth=1.5)
                else:
                    plt.plot(p[0], p[1], '-', marker=markerList[idx2], markerfacecolor='none', markevery=markStep[idx1], color=colors[idx2-1], linewidth=1.5, label=legList[idx2])
                    plt.plot(q[0], q[1], '--', marker=markerList[idx2], markerfacecolor='none', markevery=markStep[idx1], color=colors[idx2-1], linewidth=1.5)
            plt.xlabel('Time (s)', fontname='Times New Roman', fontsize=fsize)
            plt.ylabel(r'Temperature ($^o$C)', fontname='Times New Roman', fontsize=fsize)
            H = plt.legend(loc='lower right', prop={'size': 16}, numpoints=1,
                           frameon=False)
            plt.rc('xtick', labelsize=16)
            plt.rc('ytick', labelsize=16)
            plt.axis([0, axisList[idx1], 25, max(p[1])+50])
            # save figures
            plt.tight_layout()
            plt.savefig(figureName + i + j +'.png', dpi=300)
            plt.show()
