#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 06:03:44 2018

@author: christian
"""
import numpy as np
from copy import deepcopy

with open('input18.txt','r') as file:
    field = [[x for x in line.strip()] for line in file]
    


def getNeighbors(field,x,y):
    neighbors = []
    neighbors.extend(field[y-1][x-1:x+2])
    neighbors.extend(field[y+1][x-1:x+2])
    neighbors.extend(field[y][x-1])
    neighbors.extend(field[y][x+1])
    return neighbors

def getNewField(field,neighbors):
    output = field
    if field == '.' and neighbors.count('|') >= 3:
        output = '|'
    elif field == '|' and neighbors.count('#') >= 3:
        output = '#'
    elif field == '#':
        if neighbors.count('#') >= 1 and neighbors.count('|') >=1:
            output = '#'
        else:
            output = '.'
    return output
    
# pad field
padded_field = []
padded_field.append([' ' for _ in range(len(field[0])+2)])
for line in field:
    line.insert(0,' ')
    line.append(' ')
    padded_field.append(line)
padded_field.append([' ' for _ in range(len(field[0])+2)])

for minutes in range(10):
    new_field = deepcopy(padded_field)
    for x in np.arange(1,len(padded_field)-1):
        for y in np.arange(1,len(padded_field[0])-1):
            new_field[y][x] = getNewField(padded_field[y][x],getNeighbors(padded_field,x,y))
    padded_field = deepcopy(new_field)

tree_count = 0
lumber_count = 0
for line in padded_field:
    tree_count += line.count('|')
    lumber_count += line.count('#')
                               
print(tree_count * lumber_count)

padded_field = []
padded_field.append([' ' for _ in range(len(field[0]))])
for line in field:
    padded_field.append(line)
padded_field.append([' ' for _ in range(len(field[0]))])

curr_resources = list()
for minutes in range(500):
    tree_count = 0
    lumber_count = 0
    new_field = deepcopy(padded_field)
    for y in np.arange(1,len(padded_field[0])-1):    
        for x in np.arange(1,len(padded_field)-1):
            new_field[y][x] = getNewField(padded_field[y][x],getNeighbors(padded_field,x,y))
        tree_count += padded_field[y].count('|')
        lumber_count += padded_field[y].count('#')
    curr_res = lumber_count * tree_count
    if curr_res in curr_resources:
        print('Found loop: ' + str(minutes) + '/' + str(curr_resources.index(curr_res)))
    curr_resources.append(curr_res)
    padded_field = deepcopy(new_field)
    
loop_start = 465
loop_end = 492
print(curr_resources[loop_start + ((1000000000-loop_end-1) % (loop_end-loop_start+1))])