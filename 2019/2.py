import copy
from intcode import IntCode

with open('input2.txt','r') as f:
    memory = [int(l) for l in f.readline().split(',')]


class IntCodeDay2(IntCode):
    def __init__(self, memory, p1, p2):
        IntCode.__init__(self, memory, 0)
        self.memory[1] = p1
        self.memory[2] = p2

    def run(self):
        opcode = self.memory[self.ip]
        operatormap = self.get_operatormap()
        while opcode != 99:
            operatormap[opcode]()
            opcode = self.memory[self.ip]
        return self.memory[0]

part1 = IntCodeDay2(memory,12,2)
print("Day 2, Part 1: {}".format(part1.run()))

finished = False
for p1 in range(0,100):
    for p2 in range(0,100):
        part2 = IntCodeDay2(memory, p1, p2)
        if part2.run() == 19690720:
            print("Day 2, Part 2: {}(p1: {}, p2: {})".format(100 * p1 + p2, p1, p2))
            finished = True
            break
    if finished:
        break
