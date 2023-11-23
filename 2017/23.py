#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 09:30:48 2017

@author: reini
"""
import numpy as np

def interpret_line(tokens,cnt,registers,mul_count):
    if tokens[0] == 'set':
        try:
            op = int(tokens[2])
        except ValueError:
            op = registers[tokens[2]]
        registers[tokens[1]] = op
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
    if tokens[0] == 'mod':
        try:
            val = registers[tokens[2]]
        except KeyError:
            val = int(tokens[2])
        registers[tokens[1]] = registers[tokens[1]] % val
        cnt = cnt + 1
    if tokens[0] == 'mul':
        try:
            val = registers[tokens[2]]
        except KeyError:
            val = int(tokens[2])
        registers[tokens[1]] = registers[tokens[1]] * val
        mul_count += 1
        cnt = cnt + 1
    if tokens[0] == 'sub':
        try:
            val = registers[tokens[2]]
        except KeyError:
            val = int(tokens[2])
        registers[tokens[1]] = registers[tokens[1]] - val
        cnt = cnt + 1
    return cnt, mul_count


def interpret_assembunny(instructions,registers):
    cnt = 0
    mul_count = 0
    while cnt >= 0 and cnt<len(instructions):
        tokens = instructions[cnt]
        cnt,mul_count = interpret_line(tokens,cnt,registers,mul_count)
    return mul_count

instructions = [line.strip().split(' ') for line in open('input23.txt')]
registers = {'a':0, 'b':0, 'c':0, 'd':0, 'e': 0, 'f':0,'g':0,'h':0}
print(interpret_assembunny(instructions,registers))

def countNonPrimes(b):
    count = 0
    start = (b * 100) + 100000
    to = start + 17000
    for n in np.arange(start,to+1,17):
        for d in np.arange(2,np.floor(np.sqrt(n))):
            if (n % d == 0):
                count += 1
                break
    return count

print(countNonPrimes(67))

