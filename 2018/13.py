#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 19:15:13 2018

@author: christian
"""

grid = list() 
with open('input13.txt','r') as file:
    for line in file:
        grid.append([l for l in line.strip('\n')])
        
p1 = p2 = None
moves = { '^': ( 0, -1), '>': ( 1,  0), 'v': ( 0,  1), '<': (-1,  0) }
curves = {'\\': 1, '/': -1}
dirs = list(moves.keys())
turns = [ lambda d: (d[1], -d[0]), lambda d: d, lambda d: (-d[1], d[0]) ]
carts = []

for y, l in enumerate(grid):
    for x, c in [(i, c) for i, c in enumerate(l) if c in dirs]:
        carts.append(((x, y), moves[c], 0))
        l[x] = '-' if c in ['<', '>'] else '|'

while len(carts) > 1:
    carts = sorted(carts, key=lambda c: (c[0][1], c[0][0]))
    collided = []

    for i, c in enumerate(carts):
        if c in collided:
            continue

        (x, y), (dx, dy), t = c
        positions, _, _ = zip(*carts)
        nx, ny = (x + dx, y + dy)
        ns = grid[ny][nx]

        if ((nx, ny) in positions):
            p1 = p1 or (nx, ny)
            collided += [c for c in carts if c[0] in [(x, y), (nx, ny)]]
            continue

        if ns == '+':
            dx, dy = turns[t % len(turns)]((dx, dy))
            t += 1

        if ns in curves:
            f = curves[ns]
            dx, dy = (dy * f, dx * f)

        carts[i] = ((nx, ny), (dx, dy), t)

    carts = [c for c in carts if c not in collided]

p2 = carts[0][0]
print('P1: {}'.format(p1))
print('P2: {}'.format(p2))