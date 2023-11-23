#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 06:41:36 2016

@author: reini
"""
f = open('input_20.txt')

ranges = list()
for line in iter(f):
    tokens = line.split('-')
    ranges.append((int(tokens[0]),int(tokens[1])))

ranges = sorted(ranges, key= lambda x:x[0])
        
low, high = ranges[0]
allowed = 0
first = True
for l, h in ranges:
    if l <= high + 1:
        if h > high:
            high = h
    else:
        if first:
            print('Part 1:', high + 1)
            first = False
        allowed += (l - (high + 1))
        low, high = l, h

print('Part 2:', allowed)