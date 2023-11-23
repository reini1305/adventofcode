#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 07:08:52 2018

@author: christian
"""
from copy import deepcopy
from collections import defaultdict

with open('input16.txt','r') as file:
    input = [line.strip() for line in file]
    
def addr(r,i):
    r[i[2]] = r[i[0]] + r[i[1]]

def addi(r,i):
    r[i[2]] = r[i[0]] + i[1]
    
def mulr(r,i):
    r[i[2]] = r[i[0]] * r[i[1]]
    
def muli(r,i):
    r[i[2]] = r[i[0]] * i[1]
    
def banr(r,i):
    r[i[2]] = r[i[0]] & r[i[1]]
    
def bani(r,i):
    r[i[2]] = r[i[0]] & i[1]

def borr(r,i):
    r[i[2]] = r[i[0]] | r[i[1]]
    
def bori(r,i):
    r[i[2]] = r[i[0]] | i[1]
    
def setr(r,i):
    r[i[2]] = r[i[0]]
    
def seti(r,i):
    r[i[2]] = i[0]
    
def gtir(r,i):
    r[i[2]] = 1 if i[0] > r[i[1]] else 0

def gtri(r,i):
    r[i[2]] = 1 if r[i[0]] > i[1] else 0
    
def gtrr(r,i):
    r[i[2]] = 1 if r[i[0]] > r[i[1]] else 0
    
def eqir(r,i):
    r[i[2]] = 1 if i[0] == r[i[1]] else 0

def eqri(r,i):
    r[i[2]] = 1 if r[i[0]] == i[1] else 0
    
def eqrr(r,i):
    r[i[2]] = 1 if r[i[0]] == r[i[1]] else 0

functions = []
functions.append(('addr', addr))
functions.append(('addi', addi))
functions.append(('mulr', mulr))
functions.append(('muli', muli))
functions.append(('banr', banr))
functions.append(('bani', bani))
functions.append(('borr', borr))
functions.append(('bori', bori))
functions.append(('setr', setr))
functions.append(('seti', seti))
functions.append(('gtir', gtir))
functions.append(('gtri', gtri))
functions.append(('gtrr', gtrr))
functions.append(('eqir', eqir))
functions.append(('eqri', eqri))
functions.append(('eqrr', eqrr))

opcodes = defaultdict(tuple)

emptycount = 0
threeormore = 0
instructions = []
for line in input:
    if line.startswith('Before'):
        before = eval(line[8:])
        emptycount=0
    elif line.startswith('After'):
        emptycount=0
        after = eval(line[7:])
        funccount = 0
        for f in functions:
            r = deepcopy(before)
            f[1](r,instructions[1:])
            if r == after:
                funccount += 1
        if funccount == 1:
            opcodes[instructions[0]]=f
        if funccount >= 3:
            threeormore += 1
    elif line == '':
        emptycount += 1
    else:
        emptycount = 0
        instructions = [int(i) for i in line.split()]
    if emptycount > 2:
        break
    
print(threeormore)
while len(opcodes)<16:
    for line in input:
        if line.startswith('Before'):
            before = eval(line[8:])
            emptycount=0
        elif line.startswith('After'):
            emptycount=0
            after = eval(line[7:])
            funccount = 0
            used_f = tuple()
            for f in functions:
                r = deepcopy(before)
                f[1](r,instructions[1:])
                if r == after:
                    funccount += 1
                    used_f = f
            if funccount == 1:
                opcodes[instructions[0]]=used_f
                functions.remove(used_f)
        elif line == '':
            emptycount += 1
        else:
            emptycount = 0
            instructions = [int(i) for i in line.split()]
        if emptycount > 2:
            break
        
emptycount = 0
registers = [0 for _ in range(4)]
for line in input:
    if emptycount < 3:
        if line == '':
            emptycount += 1
        else:
            emptycount = 0
        continue
    
    instructions = [int(i) for i in line.split()]
    opcodes[instructions[0]][1](registers,instructions[1:])
    
print(registers[0])