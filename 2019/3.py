def tupleadd(xs,ys):
     return tuple(x + y for x, y in zip(xs, ys))

def manhattanDistance(t):
    return sum([abs(i) for i in t])

def trace_wire(wire):
    grid = list()
    position = (0,0)
    delta_map = {'L':(-1,0), 'R':(1,0), 'U':(0,-1),'D':(0,1)}
    # curr_pos = 0
    for instruction in wire:
        dir = instruction[0]
        len = int(instruction[1:])
        for _ in range(len):
            position = tupleadd(position,delta_map[dir])
            grid.append(position)
    return grid

def part1(grid1,grid2):
    intersection = list(set(grid1).intersection(grid2))
    distances = [manhattanDistance(i) for i in intersection]
    return distances[distances.index(min(distances))]

def part2(grid1,grid2):
    intersection = list(set(grid1).intersection(grid2))
    distances = [grid1.index(i) + grid2.index(i) + 2 for i in intersection]
    return distances[distances.index(min(distances))]

if __name__ == "__main__":

    with open('input3.txt','r') as f:
        wires = [l.split(',') for l in f.readlines()]

    # Tests
    gt1 = trace_wire(['R75','D30','R83','U83','L12','D49','R71','U7','L72'])
    gt2 = trace_wire(['U62','R66','U55','R34','D71','R55','D58','R83'])
    assert part1(gt1,gt2) == 159
    assert part2(gt1,gt2) == 610
    gt3 = trace_wire(['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'])
    gt4 = trace_wire(['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7'])
    assert part1(gt3,gt4) == 135
    assert part2(gt3,gt4) == 410

    grid1 = trace_wire(wires[0])
    grid2 = trace_wire(wires[1])

    print('Day 3, Part 1: {}'.format(part1(grid1,grid2)))
    print('Day 3, Part 2: {}'.format(part2(grid1,grid2)))