#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 18:01:05 2016

@author: reini
"""

numpad = [[1,2,3],
          [4,5,6],
          [7,8,9]]
x = 1
y = 1
f = open('input_2.txt')
for line in iter(f):
    for i in line:
        if i=='D':
            y = max(min(y + 1,2),0)
        if i=='U':
            y = max(min(y - 1,2),0)
        if i=='L':
            x = max(min(x - 1,2),0)
        if i=='R':
            x = max(min(x + 1,2),0)
    print numpad[y][x]
f.close()
 
# part two
numpad2 = [[0,0,1,0,0],
           [0,2,3,4,0],
           [5,6,7,8,9],
           [0,'A','B','C',0],
           [0,0,'D',0,0]]
           
x = 2
y = 2
f = open('input_2.txt')
for line in iter(f):
    for i in line:
        x_new = x
        y_new = y
        if i=='D':
            y_new = max(min(y + 1,4),0)
        if i=='U':
            y_new = max(min(y - 1,4),0)
        if i=='L':
            x_new = max(min(x - 1,4),0)
        if i=='R':
            x_new = max(min(x + 1,4),0)
        if numpad2[y_new][x_new] != 0:
            x=x_new
            y=y_new
    print numpad2[y][x]
f.close()