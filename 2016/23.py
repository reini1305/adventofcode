#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 07:54:07 2016

@author: christian
"""

def toggle(instruction):
    tokens = instruction.split(' ')
    if tokens[0] == 'inc':
        tokens[0] = 'dec'
    elif tokens[0] == 'dec' or tokens[0] == 'tgl':
        tokens[0] = 'inc'
    elif tokens[0] == 'jnz':
        tokens[0] = 'cpy'
    elif tokens[0] == 'cpy' or tokens[0] == 'add' or tokens[0] == 'mul':
        tokens[0] = 'jnz'    
    new_instruction = ' '.join(tokens)
    return new_instruction

f = open('input_23.txt')

instructions = list(i for i in iter(f))
cnt = 0
registers = {'a':12,'b':0,'c':0,'d':0}

while cnt<len(instructions):
    curr_instruction = instructions[cnt]
    curr_instruction = curr_instruction.replace('\n','')
    tokens = curr_instruction.split(' ')
    if tokens[0] == 'cpy':
        try:
            op = int(tokens[1])
        except ValueError:
            op = registers[tokens[1]]
        try:
            registers[tokens[2]] = op
        except KeyError:
            pass
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
        try:
            jmp = registers[tokens[2]]
        except KeyError:
            jmp = int(tokens[2])
        if reg != 0:
            cnt = cnt + jmp
        else:
            cnt = cnt + 1
    if tokens[0] == 'nop':
        cnt = cnt + 1
    if tokens[0] == 'mul':
        try:
            val = registers[tokens[1]]
        except KeyError:
            jmp = int(tokens[1])
        registers[tokens[2]] = registers[tokens[2]] * val
        cnt = cnt + 1
    if tokens[0] == 'add':
        try:
            val = registers[tokens[1]]
        except KeyError:
            jmp = int(tokens[1])
        registers[tokens[2]] = registers[tokens[2]] + val
        cnt = cnt + 1
    if tokens[0] == 'tgl':
        try:
            reg = registers[tokens[1]]
        except KeyError:
            reg = int(tokens[1])
        cnt_to_toggle = cnt + reg
        if cnt_to_toggle < len(instructions):
            instructions[cnt_to_toggle] = toggle(instructions[cnt_to_toggle])
        cnt = cnt + 1