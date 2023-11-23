#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 07:33:19 2018

@author: christian
"""

from collections import defaultdict

with open('input8.txt','r') as file:
    input = [int(x) for x in file.read().split()]

nodes = defaultdict(list)
children = defaultdict(list)

def parseNode(node_id):
    global input
    global nodes
    global children
    num_childs = input[0]
    num_metadata = input[1]
    del input[0:2]
    new_node_id=node_id
    for x in range(num_childs):
        children[node_id].append(parseNode(new_node_id+1))
        new_node_id = children[node_id][-1]
    for x in range(num_metadata):
        nodes[node_id].append(input[0])
        del input[0]
    return new_node_id

parseNode(0)

# Count metadata
print(sum([sum(x) for x in nodes.values()]))

acc = 0
def create_tree(L):    
    global acc
    nchild = L[0]    
    len_meta = L[1]      

    if nchild == 0:        
        metadata = L[2:2+len_meta]        
        acc+= sum(metadata)
        return {'children':[], 'metadata':metadata, 'val':sum(metadata)}, L[2+len_meta:]
    children = []
    L = L[2:]
    for _ in range(nchild):
        c, L = create_tree(L)
        children.append(c)
    metadata = L[:len_meta]
    acc += sum(metadata)
    val = sum(children[i-1]['val'] for i in metadata  if 0<i<=len(children))
    return {'children':children, 'metadata': L[:len_meta], 'val':val}, L[len_meta:]
with open('input8.txt','r') as file:
    input = [int(x) for x in file.read().split()]
tree = create_tree(input)
    
#Part 1
print(acc)

#Part2
val = tree[0]['val']
print(val)