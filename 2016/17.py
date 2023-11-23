#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 07:04:39 2016

@author: reini
"""
from hashlib import md5

input = 'ihgpwlah'
input = 'kglvqrro'
input = 'ulqzkmiv'
input = 'qzthpkfp'

# up. down, left, right
def get_walls(path):
    hash = md5(path).hexdigest()[:4]
    walls = list()
    for c in hash:
        if int(c,16)>10:
            walls.append(False)
        else:
            walls.append(True)
    return walls
        
def recursive_solve(x,y,path):
    global shortest
    if x==3 and y==3:
#        print path
        if len(path) < shortest:
            shortest = len(path)
        return path
    walls = get_walls(path)
    final_path = None
    for nx,ny,dir,wall in [(x,y-1,'U',0), (x,y+1,'D',1), (x-1,y,'L',2), (x+1,y,'R',3)]:
        if (not walls[wall]) and nx>=0 and ny>=0 and nx<=3 and ny<=3:
            tmp_path = path + dir
#            print tmp_path,shortest
            if len(tmp_path) > shortest:
                return None
            end_path = recursive_solve(nx,ny,tmp_path)
            if final_path == None:
                final_path = end_path
            elif end_path != None and len(end_path) < len(final_path):
                final_path = end_path
    return final_path

global shortest
shortest = 100000
shortest_path = recursive_solve(0,0,input)
print shortest_path[8:]

def recursive_solve_longest(x,y,path):
    global longest
    if x==3 and y==3:
#        print path
        if len(path) > longest:
            longest = len(path)
        return path
    walls = get_walls(path)
    final_path = None
    for nx,ny,dir,wall in [(x,y-1,'U',0), (x,y+1,'D',1), (x-1,y,'L',2), (x+1,y,'R',3)]:
        if (not walls[wall]) and nx>=0 and ny>=0 and nx<=3 and ny<=3:
            tmp_path = path + dir
#            print tmp_path,longest
            end_path = recursive_solve_longest(nx,ny,tmp_path)
            if final_path == None:
                final_path = end_path
            elif end_path != None and len(end_path) > len(final_path):
                final_path = end_path
    return final_path
    
global longest
longest = -100000
longest_path = recursive_solve_longest(0,0,input)
print len(longest_path) - len(input)