#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 08:05:05 2017

@author: reini
"""
import operator

registers = dict()

ops = { ">": operator.gt, 
        "<": operator.lt,
        "==": operator.eq,
        "!=": operator.ne,
        "<=": operator.le,
        ">=": operator.ge,
        "inc": operator.add,
        "dec": operator.sub}

def get_reg(name):
    if name in registers:
        return registers[name]
    return 0

curr_max = 0

with open('input8.txt') as instructionsfile:
    for instruction in instructionsfile:
        # cut into individual tokens
        tokens = instruction.split()
        if ops[tokens[5]](get_reg(tokens[4]),int(tokens[6])):
            registers[tokens[0]] = ops[tokens[1]](get_reg(tokens[0]),int(tokens[2]))
        curr_max = max(curr_max,max([val for val in registers.values()]))
            
print (max([val for val in registers.values()]))
print (curr_max)