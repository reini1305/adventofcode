#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 06:49:39 2018

@author: christian
"""

import numpy as np
from scipy import signal

serial = 4151

def getFuel(xy,serial):
    fuel = ((xy[0] + 10) * xy[1] + serial) * (xy[0] + 10)
    if fuel < 100:
        return -5
    else:
        return int(str(fuel)[-3])-5

grid = np.zeros((300,300))

for x in range(300):
    for y in range(300):
        grid[y][x] = getFuel((x,y),serial)
        
kernel = np.ones((3,3))

out = signal.convolve2d(grid,kernel,mode="valid")
max_where = np.where(out == np.max(out))
print(str(max_where[1][0]) + ',' + str(max_where[0][0]))

overall_max = 0
max_size = 0
smaller_counter = 0
for size in np.arange(3,301):
    kernel = np.ones((size,size))
    out = signal.convolve(grid,kernel,mode="valid")
    if np.max(out) >= overall_max:
        overall_max = np.max(out)
        max_where = np.where(out == np.max(out))
        max_size = size
    else:
        smaller_counter += 1
        if smaller_counter > 2:
            break
    
print(str(max_where[1][0]) + ',' + str(max_where[0][0]) + ',' + str(max_size))