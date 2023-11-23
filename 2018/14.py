#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 06:07:30 2018

@author: christian
"""

def part1(input):
    recipes = [3,7]
    elves_id = [0,1]
    while len(recipes) < input+10:
        sum_recipes = recipes[elves_id[0]] + recipes[elves_id[1]]
        digits = str(sum_recipes)
        recipes.extend([int(d) for d in digits])
        elves_id[0] = (elves_id[0] + 1 + recipes[elves_id[0]]) % len(recipes)
        elves_id[1] = (elves_id[1] + 1 + recipes[elves_id[1]]) % len(recipes)
    return  ''.join([str(r) for r in recipes[input:input+10]])

print(part1(327901))

def part2(i):
    r = [3,7]
    a = 0
    b = 1
    si = str(i)
    while si not in ''.join(map(str,r[-10:])):
        s = r[a] + r[b]
        r.extend(list(map(int,str(s))))
        a = (a + r[a] + 1) % len(r)
        b = (b + r[b] + 1) % len(r)
        
    return(''.join(map(str,r)).index(si))   

print(part2(327901))