#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 06:36:17 2016

@author: reini
"""

input = 1358
max_x = 150
max_y = 150

def get_wall(input,x,y):
    num = x*x + 3*x + 2*x*y + y + y*y + input
    if(bin(num).count('1') % 2) != 0:
        return ''
    else:
        return -1
        
maze = list(list(get_wall(input,x,y) for x in range(0,max_x)) for y in range(0,max_y))

def recursive_solve(maze,x,y):
    for nx,ny in [(x,y-1), (x-1,y), (x+1,y), (x,y+1)]:
        if nx>=0 and ny>=0 and nx<len(maze[0]) and ny<len(maze) and maze[ny][nx] != '' and (maze[ny][nx] == -1 or maze[ny][nx] > maze[y][x]+1):
            maze[ny][nx] = maze[y][x]+1
            recursive_solve(maze, nx, ny)
maze[1][1]=0
recursive_solve(maze,1,1)
s = maze[39][31]

count = 0
for y in range(0,max_y):
    for x in range(0,max_x):
        if maze[y][x]!='' and maze[y][x]!=-1 and maze[y][x]<=50:
            count = count +1