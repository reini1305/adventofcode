from collections import deque
from copy import deepcopy
from typing import Deque, List, Tuple

starting_positions = [
    'RNFVLJSM',
    'PNDZFJWH',
    'WRCDG',
    'NBS',
    'MZWPCBFN',
    'PRMW',
    'RTNGLSW',
    'QTHFNBV',
    'LMHZNF'
]

stacks_init:List[Deque[str]] = [deque(x) for x in starting_positions]

# parse instructions
instructions:List[Tuple[int, int, int]] = []

with open('input5.txt') as f:
    for line in f:
        if line.startswith('move'):
            tokens = line.strip().split(' ')
            instructions.append((int(tokens[1]), int(tokens[3]), int(tokens[5])))

stacks_part1 = deepcopy(stacks_init)
stacks_part2 = deepcopy(stacks_init)
for amount, from_stack, to_stack in instructions:
    stacks_part1[to_stack-1].extend([stacks_part1[from_stack-1].pop() for _ in range(amount)])
    stacks_part2[to_stack-1].extend(reversed([stacks_part2[from_stack-1].pop() for _ in range(amount)]))

part1 = ''.join([s.pop() for s in stacks_part1])
print(f"Day 5, Part 1: {part1}")
part2 = ''.join([s.pop() for s in stacks_part2])
print(f"Day 5, Part 2: {part2}")
