#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 07:11:00 2018

@author: reini
"""
import re
from collections import defaultdict
import numpy as np

with open('input3','r') as file:
    input = [line.strip() for line in file]

m = defaultdict(list)
for i,line in enumerate(input):
    claim = [int(x) for x in re.findall(r'\d+',line.split('@')[1])]
    x = claim[0]
    y = claim[1]
    w = claim[2]
    h = claim[3]
    for xrange in np.arange(x,x+w):
        for yrange in np.arange(y,y+h):
            m[(xrange,yrange)].append(i+1)

print(sum([1 if len(x)>1 else 0 for x in m.values()]))

for i,line in enumerate(input):
    claim = [int(x) for x in re.findall(r'\d+',line.split('@')[1])]
    x = claim[0]
    y = claim[1]
    w = claim[2]
    h = claim[3]
    overlapping = False
    for xrange in np.arange(x,x+w):
        for yrange in np.arange(y,y+h):
            if len(m[(xrange,yrange)]) > 1:
                overlapping = True
    if overlapping == False:
        print(i+1)