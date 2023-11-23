#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 22:28:33 2018

@author: christian
"""

with open('input1.txt','r') as file:
    input = file.read().strip()
    
print(sum([1 if x == '(' else -1 for x in input]))

floor = 0
for i,c in enumerate(input):
    if c == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(i+1)
        break