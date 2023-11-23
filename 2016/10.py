#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 07:44:33 2016

@author: reini
"""
import re

def create_bot():
    bot = {'chips': list(), 'low': [], 'high': []}
    return bot
    
def update_bots(bots,output):
    changes_made = True
    while changes_made:
        changes_made = False
        for key in bots:
            if len(bots[key]['chips'])==2:
                # give high to someone
                high = max(bots[key]['chips'])
                if bots[key]['high']!=[]:
                    if bots[key]['high']>=0:
                        if bots[key]['high'] not in bots:
                            bots[bots[key]['high']] = create_bot()
                        bots[bots[key]['high']]['chips'].append(high) 
                    else:
                        out_id = -bots[key]['high']-1
                        if out_id not in output:
                            output[out_id] = list()
                        output[out_id].append(high)
                    bots[key]['chips'].remove(high)
                    changes_made = True
                # give low to someone
                low = min(bots[key]['chips'])
                if bots[key]['low']!=[]:
                    if bots[key]['low']>=0:
                        if bots[key]['low'] not in bots:
                            bots[bots[key]['low']] = create_bot()
                        bots[bots[key]['low']]['chips'].append(low) 
                    else:
                        out_id = -bots[key]['low']-1
                        if out_id not in output:
                            output[out_id] = list()
                        output[out_id].append(low)
                    bots[key]['chips'].remove(low)
                    changes_made = True
                if high == 61 and low == 17:
                    print key
                if changes_made:
                    break
            
    return bots,output
    
f = open('input_10.txt')
output = dict()
bots = dict()

for line in iter(f):
    if line.startswith('value'):
        # create or update bot
        command = map(int,re.findall(r' (\d+)',line))
        if command[1] not in bots:
            bots[command[1]] = create_bot()
        bots[command[1]]['chips'].append(command[0])
    if line.startswith('bot'):
        command = map(int,re.findall(r'bot (\d+)',line))
        if command[0] not in bots:
            bots[command[0]] = create_bot()
        out_bin = map(int,re.findall(r'low to output (\d+)',line))
        if out_bin!=[]:
            bots[command[0]]['low'] = -out_bin[0]-1
        out_bin = map(int,re.findall(r'high to output (\d+)',line))
        if out_bin!=[]:
            bots[command[0]]['high'] = -out_bin[0]-1
        out_bin = map(int,re.findall(r'low to bot (\d+)',line))
        if out_bin!=[]:
            bots[command[0]]['low'] = out_bin[0]
        out_bin = map(int,re.findall(r'high to bot (\d+)',line))
        if out_bin!=[]:
            bots[command[0]]['high'] = out_bin[0]
    bots,output = update_bots(bots,output)