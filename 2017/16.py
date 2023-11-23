#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 07:16:55 2017

@author: reini
"""
from string import ascii_lowercase

input = list()

with open('input16.txt') as infile:
    for line in infile:
        input.extend(line.split(','))

positions = [c for c in ascii_lowercase]
positions = positions[:16]

def run_program(input,positions):
    for instruction in input:
        if instruction[0] == 's':
            num = int(instruction[1:])
            positions = positions[-num:] + positions[:len(positions)-num]
        elif instruction[0] == 'x':
            ab = [int(t) for t in instruction[1:].split('/')]
            t = positions[ab[0]]
            positions[ab[0]] = positions[ab[1]]
            positions[ab[1]] = t
        elif instruction[0] == 'p':
            ab = [positions.index(t) for t in instruction[1:].split('/')]
            t = positions[ab[0]]
            positions[ab[0]] = positions[ab[1]]
            positions[ab[1]] = t
    return positions
        
r = run_program(input,positions)
print (''.join(r))

# task 2

r1 = ''.join(positions)  
r = positions

for i in range(200):
    r = run_program(input,r)
    if ''.join(r) == r1 and i>0:
        print (i)
        break

# Check remaining number of iterations
num_iter = 1000000000 % (i+1)

for i in range(num_iter):
    r = run_program(input,r)
    
print (''.join(r))