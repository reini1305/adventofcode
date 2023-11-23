#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 23:05:13 2017

@author: reini
"""

import numpy as np

rules = [line for line in open('input21.txt')]

def parse(xs):
    return np.array([list(row) for row in xs.split('/') ])

mutations = [lambda x: x, lambda x: np.fliplr(x),
             lambda x: np.rot90(x,1), lambda x: np.fliplr(np.rot90(x,1)),
             lambda x: np.rot90(x,2), lambda x: np.fliplr(np.rot90(x,2)),
             lambda x: np.rot90(x,3), lambda x: np.fliplr(np.rot90(x,3))]

enhancements = dict()

for line in rules:
    tokens = line.split(' => ')
    enhancements[parse(tokens[0]).tostring()] = parse(tokens[1].replace('\n',''))

def enhance(f):
    for m in mutations:
        if m(f).tostring() in enhancements:
            return enhancements[m(f).tostring()]
        
field = parse('.#./..#/###')
              
for iter in range(18):
    size = field.shape[0]
    if size % 2 == 0:
        tiles = [np.hsplit(v, size/2) for v in np.vsplit(field,size/2)]
    else:
        tiles = [np.hsplit(v, size/3) for v in np.vsplit(field,size/3)]
    
    field = np.vstack([ np.hstack([ enhance(j) for j in i ]) for i in tiles ])
    
    print(str(iter) + ' ' + str(np.count_nonzero(field == '#')))