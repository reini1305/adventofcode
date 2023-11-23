#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 08:14:01 2016

@author: christian
"""

import re
from itertools import permutations

def f(instructions,input):
    re_digit = re.compile(r'\d')
    re_letter = re.compile(r'letter \D')
    for line in instructions:
        if line.startswith('reverse'):
            d = map(int,re.findall(re_digit,line))
            if d[0]>0:
                input = input[:d[0]] + input[d[1]:d[0]-1:-1] + input[d[1]+1:]
            else:
                input = input[:d[0]] + input[d[1]::-1] + input[d[1]+1:]
        if line.startswith('swap position'):
            d = sorted(map(int,re.findall(re_digit,line)))
            input = input[:d[0]] + input[d[1]] + input[d[0]+1:d[1]] + input[d[0]] + input[d[1]+1:]
        if line.startswith('swap letter'):
            letters = re.findall(re_letter,line)
            input = input.replace(letters[0][-1],'z')
            input = input.replace(letters[1][-1],letters[0][-1])
            input = input.replace('z',letters[1][-1])
        if line.startswith('rotate left'):
            d = map(int,re.findall(re_digit,line))
            d = d[0] % len(input)
            input = input[d:] + input[:d]
        if line.startswith('rotate right'):
            d = map(int,re.findall(re_digit,line))
            d = d[0] % len(input)
            input = input[-d:] + input[:-d]
        if line.startswith('rotate based'):
            letters = re.findall(re_letter,line)
            d = input.find(letters[0][-1])
            if d>=4:
                d = d+1
            d = (d+1) % len(input)
            input = input[-d:] + input[:-d]
        if line.startswith('move'):
             d = map(int,re.findall(re_digit,line))
             if d[1]>d[0]:
                 input = input[:d[0]] + input[d[0]+1:d[1]+1] + input[d[0]] + input[d[1]+1:]
             else:
                 input = input[:d[1]] + input[d[0]] + input[d[1]:d[0]] + input[d[0]+1:]
    return input

fi = open('input_21.txt')
instructions = list()

input = 'abcdefgh'
#input = 'abcde'
for line in iter(fi):
    instructions.append(line)
fi.close()     
print f(instructions,input)

input = 'fbgdceah'
def f_inv(instructions,target):
  for p in permutations(target):
    if f(instructions,''.join(p))==target:
      return ''.join(p)

print f_inv(instructions,input)