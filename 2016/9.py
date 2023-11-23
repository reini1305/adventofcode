#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 14:27:55 2016

@author: christian
"""
input = open('input_9.txt', 'r').readline().strip()
#input = input.replace('\n', '')
#input = 'A(1x5)BC'
#input = '(3x3)XYZ'
#input = 'A(2x2)BCD(2x2)EFG'
#input = '(6x1)(1x3)A'
#input = 'X(8x2)(3x3)ABCY'
#input = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
#input = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
out_string = list()
start_idx = 0
while start_idx<len(input):
    # append everything till the next command
    end_idx = input.find('(',start_idx)
    if end_idx<0:
        end_idx = len(input)
    out_string.append(input[start_idx:end_idx])
    start_idx = end_idx + 1 
    if start_idx>len(input):
        break
    end_idx = input.find(')',start_idx)
    command = input[start_idx:end_idx]
    tokens = command.split('x')
    repetitions = int(tokens[1])
    num_chars = int(tokens[0])
    start_idx = end_idx + 1
    for i in range(0,repetitions):
        out_string.append(input[start_idx:start_idx+num_chars])
    
    start_idx = start_idx + num_chars 
    
print len(''.join(out_string))

def getLength(data):
    length = i = 0
    while i < len(data):
        if data[i] == '(':
            markerEnd = data.find(')', i)
            (chars, repeat) = [int(x) for x in data[i + 1:markerEnd].split('x')]
            length += getLength(data[markerEnd + 1:markerEnd + chars + 1]) * repeat
            i = markerEnd + chars
        else:
            length += 1
        i += 1
    return length

print(getLength(input))