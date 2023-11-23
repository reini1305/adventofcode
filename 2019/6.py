
def path_length(data,start):
    if start in data:
        return 1 + path_length(data,data[start])
    else:
        return 1

if __name__ == "__main__":
    with open('input6.txt','r') as f:
        input = [line.strip().split(')') for line in f.readlines()]

    orbits = dict()
    for i in input:
        orbits[i[1]] = i[0]
    total_length = 0
    for k in orbits.keys():
        total_length += path_length(orbits,orbits[k])
    print('Day 6, Part 1: {}'.format(total_length))
    
    you_orbit = 'YOU'
    san_orbit = 'SAN'

    you_orbits = []
    san_orbits = []

    while you_orbit in orbits:
        you_orbits.append(orbits[you_orbit])
        you_orbit = orbits[you_orbit]

    while san_orbit in orbits:
        san_orbits.append(orbits[san_orbit])
        san_orbit = orbits[san_orbit]

    transfer_count = min([you_orbits.index(orbit) + san_orbits.index(orbit) for orbit in set(you_orbits) & set(san_orbits)])
    print('Day 6, Part 2: {}'.format(transfer_count))

