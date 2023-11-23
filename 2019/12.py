import numpy as np
from itertools import combinations
from sympy import lcm
from copy import deepcopy

def part1(planets,iterations = 1000):
    velocities = planets * 0
    for i in range(iterations):
        for p in combinations(range(4),2):
            diff = planets[p[0],:] - planets[p[1],:]
            v_diff = np.array([1 if d > 0 else -1 if d < 0 else 0 for d in diff])
            velocities[p[0],:] -= v_diff
            velocities[p[1],:] += v_diff

        planets += velocities
    return np.sum(np.sum(np.abs(planets),axis=1) * np.sum(np.abs(velocities),axis=1))

def part2(planets):
    velocities = planets * 0
    unique_x, unique_y, unique_z = set(), set(), set()
    add_x, add_y, add_z = True, True, True
    while add_x or add_y or add_z:
        x, y, z = [v.tobytes()+p for v,p in zip(velocities.T,[p.tobytes() for p in planets.T])]
        for p in combinations(range(4),2):
            diff = planets[p[0],:] - planets[p[1],:]
            v_diff = np.array([1 if d > 0 else -1 if d < 0 else 0 for d in diff])
            velocities[p[0],:] -= v_diff
            velocities[p[1],:] += v_diff
        planets += velocities
        if add_x and x not in unique_x:
            unique_x.add(x)
        else:
            add_x = False
        if add_y and y not in unique_y:
            unique_y.add(y)
        else:
            add_y = False
        if add_z and z not in unique_z:
            unique_z.add(z)
        else:
            add_z = False
    return lcm([len(unique_x),len(unique_y),len(unique_z)])

if __name__ == "__main__":
    assert part1(np.array([[-1,0,2],[2,-10,-7],[4,-8,8],[3,5,-1]]),10) == 179
    assert part1(np.array([[-8,-10,0],[5,5,10],[2,-7,3],[9,-8,-3]]),100) == 1940
    assert part2(np.array([[-1,0,2],[2,-10,-7],[4,-8,8],[3,5,-1]])) == 2772
    assert part2(np.array([[-8,-10,0],[5,5,10],[2,-7,3],[9,-8,-3]])) == 4686774924
    
    planets = np.array(
        [[14,2,8],
        [7,4,10],
        [1,17,16],
        [-4,-1,1]])
    print('Day 12, Part 1: {}'.format(part1(deepcopy(planets))))
    print('Day 12, Part 2: {}'.format(part2(planets)))