#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#==========================================
# Title :   1D-LBP Python Implementation
# Author:   pranabendra
# Date  :   11 Feb 2019
#==========================================
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import LBP_generator
import sys

filename, window_size = sys.argv[1], int(sys.argv[2])

arr = pd.read_excel(filename, header=None)
arr = arr.values

master_lbp_all = []
master_lbp_uniform = []

for x in arr:
    mat = []
    
    for i in range((window_size - 1)//2 , len(x) - (window_size - 1)//2):
        a = x[i - (window_size - 1)//2 : i]
        b = x[i+1 : i + (window_size + 1)//2]
        a = np.concatenate((a,b))
        bit_char = ['1' if k >= x[i] else '0' for k in a]
        bit_str = ''.join(bit_char)
        mat.append(int(bit_str, 2))
        m = []
    
    for i in range(pow(2,window_size - 1)):
        m.append(mat.count(i))
    
    no_of_features, ref = LBP_generator.generate(window_size - 1)
    
    lut = {}
    for i in range(len(ref)):
        lut[ref[i]] = i+1
        
        lbp_uniform = [0]*(len(ref) + 2)

    for i in range(len(mat)):
        try:
            dummy = lut[mat[i]]
        except KeyError:
            lbp_uniform[len(ref) + 1] += 1
        else:
            lbp_uniform[dummy] += 1
    
    lbp_uniform = lbp_uniform[1:]
    master_lbp_all += [mat]
    master_lbp_uniform += [lbp_uniform]
    
y1 = np.array(master_lbp_all)
y2 = np.array(master_lbp_uniform)

y1 = y1.reshape(arr.shape[0],len(x) - window_size + 1)
y2 = y2.reshape(arr.shape[0],len(ref) + 1)

df1 = pd.DataFrame(y1)
filepath = filename[:filename.index('.')] + '_LBP_all_' + str(window_size) + filename[filename.index('.'):]
df1.to_excel(filepath, header=False, index=False)

df2 = pd.DataFrame(y2)
filepath = filename[:filename.index('.')] + '_LBP_uniform_' + str(window_size) + filename[filename.index('.'):]
df2.to_excel(filepath, header=False,index=False)
