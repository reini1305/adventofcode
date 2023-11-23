#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 06:13:01 2016

@author: reini
"""

import numpy as np
import re
import matplotlib.pyplot as plt
f=open('input_8.txt')

display = np.zeros((6,50))
for line in iter(f):
    command = line.split('=')
    if 'rect' in command[0]:
        coords = map(int,re.search(r'([-+]?\d+)x([-+]?\d+)',command[0]).groups())
        display[:coords[1],:coords[0]] = 1
    if 'column' in command[0]:
        coords = map(int,re.search(r'([-+]?\d+) by ([-+]?\d+)',command[1]).groups())
        display[:,coords[0]] = np.roll(display[:,coords[0]],coords[1])
    if 'row' in command[0]:
        coords = map(int,re.search(r'([-+]?\d+) by ([-+]?\d+)',command[1]).groups())
        display[coords[0],:] = np.roll(display[coords[0],:],coords[1])
plt.imshow(display)
print sum(sum(display))