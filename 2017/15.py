#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 07:10:13 2017

@author: reini
"""

val_a = 703
val_b = 516

def get_next_a(prev):
    return (prev * 16807) % 2147483647

def get_next_b(prev):
    return (prev * 48271) % 2147483647

count = 0
for i in range(40000000):
    val_a = get_next_a(val_a)
    val_b = get_next_b(val_b)
    if (val_a & 0xffff) == (val_b & 0xffff):
        count += 1
        
print (count)

def picky_a(prev):
    n = get_next_a(prev)
    while n%4 != 0:
        n = get_next_a(n)
    return n

def picky_b(prev):
    n = get_next_b(prev)
    while n%8 != 0:
        n = get_next_b(n)
    return n

val_a = 703
val_b = 516
count = 0
for i in range(5000000):
    val_a = picky_a(val_a)
    val_b = picky_b(val_b)
    if (val_a & 0xffff) == (val_b & 0xffff):
        count += 1
        
print (count)