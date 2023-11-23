#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 18:42:51 2018

@author: christian
"""

with open('input20.txt','r') as file:
    input = file.read()

dir = {'N': 1j, 'S': -1j, 'E': 1, 'W': -1}

def traverse(it, map={0: 0}, pos=0, depth=0):
    initial_pos = pos
    initial_depth = depth
    
    for c in it:
        if c in dir:
            pos += dir[c]
            if pos in map:  # been here before, so we are backtracking
                depth = map[pos]
            else:
                depth += 1
                map[pos] = depth
        elif c == '|':
            pos = initial_pos
            depth = initial_depth
        elif c == '(':
            traverse(it, map, pos, depth)
        elif c == ')':
            return
        elif c == '$':
            return map
        else:
            print(f'Unknown character: {c}')


map = traverse(iter(input[1:]))
print(max(map.values()))
print(sum([1 for x in map.values() if x >= 1000]))