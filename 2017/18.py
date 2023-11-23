#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 06:44:18 2017

@author: reini
"""
#from numba import jit
from collections import deque

instructions = [line for line in open('input18.txt')]

def interpret_line(tokens,cnt,sound,recovered,registers,stop=True):
    if tokens[0] == 'set':
        try:
            op = int(tokens[2])
        except ValueError:
            op = registers[tokens[2]]
        registers[tokens[1]] = op
        cnt = cnt + 1
    if tokens[0] == 'snd':
        sound = registers[tokens[1]]
        cnt = cnt + 1
    if tokens[0] == 'rcv':
        try:
            val = registers[tokens[1]]
        except KeyError:
            val = int(tokens[1])
        if val > 0:
            recovered = sound
            if stop:
                print(recovered)
                return -1, sound, recovered
        cnt = cnt + 1
    if tokens[0] == 'jgz':
        try:
            reg = registers[tokens[1]]
        except KeyError:
            reg = int(tokens[1])
        try:
            jmp = registers[tokens[2]]
        except KeyError:
            jmp = int(tokens[2])
        if reg > 0:
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
        cnt = cnt + 1
    if tokens[0] == 'add':
        try:
            val = registers[tokens[2]]
        except KeyError:
            val = int(tokens[2])
        registers[tokens[1]] = registers[tokens[1]] + val
        cnt = cnt + 1
    return cnt, sound, recovered


def interpret_assembunny(instructions,registers):
    cnt = 0
    sound = 0
    recovered = 0
    while cnt >= 0 and cnt<len(instructions):
        curr_instruction = instructions[cnt]
        curr_instruction = curr_instruction.replace('\n','')
        tokens = curr_instruction.split(' ')
        cnt, sound, recovered = interpret_line(tokens,cnt,sound,recovered,registers)

registers = {'a':0, 'b':0,  'i':0,'p':0,'f':0}

interpret_assembunny(instructions,registers)

def interpret_line_2(instructions,cnt,registers,myqueue,otherqueue):
    curr_instruction = instructions[cnt]
    curr_instruction = curr_instruction.replace('\n','')
    tokens = curr_instruction.split(' ')
    if tokens[0] == 'set':
        try:
            op = int(tokens[2])
        except ValueError:
            op = registers[tokens[2]]
        registers[tokens[1]] = op
        cnt = cnt + 1
    if tokens[0] == 'rcv':
        if len(myqueue)>0:
            registers[tokens[1]] = myqueue.popleft()
            registers['waiting'] = False
            cnt = cnt + 1
        else:
            registers['waiting'] = True
    if tokens[0] == 'snd':
        try:
            val = registers[tokens[1]]
        except KeyError:
            val = int(tokens[1])
        registers['sent'] += 1
        otherqueue.append(val)
        cnt = cnt + 1
    if tokens[0] == 'jgz':
        try:
            reg = registers[tokens[1]]
        except KeyError:
            reg = int(tokens[1])
        try:
            jmp = registers[tokens[2]]
        except KeyError:
            jmp = int(tokens[2])
        if reg > 0:
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
        cnt = cnt + 1
    if tokens[0] == 'add':
        try:
            val = registers[tokens[2]]
        except KeyError:
            val = int(tokens[2])
        registers[tokens[1]] = registers[tokens[1]] + val
        cnt = cnt + 1
    return cnt
# Task 2
registers_1 = {'a':0, 'b':0,  'i':0,'p':0,'f':0, 'waiting':False, 'sent': 0}
registers_2 = {'a':0, 'b':0,  'i':0,'p':1,'f':0, 'waiting':False, 'sent': 0}


cnt_1 = 0
cnt_2 = 0
queue_1 = deque()
queue_2 = deque()
while registers_1['waiting'] == False or registers_2['waiting'] == False:
    cnt_1 = interpret_line_2(instructions,cnt_1,registers_1,queue_1,queue_2)
    cnt_2 = interpret_line_2(instructions,cnt_2,registers_2,queue_2,queue_1)
print(registers_2['sent'])