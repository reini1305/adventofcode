from intcode import IntCode
from collections import defaultdict
from itertools import zip_longest

class IntCodeDay13(IntCode):
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
            else:
                operatormap[opcode]()
            opcode = self.memory[self.ip]
        return outval

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

if __name__ == "__main__":
    memory = defaultdict(int)
    with open('input13.txt','r') as f:
        for key,l in enumerate(f.readline().split(',')):
            memory[key] = int(l)
    interpreter = IntCodeDay13(memory)
    out = interpreter.run([])
    grid = dict()
    for group in grouper(out,3):
        x,y,i = group
        grid[(x,y)] = i
    print('Day 13, Part 1: {}'.format(sum([1 if g == 2 else 0 for g in grid.values()])))