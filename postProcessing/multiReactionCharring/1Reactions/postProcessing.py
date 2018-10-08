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
fileName = 'data/charLinear1Reac'
figureName = 'charLinear1Reac'
massCol = ['# Time [s]',' Mass [Kg]']
tempCol = ['# Time [s]',' Temperature [C]']
dfMass = []
dfFT = []
dfBT = []
fileSeq = ['Nominal', '1Mass', '2Mass', '2MassTGA', '3Mass', 'FTBT', 'TGA', 'TGABTRun2', 'BT']
heatFlux = ['10kW', '60kW', '100kW']
# fileSeq = ['Nominal', 'TGADSC', '3Mass', 'TGA']
# heatFlux = ['10kW', '100kW']
legList = ['Virtual', '1Mass', '2Mass', '2Mass+TGA', '3Mass', '1Mass+FT+BT', '1Mass+TGA', '1Mass+TGA+BT', '1Mass+BT']
# legList = ['Virtual', 'M+TGA+DSC', '3 M', 'M+TGA']
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
        # for k in tempSeq:
        #     fileNameTmp = fileName + j + i + '_0_cone_' + k +'.csv'
        #     df = pd.read_csv(fileNameTmp, skiprows=0)
        #     dfTmp = df[tempCol]
        #     dfTmp = np.transpose(np.array(dfTmp))
        #     if k == 'FT':
        #         dfFT[idx].append(dfTmp)
        #     else:
        #         dfBT[idx].append(dfTmp)

# %%
# Data processing
# estimate standard error and store it in .csv file
err = []
for idx1, i in enumerate(heatFlux):
    err.append([])
    for idx2,j in enumerate(dfMass[idx1][1:]):
        errTmp = np.zeros(len(dfMass[idx1][0][0]))
        for idx3,k in enumerate(j[1]):
            errTmp[idx3] = np.abs(k - dfMass[idx1][0][1][idx3])
        errSum = np.mean(errTmp)
        err[idx1].append(errSum)
errData = pd.DataFrame(data=np.transpose(err), index=fileSeq[1:], columns=heatFlux)
errAch = np.transpose(err)
errData.to_csv('errorMassData.csv')

# err = []
# for idx1, i in enumerate(heatFlux):
#     err.append([])
#     for idx2,j in enumerate(dfFT[idx1][1:]):
#         errTmp = np.zeros(len(dfFT[idx1][0][0]))
#         for idx3,k in enumerate(j[1]):
#             errTmp[idx] = np.abs(k - dfFT[0][0][1][idx3])/dfFT[0][0][1][idx3]
#         errSum = np.sqrt(np.sum(errTmp)/(len(errTmp)+1))
#         err[idx1].append(errSum)
# errFTData = pd.DataFrame(data=np.transpose(err), index=fileSeq[1:], columns=heatFlux)
# errAch += np.transpose(err)
# errFTData.to_csv('errorFTData.csv')
#
# err = []
# for idx1, i in enumerate(heatFlux):
#     err.append([])
#     for idx2,j in enumerate(dfBT[idx1][1:]):
#         errTmp = np.zeros(len(dfBT[idx1][0][0]))
#         for idx3,k in enumerate(j[1]):
#             errTmp[idx] = np.abs(k - dfBT[0][0][1][idx3])/dfBT[0][0][1][idx3]
#         errSum = np.sqrt(np.sum(errTmp)/(len(errTmp)+1))
#         err[idx1].append(errSum)
# errBTData = pd.DataFrame(data=np.transpose(err), index=fileSeq[1:], columns=heatFlux)
# errAch += np.transpose(err)
# errBTData.to_csv('errorBTData.csv')
#
# errData = pd.DataFrame(data=errAch, index=fileSeq[1:], columns=heatFlux)
# errData.to_csv('errorData.csv')
################################################################################
# %%
# Custom greek font in label

# plt.rc('font', family='serif')
font = {'family' : 'Times New Roman',
        'weight' : 'normal'}
plt.rc('font', **font)
mpl.rcParams['mathtext.fontset'] = 'custom'
mpl.rcParams['mathtext.rm'] = 'Times New Roman'

# RGB color schemes from matlab
colors = [(0, 0.447, 0.7410), (0.8500, 0.3250, 0.0980),
          (0.9290, 0.6940, 0.1250)]

# Figure parameters
fsize = 20
hsize = 16
fwidth = 6.5
fwidthlong = 6.5+2.1
fheight = 5
markStep = [200, 20]
markerList = ['o', '^', 'v', 's', '<', '>', '*', 'p', 'h', 'x', '+']
markerSize = 8
axisList = [6000, 400]

# %%
# cherry-picked figure plots for publication
heatFluxIdx = 0
markStepIdx = 0
fig = plt.figure(figsize=(fwidth, fheight))
for i in range(len(legList[1:])):
    plt.plot(dfMass[heatFluxIdx][i+1][0], dfMass[heatFluxIdx][i+1][1], '-', marker=markerList[i], markerfacecolor='none', markevery=markStep[markStepIdx],markersize=markerSize, linewidth=1, label=legList[i+1])
plt.plot(dfMass[heatFluxIdx][0][0], dfMass[heatFluxIdx][0][1], '-k', markerfacecolor='none', markevery=markStep[markStepIdx], linewidth=3, label=legList[0])
plt.xlabel('Time (s)', fontname='Times New Roman', fontsize=fsize)
plt.ylabel(r'Normalized Mass', fontname='Times New Roman', fontsize=fsize)
# H = plt.legend(loc='lower left', prop={'size': 16}, numpoints=1,
#                             frameon=False, bbox_to_anchor=(1,0.12))
plt.axis([0, 6000, 0.7, 1.05])
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
# save figures
plt.tight_layout()
plt.savefig(figureName + '10kW' + 'NormalizedMass' +'.png', dpi=300)
plt.show()

# %%
heatFluxIdx = 2
markStepIdx = 1
fig = plt.figure(figsize=(fwidth, fheight))
for i in range(len(legList[1:])):
    plt.plot(dfMass[heatFluxIdx][i+1][0], dfMass[heatFluxIdx][i+1][1], '-', marker=markerList[i], markerfacecolor='none', markevery=markStep[markStepIdx],markersize=16, linewidth=1, label=legList[i+1])
plt.plot(dfMass[heatFluxIdx][0][0], dfMass[heatFluxIdx][0][1], '-k', markerfacecolor='none', markevery=markStep[markStepIdx], linewidth=3, label=legList[0])
plt.axis([150, 350, 0.72, 0.8])
plt.tick_params(axis='x',which='both',bottom=False,left=False,top=False,labelbottom=False,labelleft=False)
plt.tick_params(axis='y',which='both',bottom=False,left=False,top=False,labelbottom=False,labelleft=False)
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
# save figures
plt.tight_layout()
plt.savefig(figureName + '100kW' + 'NormalizedMass' +'1.png', dpi=300)
plt.show()

# %%
heatFluxIdx = 2
markStepIdx = 1
fig = plt.figure(figsize=(fwidthlong, fheight))
for i in range(len(legList[1:])):
    plt.plot(dfMass[heatFluxIdx][i+1][0], dfMass[heatFluxIdx][i+1][1], '-', marker=markerList[i], markerfacecolor='none', markevery=markStep[markStepIdx],markersize=markerSize, linewidth=1, label=legList[i+1])
plt.plot(dfMass[heatFluxIdx][0][0], dfMass[heatFluxIdx][0][1], '-k', markerfacecolor='none', markevery=markStep[markStepIdx], linewidth=3, label=legList[0])
plt.xlabel('Time (s)', fontname='Times New Roman', fontsize=fsize)
plt.ylabel(r'Normalized Mass', fontname='Times New Roman', fontsize=fsize)
H = plt.legend(loc='lower left', prop={'size': 16}, numpoints=1,
                            frameon=False, bbox_to_anchor=(1,0.12))
plt.axis([0, 500, 0.7, 1.05])
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
# save figures
plt.tight_layout()
plt.savefig(figureName + '100kW' + 'NormalizedMass' +'2.png', dpi=300)
plt.show()


# # %%
# # auto figures generation -- for large batch of figures
# for idx1,i in enumerate(heatFlux):
#     for j in ['Mass', 'Temp']:
#         fig = plt.figure(figsize=(fwidth, fheight))
#         if j == 'Mass':
#             for idx2,k in enumerate(dfMass[idx1]):
#                 if idx2 == 0:
#                     plt.plot(k[0], k[1], '-k', marker=markerList[idx2], markerfacecolor='none', markevery=markStep[idx1], linewidth=1.5, label=legList[idx2])
#                 else:
#                     plt.plot(k[0], k[1], '-', marker=markerList[idx2], markerfacecolor='none', markevery=markStep[idx1], color=colors[idx2-1], linewidth=1.5, label=legList[idx2])
#             plt.xlabel('Time (s)', fontname='Times New Roman', fontsize=fsize)
#             plt.ylabel(r'Normalized Mass', fontname='Times New Roman', fontsize=fsize)
#             H = plt.legend(loc='upper right', prop={'size': 16}, numpoints=1,
#                            frameon=False)
#             plt.rc('xtick', labelsize=16)
#             plt.rc('ytick', labelsize=16)
#             plt.axis([0, axisList[idx1], 0.3, 1.05])
#             # save figures
#             plt.tight_layout()
#             plt.savefig(figureName + i + j +'.png', dpi=300)
#             plt.show()
#         if j == 'Temp':
#             for idx2, (p,q) in enumerate(zip(dfFT[idx1], dfBT[idx1])):
#
#                 if idx2 == 0:
#                     plt.plot(p[0], p[1], '-k', marker=markerList[idx2], markerfacecolor='none', markevery=markStep[idx1], linewidth=1.5, label=legList[idx2])
#                     plt.plot(q[0], q[1], '--k', marker=markerList[idx2], markerfacecolor='none', markevery=markStep[idx1], linewidth=1.5)
#                 else:
#                     plt.plot(p[0], p[1], '-', marker=markerList[idx2], markerfacecolor='none', markevery=markStep[idx1], color=colors[idx2-1], linewidth=1.5, label=legList[idx2])
#                     plt.plot(q[0], q[1], '--', marker=markerList[idx2], markerfacecolor='none', markevery=markStep[idx1], color=colors[idx2-1], linewidth=1.5)
#             plt.xlabel('Time (s)', fontname='Times New Roman', fontsize=fsize)
#             plt.ylabel(r'Temperature ($^o$C)', fontname='Times New Roman', fontsize=fsize)
#             H = plt.legend(loc='lower right', prop={'size': 16}, numpoints=1,
#                            frameon=False)
#             plt.rc('xtick', labelsize=16)
#             plt.rc('ytick', labelsize=16)
#             plt.axis([0, axisList[idx1], 25, max(p[1])+50])
#             # save figures
#             plt.tight_layout()
#             plt.savefig(figureName + i + j +'.png', dpi=300)
#             plt.show()
