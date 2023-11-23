#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 06:25:34 2018

@author: christian
"""

import numpy as np

def countPlants(index,plants):
    count = 0
    for c,p in zip(index,plants):
        if p == '#':
            count += c
    return count

replacements = dict()
generations = 20
with open('input12.txt','r') as file:
    for i, line in enumerate(file):
        if i == 0:
            initial = line[15:].strip()
        elif i > 1:
            replacements[line[:5]] = line[9]
            
empty = ''.join(['.' for _ in range(generations * 2)])
plants = empty + initial + empty
for generation in range(generations):
    plants = '..' + plants + '..'
    new_plants = []
    for curr_index in np.arange(2,len(plants)-2):
        new_plants += replacements[plants[curr_index-2:curr_index+3]] if plants[curr_index-2:curr_index+3] in replacements else '.' 
    plants = ''.join(new_plants)

# Count
index = np.arange(-generations * 2,len(initial)+ 2*generations)
print(countPlants(index,plants))

generations = 500
index = np.arange(-generations * 2,len(initial)+ 2*generations)
empty = ''.join(['.' for _ in range(generations * 2)])
plants = empty + initial + empty
prev_count = 0
diff = 0
for generation in range(generations):
    plants = '..' + plants + '..'
    new_plants = []
    for curr_index in np.arange(2,len(plants)-2):
        new_plants += replacements[plants[curr_index-2:curr_index+3]] if plants[curr_index-2:curr_index+3] in replacements else '.' 
    plants = ''.join(new_plants)
    curr_count = countPlants(index,plants)
    if curr_count - prev_count == diff:
#        print('Generation: ' + str(generation) + ', Count: ' + str(curr_count) + ', Diff: ' + str(diff))
        print((50000000000-generation-1) * diff + curr_count)
        break
    diff = curr_count - prev_count
    prev_count = curr_count