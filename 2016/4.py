#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 15:27:48 2016

@author: reini
"""
from itertools import groupby

f = open('input_4.txt')
sum = 0
for line in iter(f):
    name=''
    for t in line.split('-'):
        if t[0].isdigit():
            number = int(t.split('[')[0])
            checksum = t.split('[')[1][0:-2]
        else:
            name = name + t

    occurences = list()
    for g in groupby(sorted(name)):
        occurences.append((len(list(g[1])),g[0]))
    check_should = ''.join(map(lambda x:x[1],sorted(sorted(occurences,key=lambda x:x[1]),key=lambda s:s[0],reverse=True)[0:5]))
    if check_should == checksum:
        sum = sum + number
        real_name =  ''.join(map(lambda x:chr((ord(x)-ord('a')+number)%26+ord('a')),name)) + ' ' + str(number)
        if 'pole' in real_name:
            print real_name
        
print 'Sum: ' + str(sum)