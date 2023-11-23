#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 07:05:55 2016

@author: reini
"""

def part1(n):
    if(n == 1): 
        return 1

    if((n%2) == 0): 
        return 2 * part1(n / 2) - 1

    if((n%2) == 1): 
        return 2 * part1((n - 1) / 2) + 1

input = 3014387

print part1(input)


def part2(n):
    w = 1;
    for i in range(1,n):
        w = w % i + 1;
        if (w > (i + 1)/2):
            w = w + 1
    return w


print part2(input)