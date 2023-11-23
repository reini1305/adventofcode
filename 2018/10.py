import re
import numpy as np
import sys

input = [line for line in open('input10','r')]
lines = [[int(i) for i in re.findall(r'-?\d+', l)] for l in input]
positions = [(x[0],x[1]) for x in lines]
velocities = [(x[2],x[3]) for x in lines]

def getPositions(p,v,t):
    return [( pos[0] + vel[0]*t, pos[1] + vel[1]*t ) for pos,vel in zip(p,v)]

def getSize(p):
    size_x = max([pos[0] for pos in p]) - min([pos[0] for pos in p]) 
    size_y = max([pos[1] for pos in p]) - min([pos[1] for pos in p]) 
    return size_x * size_y

def printGrid(p):
    max_x = max([pos[0] for pos in p])
    min_x = min([pos[0] for pos in p]) 
    max_y = max([pos[1] for pos in p])
    min_y = min([pos[1] for pos in p]) 

    for y in np.arange(min_y,max_y+1):
        for x in np.arange(min_x,max_x+1):
            if (x,y) in p:
                sys.stdout.write('#')
            else:
                sys.stdout.write(' ')
        print('')

t = 0
min_size = 1e20
while True:
    curr_size = getSize(getPositions(positions,velocities,t))
    if curr_size > min_size:
        break
    min_size = curr_size
    t += 1
t -= 1

printGrid(getPositions(positions,velocities,t))
print(t)
