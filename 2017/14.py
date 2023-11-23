#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 16:52:06 2017

@author: reini
"""
from functools import reduce

# Calc knot hash
def calcHash(input):
    lengths = [ord(token) for token in input]
    lengths.extend([17, 31, 73, 47, 23])
    #lengths = [3, 4, 1, 5, 17, 31, 73, 47, 23]
    
    cur_pos = 0
    skip = 0
    memory = list(range(256))
    for round in range(64):
        for length in lengths:
            # Select start and end point
            if cur_pos + length  >= len(memory):
                ranges = [(cur_pos,len(memory)),(0,cur_pos + length - len(memory))]
                new_pos = (cur_pos + length - len(memory) + skip) % (len(memory) )
            else:
                ranges = [(cur_pos, cur_pos + length)]
                new_pos = (cur_pos + length + skip) % (len(memory) )
            skip = (skip + 1) % (len(memory))
            # Get reversed list
            reversedlist = list([item for item in reversed([item for start, end in ranges for item in memory[start:end]])])
            # Write back to memory
            if cur_pos + length  >= len(memory):
                memory[cur_pos:] = reversedlist[:len(memory)-cur_pos]
                memory[:cur_pos + length - len(memory)] = reversedlist[len(memory)-cur_pos:]
            else:
                memory[cur_pos:cur_pos+length] = reversedlist
            cur_pos = new_pos
    
    dense_hash = ''
    # Calculate dense hash
    for block in range(16):
        val = reduce(lambda xor,a:a^xor,memory[block*16:(block+1)*16],0)
        dense_hash += format(val,'02x')
    return dense_hash
    
input = 'ugkiagan'

# Task2

elements = {'0':[0,0,0,0],
            '1':[0,0,0,1],
            '2':[0,0,1,0],
            '3':[0,0,1,1],
            '4':[0,1,0,0],
            '5':[0,1,0,1],
            '6':[0,1,1,0],
            '7':[0,1,1,1],
            '8':[1,0,0,0],
            '9':[1,0,0,1],
            'a':[1,0,1,0],
            'b':[1,0,1,1],
            'c':[1,1,0,0],
            'd':[1,1,0,1],
            'e':[1,1,1,0],
            'f':[1,1,1,1]
        }

grid = list()

non_zero = 0
for row in range(128):
    hash = calcHash(input+'-'+str(row))
    gridrow = list()
    for c in hash:
        gridrow+=elements[c]
        non_zero+=sum(elements[c])
    grid.append(gridrow)
    
# start numbering with 2 (one is already used)
def find_region(dsk, ind_i, ind_j, reg):
    dsk[ind_i][ind_j] = reg    
    if ind_i > 0 and dsk[ind_i-1][ind_j] == 1:
        find_region(dsk, ind_i-1, ind_j, reg)
    if ind_i < 127 and dsk[ind_i+1][ind_j] == 1:
        find_region(dsk, ind_i+1, ind_j, reg)
    if ind_j > 0 and dsk[ind_i][ind_j-1] == 1:
        find_region(dsk, ind_i, ind_j-1, reg)
    if ind_j < 127 and dsk[ind_i][ind_j+1] == 1:
        find_region(dsk, ind_i, ind_j+1, reg)
        
regions = 0
for row in range(128):
    for col in range(128):
        if grid[row][col] == 1:
            regions += 1
            find_region(grid, row, col, regions + 1)
            
print (non_zero)
print (regions)