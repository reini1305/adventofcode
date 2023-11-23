#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 07:28:17 2018

@author: christian
"""
from copy import deepcopy

bots = []
with open('input23.txt','r') as file:
    for line in file:
        pos = line.split()[0][5:-2]
        r = int(line.split()[1][2:])
        bots.append((tuple([int(x) for x in pos.split(',')]),r))
        
# Find largest bot
largest = sorted(bots,key=lambda x:x[1])[-1]

def getDist(x,y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1]) + abs(x[2]-y[2])

def reaches(b,bots):
    return sum([1 for bot in bots if getDist(bot[0],b[0]) <= b[1]])

def reach(bots,b):
    return sum([1 for bot in bots if getDist(bot[0],b) <= bot[1]])

in_reach = reaches(largest,bots)
print(in_reach)


xs = [x[0][0] for x in bots]
ys = [x[0][1] for x in bots]
zs = [x[0][2] for x in bots]

step = 1
while step < max(xs) - min(xs):
    step *= 2

while True:
    target_count = 0
    best = None
    best_val = None
    for x in range(min(xs), max(xs) + 1, step):
        for y in range(min(ys), max(ys) + 1, step):
            for z in range(min(zs), max(zs) + 1, step):
                count = reach(bots,(x,y,z))
                if count > target_count:
                    target_count = count
                    best_val = abs(x) + abs(y) + abs(z)
                    best = (x, y, z)
                elif count == target_count:
                    if not best_val or abs(x) + abs(y) + abs(z) < best_val:
                        best_val = abs(x) + abs(y) + abs(z)
                        best = (x, y, z)

    if step == 1:
        break
    else:
        xs = [best[0] - step, best[0] + step]
        ys = [best[1] - step, best[1] + step]
        zs = [best[2] - step, best[2] + step]
        step = int(step/2)
            
print(best_val)