#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 06:26:47 2018

@author: christian
"""

import numpy as np
from collections import defaultdict

with open('input6','r') as file:
    input = [line.strip().split(',') for line in file]
   
def getMinManhattanDist(point, coordinates):
    min_coord = list()
    min_dist = 10000
    for i,coordinate in enumerate(coordinates):
        dist = np.sum(abs((np.subtract(point,coordinate))))
        if dist == min_dist:
            min_coord.append(i)
        elif dist < min_dist:
            min_dist = dist
            min_coord = list()
            min_coord.append(i)
    return None if len(min_coord) > 1 else min_coord[0]
    
coordinates = list()
max_x = 0
max_y = 0
for coordinate in input:
    coordinates.append((int(coordinate[0]),int(coordinate[1])))
    max_x = max(max_x, coordinates[-1][0])
    max_y = max(max_y, coordinates[-1][1])
    
nearest_points = defaultdict(list)
is_infinite = [False for x in coordinates]
for x in range(max_x):
    for y in range(max_y):
        closest = getMinManhattanDist((x,y),coordinates)
        if closest:
            if x ==0 or y == 0 or x == max_x - 1 or y == max_y - 1:
                is_infinite[closest] = True
            nearest_points[closest].append((x,y))
            
max_size = 0
for i in range(len(coordinates)):
    if not is_infinite[i]:
        max_size = max(max_size,len(nearest_points[i]))
        
print(max_size)

def getSumManhattanDist(point, coordinates):
    sum_dist = 0
    for i,coordinate in enumerate(coordinates):
        sum_dist += np.sum(abs((np.subtract(point,coordinate))))
    return sum_dist

num_within_safe = 0

for x in range(max_x):
    for y in range(max_y):
        if getSumManhattanDist((x,y),coordinates) < 10000:
            num_within_safe += 1

print(num_within_safe)