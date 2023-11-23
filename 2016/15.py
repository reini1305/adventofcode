# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/christian/.spyder2/.temp.py
"""

disks = [(7,0,1),(13,0,2),(3,2,3),(5,2,4),(17,0,5),(19,7,6)]
#disks = [(5,4,1),(2,1,2)]

time = 0
while sum(map(lambda x:(time+x[1]+x[2])%x[0],disks)) != 0:
    time = time +1
print time
time = 0
disks.append((11,0,7))
while sum(map(lambda x:(time+x[1]+x[2])%x[0],disks)) != 0:
    time = time +1
print time