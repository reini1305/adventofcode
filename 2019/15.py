from intcode import IntCode
from collections import defaultdict,deque
from itertools import zip_longest

class IntCodeDay15(IntCode):
    def __init__(self, memory):
        IntCode.__init__(self, memory, 0)

    def run(self, user_input):
        opcode = self.memory[self.ip]
        operatormap = self.get_operatormap()
        while opcode != 99:
            if opcode == 3 or opcode == 203:
                operatormap[opcode](user_input)
            elif opcode == 4 or opcode == 104 or opcode == 204:
                return operatormap[opcode]()
            else:
                operatormap[opcode]()
            opcode = self.memory[self.ip]
        return None

def explore(visited, interpreter, cur_pos, trail):
    movements = {1: lambda x: (x[0],x[1]+1),
                 2: lambda x: (x[0],x[1]-1),
                 3: lambda x: (x[0]-1,x[1]),
                 4: lambda x: (x[0]+1,x[1])}
    opposite = {1:2, 2:1, 3:4, 4:3}

    for dir in movements:
        new_pos = movements[dir](cur_pos)
        if not new_pos in visited:
            visited[new_pos] = interpreter.run(dir)
            if visited[new_pos] == 2: # Found it!
                print('Day 15, Part 1: {}'.format(len(trail)+1))
            if visited[new_pos] == 1 or visited[new_pos] == 2:
                trail.append(dir)
                explore(visited,interpreter,new_pos, trail)
                dir = trail.pop()
                interpreter.run(opposite[dir])

def fill_up(grid,cur_pos,to_visit,level):
    movements = {1: lambda x: (x[0],x[1]+1),
                 2: lambda x: (x[0],x[1]-1),
                 3: lambda x: (x[0]-1,x[1]),
                 4: lambda x: (x[0]+1,x[1])}
    if grid[cur_pos] == 1:
        grid[cur_pos] = -level
        for dir in movements:
            new_pos = movements[dir](cur_pos)
            if new_pos in grid and grid[new_pos] == 1:
                to_visit.append((new_pos,level))
        while to_visit:
            (new_pos,new_level) = to_visit.popleft()
            fill_up(grid,new_pos,to_visit, new_level + 1)

if __name__ == "__main__":
    memory = defaultdict(int)
    with open('input15.txt','r') as f:
        for key,l in enumerate(f.readline().split(',')):
            memory[key] = int(l)
    interpreter = IntCodeDay15(memory)
    grid = {}
    cur_pos = (0,0)
    grid[cur_pos] = 1
    explore(grid,interpreter,cur_pos,[])
    to_visit=deque()
    start_pos = list(grid.keys())[list(grid.values()).index(2)]
    grid[start_pos] = 1
    fill_up(grid,start_pos,to_visit,0)
    print('Day 15, Part 2: {}'.format(-min(grid.values())))