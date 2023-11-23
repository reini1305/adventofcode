from intcode import IntCode
from collections import defaultdict
import numpy as np

class IntCodeDay11(IntCode):
    def __init__(self, memory):
        IntCode.__init__(self, memory, 0)

    def run(self, user_input):
        opcode = self.memory[self.ip]
        operatormap = self.get_operatormap()
        input_id = 0
        outval = []
        while opcode != 99:
            if opcode == 3 or opcode == 203:
                operatormap[opcode](user_input[input_id])
                input_id += 1
            elif opcode == 4 or opcode == 104 or opcode == 204:
                out = operatormap[opcode]()
                outval.append(out)
                if len(outval) == 2:
                    break
            else:
                operatormap[opcode]()
            opcode = self.memory[self.ip]
        return outval

def turn_left(dir):
    return (-dir[1],dir[0])

def turn_right(dir):
    return (dir[1],-dir[0])

def part1(memory):
    interpreter = IntCodeDay11(memory)
    grid = defaultdict(int)
    turn_map = {0: turn_left, 1: turn_right}
    dir = (0,1)
    pos = (0,0)
    while True:
        next = interpreter.run([grid[pos]])
        if not next:
            break
        grid[pos] = next[0]
        dir = turn_map[next[1]](dir)
        pos = (dir[0]+pos[0],dir[1]+pos[1])
    return len(grid.keys())

def part2(memory):
    interpreter = IntCodeDay11(memory)
    grid = defaultdict(int)
    turn_map = {0: turn_left, 1: turn_right}
    dir = (0,1)
    pos = (0,0)
    grid[pos] = 1
    while True:
        next = interpreter.run([grid[pos]])
        if not next:
            break
        grid[pos] = next[0]
        dir = turn_map[next[1]](dir)
        pos = (dir[0]+pos[0],dir[1]+pos[1])

    out = np.zeros((6,48))
    for pixel in grid:
        x, y = pixel
        out[-y,x] = grid[pixel]
    return out

if __name__ == "__main__":
    memory = defaultdict(int)
    with open('input11.txt','r') as f:
        for key,l in enumerate(f.readline().split(',')):
            memory[key] = int(l)
    
    print('Day 11, Part 1: {}'.format(part1(memory)))
    out = part2(memory)
    np.set_printoptions(linewidth = 130, formatter={'all':lambda x: ' ' if x==0 else '*'})
    print('Day 11, Part 2: \n{}'.format(out))