#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 17:42:33 2016

@author: reini
"""

import hashlib

input = 'reyedfim'

test_int = 0
output = hashlib.md5(input+str(test_int)).hexdigest()
key1 = ''
key2=list('.' for x in range(0,8))
while '.' in key2:
    while output[:5]!='00000':
        test_int = test_int + 1
        output = hashlib.md5(input+str(test_int)).hexdigest()
    if len(key1)<=7:
        key1 = key1+output[5]
    try:
        idx = int(output[5])
    except ValueError:
        output=''
        continue
    if idx>=0 and idx <=7 and key2[idx]=='.':
        key2[idx] = output[6]
    output=''
    print 'Key 1: '+key1
    print 'Key 2: '+''.join(key2)