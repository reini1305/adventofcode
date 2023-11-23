#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 08:34:08 2017

@author: reini
"""
from functools import reduce

lengths = '18,1,0,161,255,137,254,252,14,95,165,33,181,168,2,188'
lengths = [int(token) for token in lengths.split(',')]

memory = list(range(256))
cur_pos = 0
skip = 0

for length in lengths:
    # Select start and end point
    if cur_pos + length  >= len(memory):
        ranges = [(cur_pos,len(memory)),(0,cur_pos + length - len(memory))]
        new_pos = cur_pos + length - len(memory) + skip
    else:
        ranges = [(cur_pos, cur_pos + length)]
        new_pos = cur_pos + length + skip
    skip += 1
    # Get reversed list
    reversedlist = [item for item in reversed([item for start, end in ranges for item in memory[start:end]])]
    # Write back to memory
    if cur_pos + length  >= len(memory):
        memory[cur_pos:] = reversedlist[:len(memory)-cur_pos]
        memory[:cur_pos + length - len(memory)] = reversedlist[len(memory)-cur_pos:]
    else:
        memory[cur_pos:cur_pos+length] = reversedlist
    cur_pos = new_pos
    
print(memory[0]*memory[1])

# Part 2
input = '18,1,0,161,255,137,254,252,14,95,165,33,181,168,2,188'
#input = '1,2,3'
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
        reversedlist = [item for item in reversed([item for start, end in ranges for item in memory[start:end]])]
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
    
print (dense_hash)