#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 07:56:47 2017

@author: reini
"""

with open('input24.txt') as f:
    data = f.read().splitlines()

parts = [list(map(int, line.split('/'))) for line in data]

def score(bridge):
    return sum([sum(part) for part in bridge])

def search(base, port, parts):
    choices = [part for part in parts if port in part]
    if not choices: return [base]

    outputs = []
    for choice in choices:
        left = parts[:]
        left.remove(choice)
        part = choice[:] 
        part.remove(port)
        outputs += search(base + [choice], part[0], left)
    return outputs

outputs = search([], 0, parts)
scores = [(len(o), score(o)) for o in outputs]
print('highest', max([s[1] for s in scores]))
print('longest', max([(s[0], s[1]) for s in scores]))
