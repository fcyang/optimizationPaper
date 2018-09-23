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
def readSolution(dir, nameList, reac):
    solutionName = []
    solution = []
    colList = [x for x in range(reac+1)]
    for idx,x in enumerate(nameList):
        print('Reading solution: ' + dir + x + '_solution.txt')
        solutionName.append(glob.glob(dir + x + '_solution.txt')[0])
        solTmp = pd.read_csv(solutionName[idx], sep='=|,', engine='python', index_col=0, header=None)
        # solTmp.columns = colList
        if reac>1:
            solTmp = solTmp.iloc[:,0:reac]
        else:
            solTmp = solTmp.iloc[:,0:2]
        solTmp.index = [y[:-2] for y in solTmp.index]
        solution.append(solTmp)
    return solutionName, solution

def generateVal(dir, solList, codeDir, sol, heatFluxList, reac):
    newFileList = []
    for idx1,i in enumerate(sol):
        with open(dir+'Template.yaml') as f:
            doc = yaml.load(f)
        docName = doc['name']
        # change kinetic parameters for 1 reaction
        for k in range(reac):
            doc['reactionParams']['A'][k][0] = sol[idx1].loc['A',k]
            doc['reactionParams']['E'][k][0] = sol[idx1].loc['E',k]
            doc['reactionParams']['n'][k][0] = sol[idx1].loc['n',k]
            doc['reactionParams']['Hp'][k][0] = sol[idx1].loc['Hp',k]
            doc['reactionParams']['Xi'][k][0] = sol[idx1].loc['Xi',k]
        # change material properties
        doc['phaseParams']['ka'][0][0] = sol[idx1].loc['ka',0]
        doc['phaseParams']['ka'][1][0] = sol[idx1].loc['ka',1]
        doc['phaseParams']['kb'][0][0] = sol[idx1].loc['kb',0]
        doc['phaseParams']['kb'][1][0] = sol[idx1].loc['kb',1]
        doc['phaseParams']['Cpa'][0][0] = sol[idx1].loc['Cpa',0]
        doc['phaseParams']['Cpa'][1][0] = sol[idx1].loc['Cpa',1]
        doc['phaseParams']['Cpb'][0][0] = sol[idx1].loc['Cpb',0]
        doc['phaseParams']['Cpb'][1][0] = sol[idx1].loc['Cpb',1]
        doc['phaseParams']['K'][0][0] = sol[idx1].loc['K',0]
        doc['phaseParams']['eps'][0][0] = sol[idx1].loc['eps',0]

        for idx2,j in enumerate(heatFluxList):
            # change case name
            doc['name'] = docName+solList[idx1]+j+'kW'
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
                                    # run validation cases
                    print('Running validation case '+valFileName)
                    call(['python', codeDir, valFileName])
                    newFileList.append(doc)
                else:
                    break
            else:
                # write to yaml file
                with open(valFileName, "w") as f:
                    yaml.dump(doc, f, default_flow_style=False)
                # run validation cases
                print('Running validation case '+valFileName)
                call(['python', codeDir, valFileName])
                newFileList.append(doc)
    return newFileList

# %%
def main(argv=None):
    if argv is None:
        argv = sys.argv
    print(argv)
    # run script
    preFileName = 'charLinear1Reac'
    solDir = 'C:/Users/Fyang/Workspace/optimization/optimizationPaper/results/multiReactionCharring/1Reactions/solutions/'
    solList = ['1Mass', 'FTBT', 'BT', 'TGABT', 'TGABTRun2', 'TGABTRun1', 'TGADSC', 'TGA', '2Mass', '2MassTGA', '3Mass']
    heatFluxList = ['10', '60', '100']
    reac = 1
    name, sol = readSolution(solDir+preFileName, solList, reac)

    confDir = 'C:/Users/Fyang/Workspace/optimization/optimizationPaper/config/multiReactionCharring/1Reactions/validation/'
    codeDir = 'C:/Users/Fyang/Workspace/optimization/sourceCode/optimizationPython/src/main.py'
    tempFileName = confDir + preFileName
    fileList = generateVal(tempFileName, solList, codeDir, sol, heatFluxList, reac)
    with open('validationCase.log', 'w') as f:
        for x in fileList:
            f.write('%s\n\n' % x)

if __name__=='__main__':
    main()
