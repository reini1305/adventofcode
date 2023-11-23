#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 07:30:29 2017

@author: reini
"""

programs = dict()


with open('input12.txt') as infile:
    for line in infile:
        tokens = line.split()
        program = set()
        program.add(int(tokens[0]))
        programs[int(tokens[0])] = program
        
# add children
with open('input12.txt') as infile:
    for line in infile:
        tokens = line.split()
        for i in range(len(tokens)-2):
            child = int(tokens[i+2].replace(',',''))
            programs[int(tokens[0])].add(child)
            programs[child].add(int(tokens[0]))
        
# check who can reach 0
            
def can_reach(tree,visited,node,value):
    if visited[node]:
        return False
    visited[node] = True
    if node == value:
        return True
    if value in tree[node]:
        return True
    for child in tree[node]:
        if can_reach(tree,visited,child,value):
            return True
    return False

visited = [False for i in range(len(programs))]

count = 0

for i in range(len(programs)):
    visited = [False for j in range(len(programs))]
    if can_reach(programs,visited,i,0):
        count += 1