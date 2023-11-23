#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 07:07:51 2018

@author: christian
"""
import networkx
import enum

depth = 6969
target = (9,796)

map = dict()
risk = 0
for x in range(target[0]+50):
    for y in range(target[1]+50):
        # Get geologic index
        if x == 0:
            g = y * 48271
        elif y == 0:
            g = x * 16807
        else:
            g = map[(x-1,y)][0] * map[(x,y-1)][0]
        if (x,y) == target:
            g = 0
        e = (g + depth) % 20183
        t = e % 3
        if x <= target[0] and y <= target[1]:
            risk += t
        map[(x,y)] = (e,g,t)

print(risk)

class Region(enum.IntEnum):
    ROCKY = 0
    WET = 1
    NARROW = 2

class Tool(enum.Enum):
    CLIMBING_GEAR = enum.auto()
    TORCH = enum.auto()
    NEITHER = enum.auto()

    def usable(self, region):
        return region in {
            Tool.CLIMBING_GEAR: {Region.ROCKY, Region.WET},
            Tool.TORCH: {Region.ROCKY, Region.NARROW},
            Tool.NEITHER: {Region.WET, Region.NARROW},
        }[self]
        
def nb4(p):
    x, y = p
    return [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]

g = networkx.Graph()
for x in range(target[0]+49):
    for y in range(target[1]+49):
        _, _, t = map[(x,y)]
        p = (x,y)
        if t == Region.ROCKY:
            g.add_edge((p,Tool.CLIMBING_GEAR),(p,Tool.TORCH), weight = 7)
        elif t == Region.WET:
            g.add_edge((p,Tool.CLIMBING_GEAR),(p,Tool.NEITHER), weight = 7)
        else:
            g.add_edge((p,Tool.NEITHER),(p,Tool.TORCH), weight = 7)
            
        for nb in nb4(p):
            if 0 <= nb[0] and 0 <= nb[1]:
                for tool in Tool:
                    if tool.usable(t) and tool.usable(map[nb][2]):
                        g.add_edge((p,tool),(nb,tool), weight = 1)
                        
print(networkx.algorithms.astar_path_length(g, ((0, 0), Tool.TORCH), (target, Tool.TORCH)))