#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 06:46:53 2017

@author: reini
"""

firewall = dict()
#position = dict()

with open('input13.txt') as infile:
    for line in infile:
        tokens = line.split(': ')
        firewall[int(tokens[0])] = int(tokens[1])
#        position[int(tokens[0])] = 0
  

def getPosition(time,num_entries):
    return time % (2 * (num_entries - 1)) 
    
def calcCost(firewall, delay, withZero = True):
    cost = 0      
    # check each firewall layer
    for curr_layer in sorted(firewall.keys()):
        # calculate current position of scanner      
        if getPosition(delay + curr_layer,firewall[curr_layer]) == 0:
            cost += curr_layer * firewall[curr_layer]
            if not withZero and curr_layer == 0:
                cost += 1
    return cost
        
print (calcCost(firewall,0))

delay = 0
while calcCost(firewall,delay,False) > 0:
    delay += 1
print (delay)