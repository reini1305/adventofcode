from intcode import IntCode
from collections import defaultdict

class IntCodeDay9(IntCode):
    def __init__(self, memory, user_input):
        IntCode.__init__(self, memory, 0)
        self.user_input = user_input
        self.input_id = 0

    def run(self):
        opcode = self.memory[self.ip]
        operatormap = self.get_operatormap()
        outval = None
        while opcode != 99:
            if opcode == 3 or opcode == 203:
                operatormap[opcode](self.user_input[self.input_id])
                self.input_id += 1
            elif opcode == 4 or opcode == 104 or opcode == 204:
                outval = operatormap[opcode]()
            else:
                operatormap[opcode]()
            opcode = self.memory[self.ip]
        return outval

if __name__ == "__main__":
    memory = defaultdict(int)
    with open('input9.txt','r') as f:
        for key,l in enumerate(f.readline().split(',')):
            memory[key] = int(l)

    part1 = IntCodeDay9(memory,[1])
    part2 = IntCodeDay9(memory,[2])
    print('Day 9, Part 1: {}'.format(part1.run()))
    print('Day 9, Part 2: {}'.format(part2.run()))