#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:23:55 2017

@author: reini
"""

#import numpy as np
import math
inputValue = 265149


#inputValue = int(input())

layer = math.floor(math.ceil(math.sqrt(inputValue)) / 2)+1
maxVal = (2*layer - 1)
squaredMaxVal = maxVal ** 2
distToClosestEdge = maxVal

for i in range(5):
    if (abs(squaredMaxVal - i*(maxVal-1) - inputValue) < distToClosestEdge):
        distToClosestEdge = abs(squaredMaxVal - i*(maxVal-1) - inputValue)

print(maxVal - 1 - distToClosestEdge)
