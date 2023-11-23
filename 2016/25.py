#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 07:54:07 2016

@author: christian
"""
import sys

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


def interpret_assembunny(instructions,registers):
    cnt = 0
    curr_out = 1
    while cnt<len(instructions):
        print cnt
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
            if tokens[0] == 'out':
                try:
                    reg = registers[tokens[1]]
                except KeyError:
                    reg = int(tokens[1])
                sys.stdout.write(str(reg))
                sys.stdout.flush()
                if reg == curr_out or (reg != 0 and reg != 1):
                    return False
                else:
                    curr_out = reg
                
                cnt = cnt + 1

#for a in range(10000):
#    registers = {'a':a,'b':0,'c':0,'d':0}
#    if interpret_assembunny(instructions,registers) == False:
#        sys.stdout.write('\n')
#        print a

target = 2532
def day25a():
    n = 1
    while n < target:
        if n % 2 == 0:
            n = n * 2 + 1
        else:
            n *= 2
    return n - target