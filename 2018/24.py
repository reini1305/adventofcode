#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 08:51:25 2018

@author: christian
"""
#from collections import namedtuple

#Group = namedtuple('Group','army units hitpoints damage attack initiative weaknesses immunities')
current = 'immune'
groups = []
#attacks = set()
with open('input24.txt','r') as file:
    for line in file:
        if line.startswith("Immune"):
            continue
        elif line.startswith("Infection"):
            current = 'infection'
            continue
        elif line == "\n":
            continue
        else:
            group = dict()
            words = line.split()
            group["units"] = int(words[0])
            group["hp"] = int(words[4])
            group["initiative"] = int(words[-1])
            group["damage"] = int(words[-6])
            group["attack"] = words[-5]
#            attacks.add(a)
            imu = []
            words = line.split('immune to ')
            if len(words)>1:
                for im in words[1].split(', '):
                    if im.find(';')>0:
                        imu.append(im[:im.find(';')])
                        break
                    elif im.find(')')>0:
                        imu.append(im[:im.find(')')])
                    else:
                        imu.append(im)
            group["immunities"] = imu
            weak = []
            words = line.split('weak to ')
            if len(words)>1:
                for im in words[1].split(', '):
                    if im.find(';')>0:
                        weak.append(im[:im.find(';')])
                        break
                    elif im.find(')')>0:
                        weak.append(im[:im.find(')')])
                    else:
                        weak.append(im)
            group["weaknesses"] = weak
            group["army"] = current
            group["pick"] = -1
            groups.append(group)

def getDamage(a,v):
    damage = a["units"] * a["damage"]
    if a["attack"] in v["immunities"]:
        return 0
    if a["attack"] in v["weaknesses"]:
        return damage * 2
    return damage

def attack(a,d):
    damage = getDamage(a,d)
    d["units"] = max(d["units"] - int(damage/d["hp"]), 0)
    
num_immune = 1000
num_infection = 1000

while num_immune > 0 and num_infection > 0: 
    print([g["units"] for g in groups])          
    # Target Selection
    groups.sort(key = lambda x: (x["units"]*x["damage"],x["initiative"]), reverse = True)
    picks = set()
    
    for i,attacker in enumerate(groups):
        largest_ep = 0
        highest_initiative = 0
        largest_damage = 0
        pick = -1
        for j,victim in enumerate(groups):
            if victim["army"] == attacker["army"] or j in picks:
                continue
            d = getDamage(attacker,victim)
            ep = victim["units"] * victim["damage"]
            if d > largest_damage:
                largest_damage = d
                pick = j
                highest_ep = ep
                highest_initiative = victim["initiative"]
            elif d == largest_damage:
                if ep > highest_ep:
                    largest_damage = d
                    pick = j
                    highest_ep = ep
                    highest_initiative = victim["initiative"]
                elif ep == highest_ep:
                    if victim["initiative"] > highest_initiative:
                        largest_damage = d
                        pick = j
                        highest_ep = ep
                        highest_initiative = victim["initiative"]
        if largest_damage == 0:
            pick = -1
        picks.add(pick)
        attacker["pick"] = pick
    # Fighting
    for attacker in sorted(groups,key = lambda x:x["initiative"], reverse = True):
        if attacker["units"] > 0 and attacker["pick"] >= 0:
            attack(attacker,groups[attacker["pick"]])
        
        
    # Check if over
    num_immune = sum([1 for g in groups if g["army"] == 'immune' and g["units"] > 0 ])
    num_infection = sum([1 for g in groups if g["army"] == 'infection' and g["units"] > 0 ])
    
print(sum([g["units"] for g in groups if g["army"] == 'immune']))
print(sum([g["units"] for g in groups if g["army"] == 'infection']))