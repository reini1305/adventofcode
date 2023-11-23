#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 07:48:25 2017

@author: reini
"""
#from numba import jit

input = 345

buffer = list()

buffer.append(0)
curr_pos = 0

for i in range(2017):
    curr_pos = (curr_pos + input + 1) % len(buffer)
    buffer.insert(curr_pos,i+1)

print(buffer[buffer.index(2017)+1])


#@jit
def task2():
    answer = 0
    curr_pos = 0
    for i in range(50000000):
        curr_pos = (curr_pos + input + 1) % (i+1)
        if curr_pos == 0:
            answer = i+1
    return answer
        
print(task2())
