#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 07:58:08 2018

@author: christian
"""
import itertools

with open('input25.txt') as file:
    input = [[int(x) for x in line.strip().split(',')] for line in file]

def getDist(a,b):
    return sum([abs(x-y) for x,y in zip(a,b)])

def getClusterDist(a,b):
    minDist = 10000
    for x in itertools.product(a,b):
        minDist = min(getDist(x[0],x[1]),minDist)
    return minDist
    
clusters = []
for point in input:
    found_cluster = False
    for c in clusters:
        if found_cluster:
            break
        for pc in c:
            if getDist(point,pc) <= 3:
                c.append(point)
                found_cluster = True
                break
    if not found_cluster:
        clusters.append([point])
 
 
while True: 
    merged = False 
    for i,c in enumerate(clusters):
        for j,d in enumerate(clusters):
            if i == j:
                continue
            if getClusterDist(c,d) <= 3:
                c.extend(d)
                d.clear()
                merged = True
    if merged:
        for i in reversed(range(len(clusters))):
            if len(clusters[i]) == 0:
                del clusters[i]
    else:
        break
print(len(clusters))