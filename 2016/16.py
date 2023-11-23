#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 09:35:57 2016

@author: root
"""

from copy import copy

input = '10111100110001111'
#input = '10000'
target_len = 272
target_len = 35651584
#target_len = 20
output = copy(input)

while len(output)<target_len:
    output = output + '0' + output[::-1].replace('1','2').replace('0','1').replace('2','0')
    
output = output[:target_len]
checksum = list()
for idx in range(0,len(output)-1,2):
    if output[idx]==output[idx+1]:
        checksum.append('1')
    else:
        checksum.append('0')
        
while len(checksum) % 2 == 0:
    output = copy(checksum)
    checksum = list()
    for idx in range(0,len(output)-1,2):
        if output[idx]==output[idx+1]:
            checksum.append('1')
        else:
            checksum.append('0')
            
print ''.join(checksum)