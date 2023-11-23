#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 06:05:12 2018

@author: reini
"""

from collections import defaultdict, Counter
from dateutil import parser


def most_common(lst):
    return max(set(lst), key=lst.count)

with open('input4','r') as file:
    input = [line.strip() for line in file]
    
instructions = list()
for line in input:
    date = parser.parse(line[1:17])
    instructions.append((date,line[19:]))
    
instructions.sort(key=lambda tup:tup[0])

guard_asleep_map = defaultdict(list)
current_guard = 0
fell_asleep = -1
for instruction in instructions:
    if instruction[1].startswith('Guard'):
        current_guard = int(instruction[1].split()[1][1:])
        fell_asleep=-1
    elif instruction[1].startswith('falls'):
        fell_asleep = instruction[0].minute
    elif instruction[1].startswith('wakes') and fell_asleep != -1:
        guard_asleep_map[current_guard].extend(range(fell_asleep,instruction[0].minute))
        
num_asleep=[len(x) for x in guard_asleep_map.values()]
most_asleep=list(guard_asleep_map.keys())[num_asleep.index(max(num_asleep))]

print(most_asleep * most_common(guard_asleep_map[most_asleep]))

# Task 2
most_minutes = 0
most_minute = 0
most_minute_guard = 0
for guard,minutes in guard_asleep_map.items():
    curr_guard = Counter(guard_asleep_map[guard]).most_common()[0]
    if curr_guard[1] > most_minutes:
        most_minutes = curr_guard[1]
        most_minute = curr_guard[0]
        most_minute_guard = guard
        
print(most_minute_guard * most_minute)
