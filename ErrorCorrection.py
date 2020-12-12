import datetime
import time
import numpy as np
import pandas as pd
from operator import and_
from operator import not_
import inDetail2 as detailed
ct_df = pd.read_csv('correct_tags.csv')

correct_tags = ct_df.loc[:,"powerStatus":"exit1"].values
temp = np.asarray(ct_df.columns)
tag_names = np.delete(temp,0)


def all_check(tag_list):
    return sum(tag_list)

def mul(a,b): #Returns 1 if both values are same
    if a == b:
        return 1
    else:
        return 0

'''
def mat_mul(mat1,mat2):
    row1,col1 = mat1.shape
    row2,col2 = mat2.shape
    op_mat = np.zeros((row1,col2))

    if (col1 == row2):
        for i in range(row1):
            for j in range(col2):
                op_mat[i][j] = sum(list(map(mul,mat1[i,:],mat2[:,j])))

    return op_mat
'''

def faults(tags,time_val,moreTags):
    op = list(map(mul,tags,list(correct_tags[time_val,:])))
    if all_check(op) != len(tags):
        faults = list(map(bool,op)) 
        faults = list(map(not_,faults))
        print('Faults at:',tag_names[faults])    
        detailed.reasons(moreTags)
