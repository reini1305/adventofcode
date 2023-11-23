#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 19:51:53 2017

@author: reini
"""

valid = 0
with open('input4.txt') as infile:
    for line in infile:
        unique_tokens = dict()
        for token in line.split():
            unique_tokens[token] = 1
        if len(unique_tokens) == len(line.split()):
            valid += 1
            
print (valid)

valid = 0
with open('input4.txt') as infile:
    for line in infile:
        unique_tokens = dict()
        for token in line.split():
            unique_tokens[''.join(sorted(token))] = 1
        if len(unique_tokens) == len(line.split()):
            valid += 1
            
print(valid)