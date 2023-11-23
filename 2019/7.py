from intcode import IntCode
from itertools import permutations

class IntCodeDay7(IntCode):
    def __init__(self, memory):
        IntCode.__init__(self, memory, 0)

    def run(self, user_input):
        opcode = self.memory[self.ip]
        operatormap = self.get_operatormap()
        input_id = 0
        while opcode != 99:
            if opcode == 3 or opcode == 203:
                operatormap[opcode](user_input[input_id])
                input_id += 1
            elif opcode == 4 or opcode == 104 or opcode == 204:
                return operatormap[opcode]()
            else:
                operatormap[opcode]()
            opcode = self.memory[self.ip]
        return None

def part1(memory):
    max_output = 0
    for sequence in permutations(range(5)):
        input = 0
        for s in sequence:
            interpreter = IntCodeDay7(memory)
            input = interpreter.run([s,input])
        if input > max_output:
            max_output = input
    return max_output

def part2(memory):
    max_output = 0
    for sequence in permutations(range(5,10)):
        input = 0
        first = True
        interpreter = [IntCodeDay7(memory) for _ in range(5,10)]
        while True:
            for i,s in enumerate(sequence):
                if first:
                    input = interpreter[i].run([s,input])
                else:
                    input = interpreter[i].run([input])
            first = False
            if input is None:
                break
            if input > max_output:
                max_output = input
    return max_output

if __name__ == "__main__":
    with open('input7.txt','r') as f:
        memory = [int(l) for l in f.readline().split(',')]

    print('Day 7, Part 1: {}'.format(part1(memory)))
    print('Day 7, Part 2: {}'.format(part2(memory)))