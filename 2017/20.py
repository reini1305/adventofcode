#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 06:41:23 2017

@author: reini
"""
import numpy as np

input = [line for line in open('input20.txt')]

def get_coordinates(token):
    token = token.replace('\n','')
    return np.array([int(i) for i in token[3:-1].split(',')])

def get_distance(particle):
    return np.sum(np.abs(particle))

def get_distance_at_x(particle,i):
    x = particle['position'] + i * particle['acceleration'] + i * i * particle['acceleration']
    return get_distance(x)

particles = list()

for line in input:
    particle = dict()
    tokens = line.split(', ')
    particle['position'] = get_coordinates(tokens[0])
    particle['velocity'] = get_coordinates(tokens[1])
    particle['acceleration'] = get_coordinates(tokens[2])
    
    particles.append(particle)
    

min_distance = 1e15
closest = -1

for i, particle in enumerate(particles):
    distance = get_distance_at_x(particle,100000)
    if distance < min_distance:
        min_distance = distance
        closest = i
            
print(closest)

for particle in particles:
    particle['velocity'] += particle['acceleration']
    particle['position'] += particle['velocity']
    
# check for equality
for particle in particles:
    collisions = [(True in particle['position'] == p['position']) for p in particles]