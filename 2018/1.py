#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 15:05:43 2018

@author: reini
"""

with open('input1','r') as file:
    operations = [int(line) for line in file]
    
value = 0
for operation in operations:
    value += operation
    
print(value)

value = 0
values = set()
values.add(value)
running = True
iterations = 0
while running:
    iterations += 1
    for operation in operations:
        value += operation
        if value in values:
            print(value)
            running = False
            break
        values.add(value)
        
print(iterations)