#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 07:30:21 2017

@author: reini
"""

input = [int(line) for line in open('input5.txt')]
steps = 0
idx = 0
while idx < len(input):
    new_idx = idx + input[idx]
    input[idx] += 1
    idx = new_idx
    steps += 1
    
print (steps)

input = [int(line) for line in open('input5.txt')]
steps = 0
idx = 0
while idx < len(input):
    new_idx = idx + input[idx]
    if input[idx]>=3:
        input[idx] -= 1
    else:
        input[idx] += 1
    idx = new_idx
    steps += 1
    
print (steps)