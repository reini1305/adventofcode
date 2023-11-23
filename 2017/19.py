#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 06:41:52 2017

@author: reini
"""

puzzle = [line for line in open('input19.txt')]

#puzzle = ['     |          ',
#          '     |  +--+    ',
#          '     A  |  C    ',
#          ' F---|----E|--+ ',
#          '     |  |  |  D ',
#          '     +B-+  +--+ ',
#          '                ']

x = puzzle[0].index('|')
y = 0
dx = 0
dy = 1

output=''
steps = -1
while x>=0 and y>=0 and x<len(puzzle[y]) and y<len(puzzle):
    curr_piece = puzzle[y][x]
    steps += 1
    if curr_piece.isalpha():
        output+=curr_piece 
    elif curr_piece == ' ':
        break
    elif curr_piece == '+': # we must turn
        if dx == 0:  # look left or right
            if puzzle[y][x+1] != ' ':
                dx = 1
                dy = 0
            elif puzzle[y][x-1] != ' ':
                dx = -1
                dy = 0
            else:
                break
            
        else:
            if puzzle[y+1][x] != ' ':
                dx = 0
                dy = 1
            elif puzzle[y-1][x] != ' ':
                dx = 0
                dy = -1 
            else:
                break
    x+=dx
    y+=dy
print(output)
print(steps)