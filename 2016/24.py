# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from copy import deepcopy
import numpy as np
import sys
from itertools import permutations

sys.setrecursionlimit(10000)

f = open('input_24.txt')

maze = list()
numbers = list((0,0) for x in range(8))

for y,line in enumerate(iter(f)):
    line = line.replace('\n','')
    mazeline = list()
    for x,l in enumerate(line):
        if l=='#':
            mazeline.append('#')
        else:
            mazeline.append(-1)
        try:
            val = int(l)
        except ValueError:
            val = -1
        if val>=0:
            numbers[val] = (x,y)
        
    maze.append(mazeline)
f.close()

def recursive_solve(maze,x,y):
    for nx,ny in [(x,y-1), (x-1,y), (x+1,y), (x,y+1)]:
        if nx>=0 and ny>=0 and nx<len(maze[0]) and ny<len(maze) and maze[ny][nx] != '#' and (maze[ny][nx] == -1 or maze[ny][nx] > maze[y][x]+1):
            maze[ny][nx] = maze[y][x]+1
            recursive_solve(maze, nx, ny)
            
# Find minimum paths between all nodes
orig_maze = deepcopy(maze)
distances = 10e3*np.ones((8,8))

for start in range(8):
    maze = deepcopy(orig_maze)
    s_coord = numbers[start]
    maze[s_coord[1]][s_coord[0]] = 0
    recursive_solve(maze,s_coord[0],s_coord[1])
    for end in range(8):
        e_coord = numbers[end]
        distances[start][end] = maze[e_coord[1]][e_coord[0]]
        distances[end][start] = maze[e_coord[1]][e_coord[0]]

# Enumerate all possible ways and calculate length
way = range(1,8)
shortest = 10e10
for per in permutations(way):
    per = [0] + list(per)
    curr_path = sum(distances[per[x]][per[x+1]] for x in range(7))
    if curr_path<shortest:
        shortest = curr_path
        best_path = per
print "Task 1: shortest path= " + str(best_path) + ' ' + str(shortest)  
# Enumerate all possible ways and calculate length
shortest = 10e10
for per in permutations(way):
    per = [0] + list(per) + [0]
    curr_path = 0
    curr_path = sum(distances[per[x]][per[x+1]] for x in range(8))
    if curr_path<shortest:
        shortest = curr_path
        best_path = per
print "Task 2: shortest path= " + str(best_path) + ' ' + str(shortest)