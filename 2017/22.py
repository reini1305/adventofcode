#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 09:02:21 2017

@author: reini
"""
import numpy as np

m = np.zeros([1000,1000])

direction = {0: np.array([0,1]),
             1: np.array([-1,0]),
             2: np.array([0,-1]),
             3: np.array([1,0])}



offset = 500

with open('input22.txt') as infile:
    for y,line in enumerate(infile):
        for x,char in enumerate(line):
            if char == '#':
                m[offset + y][offset + x] = 1
                
curr_dir = 2
curr_pos = offset + np.array([x/2,y/2])
bursts = 0

for i in range(10000):
    if m[int(curr_pos[1])][int(curr_pos[0])] == 1:
        curr_dir = (curr_dir + 1) % 4
        m[int(curr_pos[1])][int(curr_pos[0])] = 0
    else:
        curr_dir = (curr_dir - 1) % 4
        m[int(curr_pos[1])][int(curr_pos[0])] = 1
        bursts += 1
    curr_pos += direction[curr_dir]
    
print(bursts)

# part 2
# 0:clean, 1: weakend, 2: flagged, 3: infected
m = np.zeros([10000,10000])
offset = 5000
with open('input22.txt') as infile:
    for y,line in enumerate(infile):
        for x,char in enumerate(line):
            if char == '#':
                m[offset + y][offset + x] = 3

def part2():
    curr_dir = 2
    curr_pos = offset + np.array([x/2,y/2])
    bursts = 0
    
    for i in range(10000000):
        if m[int(curr_pos[1])][int(curr_pos[0])] == 3: # infected
            curr_dir = (curr_dir + 1) % 4
            m[int(curr_pos[1])][int(curr_pos[0])] = 2
        elif m[int(curr_pos[1])][int(curr_pos[0])] == 0: # clean
            curr_dir = (curr_dir - 1) % 4
            m[int(curr_pos[1])][int(curr_pos[0])] = 1
        elif m[int(curr_pos[1])][int(curr_pos[0])] == 1: #weakend
            m[int(curr_pos[1])][int(curr_pos[0])] = 3
            bursts += 1
        else: # flagged
            curr_dir = (curr_dir + 2) % 4
            m[int(curr_pos[1])][int(curr_pos[0])] = 0
        curr_pos += direction[curr_dir]
    print(bursts)
    
part2()
