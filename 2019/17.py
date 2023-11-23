from intcode import IntCode
from collections import defaultdict
import numpy as np

class IntCodeDay17(IntCode):
    def __init__(self, memory):
        IntCode.__init__(self, memory, 0)
        self.grid = {}
        self.cur_pos = (0,0)

    def run(self, user_input):
        opcode = self.memory[self.ip]
        operatormap = self.get_operatormap()
        while opcode != 99:
            if opcode == 3 or opcode == 203:
                operatormap[opcode](user_input)
            elif opcode == 4 or opcode == 104 or opcode == 204:
                outval = operatormap[opcode]()
                self.grid[self.cur_pos] = str(chr(outval))
                if outval == 10:
                    self.cur_pos = (0,self.cur_pos[1]+1)
                else:
                    self.cur_pos = (self.cur_pos[0]+1,self.cur_pos[1])
            else:
                operatormap[opcode]()
            opcode = self.memory[self.ip]
        return self.grid

def get_intersections(grid):
    intersections = []
    movements = {1: lambda x: (x[0],x[1]+1),
                 2: lambda x: (x[0],x[1]-1),
                 3: lambda x: (x[0]-1,x[1]),
                 4: lambda x: (x[0]+1,x[1])}
    for pos in grid:
        if grid[pos] == '#':
            all_scafold = True
            for m in movements:
                new_pos = movements[m](pos)
                all_scafold = all_scafold and new_pos in grid and (grid[new_pos] == '#')
            if all_scafold:
                intersections.append(pos)
    return intersections
    
if __name__ == "__main__":
    memory = defaultdict(int)
    with open('input17.txt','r') as f:
        for key,l in enumerate(f.readline().split(',')):
            memory[key] = int(l)

    # memory[0]=2
    interpreter = IntCodeDay17(memory)
    grid = interpreter.run(None)
    # print(''.join(list(grid.values())))
    intersections = get_intersections(grid)
    # print(intersections)
    print('Day17, Part 1: {}'.format(sum(map(lambda x: x[0]*x[1],intersections))))
