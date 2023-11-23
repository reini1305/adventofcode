#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 16:33:06 2018

@author: christian
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 06:10:15 2018

@author: christian
"""

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

functions = dict()
functions['addr'] = addr
functions['addi'] = addi
functions['mulr'] = mulr
functions['muli'] = muli
functions['banr'] = banr
functions['bani'] = bani
functions['borr'] = borr
functions['bori'] = bori
functions['setr'] = setr
functions['seti'] = seti
functions['gtir'] = gtir
functions['gtri'] = gtri
functions['gtrr'] = gtrr
functions['eqir'] = eqir
functions['eqri'] = eqri
functions['eqrr'] = eqrr

with open('input21.txt','r')as file:
    input = [line.strip().split() for line in file]
    
for line in input:
    line[1:] = [int(x) for x in line[1:]]
    
registers = [0 for _ in range(6)]
ipr = input[0][1]
del input[0]

while registers[ipr] < len(input):
    i = input[registers[ipr]]
    if i[0] == 'eqrr':
        print(registers[i[1]])
        break
    functions[i[0]](registers,i[1:])
    registers[ipr]+= 1

registers = [0 for _ in range(6)]
seen = []
while registers[ipr] < len(input):
    i = input[registers[ipr]]
    if i[0] == 'eqrr':
        if registers[i[1]] in seen:
            print(seen[-1])
            break
        seen.append(registers[i[1]])
    functions[i[0]](registers,i[1:])
    registers[ipr]+= 1