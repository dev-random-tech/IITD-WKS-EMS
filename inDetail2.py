import numpy as np
import pandas as pd
from operator import not_

stateTags_df = pd.read_csv('stateNodes.csv')
varNames = stateTags_df.iloc[:,0].values
varNames = np.asarray(varNames)
rightVals = list(stateTags_df.iloc[:,1].values)

def mul(a,b): #Returns 1 if both values are same
    if a == b:
        return 1
    else:
        return 0

def reasons(tags):
    out = list(map(mul,tags,rightVals))
    faults = list(map(bool,out))
    faults = list(map(not_,faults))
    print('Reasons for fault:',varNames[faults])
