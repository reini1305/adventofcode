#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 18:34:09 2016

@author: reini
"""

import itertools
import numpy as np
combinations = list(itertools.permutations([0,1,2]))

num_valid = 0
f = open('input_3.txt')
for line in iter(f):
    sides = map(int,line.split())
    is_valid = True
    for c in iter(combinations):
        if(sides[c[0]]+sides[c[1]])<=sides[c[2]]:
            is_valid = False
    if is_valid:
        num_valid = num_valid + 1
print num_valid
f.close()

# part 2

num_valid = 0
f = open('input_3.txt')
line_counter = 0
lines = list()
for line in iter(f):
    lines.append(map(int,line.split()))
    line_counter = line_counter + 1
    if line_counter>2:
        line_counter = 0
        triangles = np.array(lines).transpose()
        lines = list()
        for i in range(0,3):
            sides = triangles[i,:]
            is_valid = True
            for c in iter(combinations):
                if(sides[c[0]]+sides[c[1]])<=sides[c[2]]:
                    is_valid = False
            if is_valid:
                num_valid = num_valid + 1
print num_valid
f.close()