#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 21:52:07 2016

@author: reini
"""

from itertools import groupby

f = open('input_6.txt')
sum = 0
occurences = list(list() for x in range(0,8))
for line in iter(f):
    for i in range(0,8):
        occurences[i].append(line[i])
key = ''
key2 = ''
for i in range(0,8):
    o = list()
    for g in groupby(sorted(occurences[i])):
        o.append((len(list(g[1])),g[0]))
    key = key + sorted(o,key=lambda x:x[0])[-1][1]
    key2 = key2 + sorted(o,key=lambda x:x[0])[0][1]
print key
print key2