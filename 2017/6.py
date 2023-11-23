#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 07:23:15 2017

@author: reini
"""
import numpy as np

input = '5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6'
input = [int(token) for token in input.split()]

combinations = dict()

memory = input
counter = 0
while not ''.join(str(memory)) in combinations:
    combinations[''.join(str(memory))] = counter
    # find maximum
    index = np.argmax(memory)   
    # find out how many to distribute
    per_bucket = np.maximum(1,memory[index]/len(memory))  
    new_index = (index+1)%len(memory)
    while(memory[index]>=per_bucket):
        memory[index]-=per_bucket
        memory[new_index]+=per_bucket
        new_index = (new_index+1)%len(memory)
    # Now there might be some left for the last bucket
    while(memory[index]>0):
        memory[index]-=1
        memory[new_index]+=1
        new_index = (new_index+1)%len(memory)
    counter += 1

print (counter)
print (counter-combinations[''.join(str(memory))])