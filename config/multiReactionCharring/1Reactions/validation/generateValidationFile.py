################################################################################
'''
This python code is used to automatically transform solution.txt to validation
yaml file and run it. The functions can be reusable with small changes.
--Fengchang Yang
08/01/2018
'''
################################################################################

# %%
# import default modules
import numpy as np
import yaml
from collections import defaultdict
import os
import matplotlib.pyplot as plt
import sys
import glob
import pandas as pd
from subprocess import call

# %%
# import customized modules
# NA

# %%
# define functions
def readSolution(dir, nameList):
    solutionName = []
    solution = []
    for idx,x in enumerate(nameList):
        solutionName.append(glob.glob(dir + x + '_solution.txt')[0])
        print(dir + x + '.txt')
        solTmp = pd.read_csv(solutionName[idx], sep='=|,', engine='python', names=['virgin', 'char', 'none'])
        solTmp = solTmp.iloc[:,0:2]
        solTmp.index = [y[:-2] for y in solTmp.index]
        solution.append(solTmp)
    return solutionName, solution

def generateVal(dir, solList, codeDir, sol, heatFluxList):
    for idx1,i in enumerate(sol):
        for idx2,j in enumerate(heatFluxList):
            with open(dir+'Template.yaml') as f:
                doc = yaml.load(f)

            # change case name
            doc['name'] = doc['name']+solList[idx1]+j+'kW'
            # change kinetic parameters for 1 reaction
            doc['reactionParams']['A'][0][0] = sol[idx1].loc['A','virgin']
            doc['reactionParams']['E'][0][0] = sol[idx1].loc['E','virgin']
            doc['reactionParams']['n'][0][0] = sol[idx1].loc['n','virgin']
            doc['reactionParams']['Hp'][0][0] = sol[idx1].loc['Hp','virgin']
            # change material properties
            doc['phaseParams']['ka'][0][0] = sol[idx1].loc['ka','virgin']
            doc['phaseParams']['ka'][1][0] = sol[idx1].loc['ka','char']
            doc['phaseParams']['kb'][0][0] = sol[idx1].loc['kb','virgin']
            doc['phaseParams']['kb'][1][0] = sol[idx1].loc['kb','char']
            doc['phaseParams']['Cpa'][0][0] = sol[idx1].loc['Cpa','virgin']
            doc['phaseParams']['Cpa'][1][0] = sol[idx1].loc['Cpa','char']
            doc['phaseParams']['Cpb'][0][0] = sol[idx1].loc['Cpb','virgin']
            doc['phaseParams']['Cpb'][1][0] = sol[idx1].loc['Cpb','char']
            doc['phaseParams']['K'][0][0] = sol[idx1].loc['K','virgin']
            doc['phaseParams']['eps'][0][0] = sol[idx1].loc['eps','virgin']
            # change heat flux
            doc['cone1']['frontBoundaryConditions']['heatFlux'] = float(j)
            if j == '10':
                doc['cone1']['file'] = 'C:/Users/Fyang/Workspace/optimization/optimizationPaper/data/multiReactionCharring/multiReactionCharringFake1.csv'
            else:
                doc['cone1']['file'] = 'C:/Users/Fyang/Workspace/optimization/optimizationPaper/data/multiReactionCharring/multiReactionCharringFake.csv'

            valFileName = doc['name']+'.yaml'

            if os.path.isfile(valFileName):
                print('The file '+valFileName+' already exists.')
                flag = input('Do you want to replace it? Y/N:')
                if flag == 'Y':
                    # write to yaml file
                    with open(valFileName, "w") as f:
                        yaml.dump(doc, f, default_flow_style=False)
                else:
                    pass
            else:
                # write to yaml file
                with open(valFileName, "w") as f:
                    yaml.dump(doc, f, default_flow_style=False)

            # run validation cases
            print('Running validation case '+valFileName)
            call(['python', codeDir, valFileName])
            # resultsDir = 'C:/Users/Fyang/Workspace/optimization/optimizationPaper/results/multiReactionCharring/1Reactions/validation/'+valFileName[0:-5]+'_0_cone_Mass.csv'
            # dataDir = 'C:/Users/Fyang/Workspace/optimization/optimizationPaper/postProcessing/multiReactionCharring/1Reactions/data/'
            # call(['copy', resultsDir, dataDir], shell=True)

# %%
# run script
preFileName = 'charLinear1Reac'
solDir = 'C:/Users/Fyang/Workspace/optimization/optimizationPaper/results/multiReactionCharring/1Reactions/solution/'
solList = ['2MassTGA']
heatFluxList = ['10', '60', '100']
name, sol = readSolution(solDir+preFileName, solList)

confDir = 'C:/Users/Fyang/Workspace/optimization/optimizationPaper/config/multiReactionCharring/1Reactions/validation/'
codeDir = 'C:/Users/Fyang/Workspace/optimization/sourceCode/optimizationPython/src/main.py'
tempFileName = confDir + preFileName
generateVal(tempFileName, solList, codeDir, sol, heatFluxList)
