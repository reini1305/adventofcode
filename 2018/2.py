#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 08:43:56 2018

@author: reini
"""
import numpy as np

with open('input2','r') as file:
    boxes = [line.strip() for line in file]

twos = 0
threes = 0    
for box in boxes:
    letters = dict()
    for letter in box:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    twos += 2 in letters.values()
    threes += 3 in letters.values()

print(twos*threes)

def getDiff(string1, string2):
    count_diff = 0
    for letter1,letter2 in zip(string1,string2):
        if letter1 != letter2:
            count_diff += 1
    return count_diff

for box_id1 in np.arange(len(boxes)):
    for box_id2 in np.arange(box_id1 +1, len(boxes)):
        if getDiff(boxes[box_id1],boxes[box_id2])==1:
            print("".join([x if x==y else "" for x,y in zip(boxes[box_id1],boxes[box_id2])]))
            break