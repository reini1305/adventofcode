#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 07:32:19 2017

@author: reini
"""

states = dict()

# A
state = dict()
state['move'] = [1, -1]
state['write'] = [1, 0]
state['next'] = ['B', 'D']
states['A'] = state

# B
state = dict()
state['move'] = [1, 1]
state['write'] = [1, 0]
state['next'] = ['C', 'F']
states['B'] = state

# C
state = dict()
state['move'] = [-1, -1]
state['write'] = [1, 1]
state['next'] = ['C', 'A']
states['C'] = state

# D
state = dict()
state['move'] = [-1, 1]
state['write'] = [0, 1]
state['next'] = ['E', 'A']
states['D'] = state

# E
state = dict()
state['move'] = [-1, 1]
state['write'] = [1, 0]
state['next'] = ['A', 'B']
states['E'] = state

# F
state = dict()
state['move'] = [1, 1]
state['write'] = [0, 0]
state['next'] = ['C', 'E']
states['F'] = state

curr_state = 'A'
memory = [0]
curr_pos = 0

for iter in range(12302209):
    old_mem = memory[curr_pos]
    memory[curr_pos] = states[curr_state]['write'][old_mem]
    curr_pos +=        states[curr_state]['move'][old_mem]
    curr_state =       states[curr_state]['next'][old_mem]
    
    #make sure we don't run out of memory
    if curr_pos == len(memory):
        memory.append(0)
    elif curr_pos < 0:
        memory.insert(0,0)
        curr_pos = 0
        
    if iter % 1000000 == 0:
        print('.')
    
print(sum(memory)) 
    