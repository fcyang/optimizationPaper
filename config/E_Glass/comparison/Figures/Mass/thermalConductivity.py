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


# %%
# Data processing
# Normalizing mass
kvaNorm = 0.312
kvbNorm = 4.41e-5
kvaHydr = 0.27005
kvbHydr = 0.000169
kcaNorm = 0.0949
kcbNorm = 2.83e-4
kcaHydr = 0.2016
kcbHydr = 0.000180065

T = np.arange(273,800+273,1)
kvNorm = kvaNorm + T*kvbNorm
kvHydr = kvaHydr + T*kvbHydr
kcNorm = kcaNorm + T*kcbNorm
kcHydr = kcaHydr + T*kcbHydr

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
plt.plot(T, kvNorm, '-b') #marker='o', markerfacecolor='none', markevery=90, linewidth=1.0)
plt.plot(T, kvHydr, '--b')
plt.plot(T, kcNorm, '-r')
plt.plot(T, kcHydr, '--r')
plt.xlabel('Temperature (K)', fontname='Times New Roman', fontsize=fsize)
plt.ylabel(r'Thermal Conductivity (W/m/K)', fontname='Times New Roman', fontsize=fsize)
leg = ('Virtual', 'Hybrid')
H = plt.legend(leg, loc='upper left', prop={'size': 16}, numpoints=1,
               frameon=False)
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
plt.axis([273, 800+273, 0.1, 0.5])
# Save figures
plt.tight_layout()
plt.savefig('thermalConductivity.png', dpi=300)
plt.show()
plt.close()
