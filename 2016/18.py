#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 08:32:09 2016

@author: reini
"""
from copy import copy

input = '.^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^....'
#input = '..^^.'
#input = '.^^.^.^^^^'

sum_safe = input.count('.')
output = copy(input)
for row in range(400000-1):
    aug_input = '.' + output + '.'
    output = list()
    for i in range(1,len(aug_input)-1):
        if aug_input[i-1:i+2] == '^^.' or aug_input[i-1:i+2] == '.^^' or aug_input[i-1:i+2] == '^..' or aug_input[i-1:i+2] == '..^':
            output.append('^')
        else:
            output.append('.')
    output = ''.join(output)
#    print output
    sum_safe = sum_safe + output.count('.')
print sum_safe