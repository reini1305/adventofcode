# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

directions = 'R2, L5, L4, L5, R4, R1, L4, R5, R3, R1, L1, L1, R4, L4, L1, R4, L4, R4, L3, R5, R4, R1, R3, L1, L1, R1, L2, R5, L4, L3, R1, L2, L2, R192, L3, R5, R48, R5, L2, R76, R4, R2, R1, L1, L5, L1, R185, L5, L1, R5, L4, R1, R3, L4, L3, R1, L5, R4, L4, R4, R5, L3, L1, L2, L4, L3, L4, R2, R2, L3, L5, R2, R5, L1, R1, L3, L5, L3, R4, L4, R3, L1, R5, L3, R2, R4, R2, L1, R3, L1, L3, L5, R4, R5, R2, R2, L5, L3, L1, L1, L5, L2, L3, R3, R3, L3, L4, L5, R2, L1, R1, R3, R4, L2, R1, L1, R3, R3, L4, L2, R5, R5, L1, R4, L5, L5, R1, L5, R4, R2, L1, L4, R1, L1, L1, L5, R3, R4, L2, R1, R2, R1, R1, R3, L5, R1, R4'

# heading: 0:N 1:W 2:S 3:E
heading = 0
x = 0
y = 0
visited = set()
visited.add((x,y))
found = False
for d in directions.split(', '):
    dir = d[0]
    amount = int(d[1:])
    if dir=='R':
        heading = (heading + 1) % 4
    if dir=='L':
        heading = (heading - 1) % 4
    for i in range(0,amount):
        if heading == 0:
            y = y - 1
        if heading == 1:
            x = x + 1
        if heading == 2:
            y = y + 1
        if heading == 3:
            x = x - 1
        #print str(x) + '|' + str(y)
        if not found and (x,y) in visited:
            print 'HQ at: '+str(x)+'|'+str(y)+' Dist: '+ str(abs(x) + abs(y))
            found=True
        visited.add((x,y))
    
    
print abs(x) + abs(y)