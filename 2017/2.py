#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:04:49 2017

@author: reini
"""

#import numpy as np

checksum = 0
checksum2 = 0
with open('input2.txt') as infile:
    for line in infile:
        linemin = 10000
        linemax = 0
        for number in line.split():
            n = int(number)
            if n>linemax:
                linemax = n
            if n<linemin:
                linemin = n
            for number2 in line.split():
                n2 = int(number2)
                if n2 != n:
                    if n2 % n == 0:
                        checksum2 += n2/n
                        break
                    if n % n2 == 0:
                        checksum2 += n/n2
                        break
        checksum += linemax - linemin

print (checksum)
print (checksum2/2)