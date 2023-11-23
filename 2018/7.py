#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 15:05:14 2018

@author: reinbc
"""
from collections import defaultdict

parents=defaultdict(set)

with open('input7','r') as file:
    for line in file:
        parents[line.split()[7]].add(line.split()[1])
        
def getAvailable(parents):
    all_parents = set()
    for x in parents.values():
        for y in x:
            all_parents.add(y)
            
    available = set()
    for x in all_parents:
        if not x in parents.keys():
            available.add(x)
    return available


solution = ''
while parents:
    available = getAvailable(parents)
    nextc = sorted(available)[0]
    solution += nextc
    available.remove(nextc)
    
    for key,values in parents.items():
        if nextc in values:
            parents[key].remove(nextc)
    
    if len(parents) == 1:
        solution += ''.join(sorted(available))
        solution += list(parents.keys())[0]
        break
    for key in list(parents.keys()):       
        if not parents[key]:
            del parents[key]

print(solution)

# part 2
#parents=defaultdict(set)
#
#with open('input7_light','r') as file:
#    for line in file:
#        parents[line.split()[7]].add(line.split()[1])
#        
#t = 0
#workers = [0 for _ in range(2)]
#last_available = None
#
#available = getAvailable(parents)
#for key,values in parents.items():
#    if sorted(available)[0] in values:
#        parents[key].remove(sorted(available)[0])
#    
#while parents or sum(workers) > 0:
#    for i,_ in enumerate(workers):
#        workers[i] = max(0, workers[i]-1)
#        if workers[i] == 0 and available:
#            workers[i] = 1 + ord(sorted(available)[0]) - ord('A')
#            available.remove(sorted(available)[0])
#    
#    if last_available and parents:
#        available = set(last_available)
#        del parents[last_available]
#    elif not available:
#        available = getAvailable(parents)
#        for key,values in parents.items():
#            if sorted(available)[0] in values:
#                parents[key].remove(sorted(available)[0])
#        if len(parents) == 1 and not last_available:
#            last_available = list(parents.keys())[0]
#        else:
#            for key in parents.keys():       
#                if not parents[key]:
#                    del parents[key]
#    
#    t += 1
