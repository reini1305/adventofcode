from intcode import IntCode
from copy import deepcopy

class IntCodeDay5(IntCode):
    def __init__(self, memory):
        IntCode.__init__(self, memory, 0)

    def run(self, user_input):
        opcode = self.memory[self.ip]
        operatormap = self.get_operatormap()
        outval = []
        input_id = 0
        while opcode != 99:
            if opcode == 3 or opcode == 203:
                operatormap[opcode](user_input[input_id])
                input_id += 1
            elif opcode == 4 or opcode == 104 or opcode == 204:
                out = operatormap[opcode]()
                outval.append(out)
            else:
                operatormap[opcode]()
            opcode = self.memory[self.ip]
        return outval[-1]

if __name__ == "__main__":
    with open('input5.txt','r') as f:
        memory = [int(l) for l in f.readline().split(',')]

    part1 = IntCodeDay5(memory)
    part2 = IntCodeDay5(memory)
    print('Day 5, Part 1: {}'.format(part1.run([1])))
    print('Day 5, Part 2: {}'.format(part2.run([5])))
    