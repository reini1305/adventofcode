#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 09:39:35 2017

@author: reini
"""

non_canceled_garbage = 0
ignore_mode = False
within_garbage = False
current_score = 0
current_nest = 0
             
def begin_garbage():
    global within_garbage
    global ignore_mode
    global non_canceled_garbage
    if within_garbage and not ignore_mode:
        non_canceled_garbage -= 1
    within_garbage = True
    ignore_mode = False
    
def begin_group():
    global within_garbage
    global ignore_mode
    global current_nest
    global current_score
    global non_canceled_garbage
    if not ignore_mode and not within_garbage:
        current_nest += 1
        current_score += current_nest
    ignore_mode = False
    
def ignore():
    global within_garbage
    global ignore_mode
    global non_canceled_garbage
    if within_garbage and not ignore_mode:
        ignore_mode = True 
    else:
        ignore_mode = False
    
def end_group():
    global within_garbage
    global ignore_mode
    global current_nest
    if not ignore_mode and not within_garbage:
        current_nest -= 1
    ignore_mode = False
    
def end_garbage():
    global within_garbage
    global ignore_mode
    if not ignore_mode:
        within_garbage = False
    ignore_mode = False
    
functions = {'<': begin_garbage,
             '>': end_garbage,
             '{': begin_group,
             '}': end_group,
             '!': ignore}        

with open('input9.txt') as inputfile:
    for line in inputfile:
        for char in line:
            if char in functions:
                functions[char]()
                if within_garbage and not ignore_mode:
                    non_canceled_garbage += 1
            else:
                if within_garbage and not ignore_mode:
                    non_canceled_garbage += 1
                ignore_mode = False
            
                
print (current_score)
print (non_canceled_garbage)

with open('input9.txt') as f:
    inputs = [ s[:-1] for s in f.readlines() ]

for s in inputs: # loop to also process test inputs
    level, ignore_next, in_garbage, total, garbage = 0, False, False, 0, 0
    for c in s:
        if ignore_next: ignore_next = False
        elif in_garbage:
            if c == '!': ignore_next = True
            elif c == '>': in_garbage = False
            else: garbage += 1
        elif c == '<':
            in_garbage = True
        elif c == '{':
            level += 1
            total += level
        elif c == '}':
            level -= 1
    print(s[0:50], total, garbage)
