#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 08:35:03 2016

@author: christian
"""
import re

f = open('input_22.txt')

re_numbers = re.compile(r'(\d{0,3})T')
re_index_x = re.compile(r'x(\d{1,2})')
re_index_y = re.compile(r'y(\d{1,2})')

nodes = list()
for line in iter(f):
    numbers = map(int,re.findall(re_numbers,line))
    if len(numbers) == 0:
        continue
    x = int(re.search(re_index_x,line).groups()[0])
    y = int(re.search(re_index_y,line).groups()[0])
    nodes.append((x,y,numbers))

viable_pairs = 0
for a in nodes:
    for b in nodes:
        if a[0] == b [0] and a[1] == b [1]:
            continue
        if a[2][1] == 0:
            continue
        if a[2][1] <= b[2][2]:
            viable_pairs = viable_pairs + 1
print viable_pairs

#Visualize disk states
output = list(list(' ' for x in range(37)) for y in range(25))
for n in nodes:
    if n[2][1] == 0:
        output[n[1]][n[0]] = '_'
    elif float(n[2][1])/n[2][0] > 0.9:
        output[n[1]][n[0]] = '#'
    else:
        output[n[1]][n[0]] = '.'
output[0][-1] = 'G'
for line in output:
    print ''.join(line)