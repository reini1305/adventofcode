#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 17:49:17 2016

@author: reini
"""

f = open('input_12.txt')

instructions = list(i for i in iter(f))
cnt = 0
registers = {'a':0,'b':0,'c':1,'d':0}

while cnt<len(instructions):
    curr_instruction = instructions[cnt]
    curr_instruction = curr_instruction.replace('\n','')
    tokens = curr_instruction.split(' ')
    if tokens[0] == 'cpy':
        try:
            op = int(tokens[1])
        except ValueError:
            op = registers[tokens[1]]
        registers[tokens[2]] = op
        cnt = cnt + 1
    if tokens[0] == 'inc':
        registers[tokens[1]] = registers[tokens[1]] + 1
        cnt = cnt + 1
    if tokens[0] == 'dec':
        registers[tokens[1]] = registers[tokens[1]] - 1   
        cnt = cnt + 1
    if tokens[0] == 'jnz':
        try:
            reg = registers[tokens[1]]
        except KeyError:
            reg = int(tokens[1])
        if reg != 0:
            cnt = cnt + int(tokens[2])
        else:
            cnt = cnt + 1
    