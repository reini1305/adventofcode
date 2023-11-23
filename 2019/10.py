import numpy as np

def getDiffs(asteroid,asteroids):
    diffs = dict()
    for a in asteroids:
        diff = np.subtract(a,asteroid)
        norm = np.linalg.norm(diff)
        if norm < 1e-3: # a == asteroid
            continue
        diff = np.around(np.divide(diff,norm),5)
        key = (diff[0],diff[1])
        if key in diffs:
            if diffs[key][0] > norm:
                diffs[key] = (norm,a)
        else:
            diffs[key] = (norm,a)
    return diffs   

def getAngle(vector):
    up = np.array([0,-1])
    ang1 = np.arctan2(*up[::-1])
    ang2 = np.arctan2(*vector[::-1])
    return  ((ang2 - ang1) % (2 * np.pi))

if __name__ == "__main__":
    
    asteroids = list()
    with open('input10.txt','r') as f:
        y = 0
        for line in f:
            x = 0
            for c in line:
                if c == '#':
                    asteroids.append(np.array([x,y]))
                x += 1
            y += 1


    max_diffs = 0
    max_station = None
    for asteroid in asteroids:
        diffs = getDiffs(asteroid,asteroids)
        if len(diffs) > max_diffs:
            max_diffs = len(diffs)
            max_station = asteroid

    print('Day 10, Part 1: {}'.format(max_diffs))

    num_killed = 0
    max_stations = getDiffs(max_station,asteroids)
    last_killed_station = None
    while num_killed < 200:
        closest_station = min(max_stations,key = lambda x: getAngle(x))
        last_killed_station = max_stations[closest_station][1]
        del max_stations[closest_station]
        num_killed += 1
    print('Day 10, Part 2: {}'.format(last_killed_station[0]*100 + last_killed_station[1]))
