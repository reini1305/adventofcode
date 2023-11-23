import pytest
from typing import List
from aoc import day, get_input
from collections import defaultdict

def apply_mask(value:int, mask:str)->int:
    binary_value = format(value,'036b')
    binary_masked_value = ''.join([m if m!='X' else v for m,v in zip(mask,binary_value)])
    return int(binary_masked_value, 2)

def sum_not_zero(instructions:List[str])->int:
    mem = defaultdict(int)
    mask = ''
    for instruction in instructions:
        if instruction.startswith('mask'):
            mask = instruction[-36:]
        else:
            value = int(instruction.split('=')[1])
            addr = int(instruction[instruction.index('[')+1:instruction.index(']')])
            mem[addr] = apply_mask(value,mask)
    return sum([mem[m] for m in mem])

def part1(input: List[str])-> None:
    result = sum_not_zero(input)
    print(f'Day {day()}, Part 1: {result}')

def apply_mask_v2(value:int, mask:str)->List[int]:
    binary_value = format(value,'036b')
    binary_masked_value = [m if m!='0' else v for m,v in zip(mask,binary_value)]
    num_x = binary_masked_value.count('X')
    values:List[int] = []
    for i in range(2**num_x):
        binary_i = format(i,f'0{num_x}b')
        j = 0
        masked = []
        for m in binary_masked_value:
            if m != 'X':
                masked.append(m)
            else:
                masked.append(binary_i[j])
                j+=1
        values.append(int(''.join(masked), 2))
    return values

def sum_not_zero_v2(instructions:List[str])->int:
    mem = defaultdict(int)
    mask = ''
    for instruction in instructions:
        if instruction.startswith('mask'):
            mask = instruction[-36:]
        else:
            value = int(instruction.split('=')[1])
            addr = int(instruction[instruction.index('[')+1:instruction.index(']')])
            for m in apply_mask_v2(addr, mask):
                mem[m] = value
    return sum([mem[m] for m in mem])

def part2(input: List[str])-> None:
    result = sum_not_zero_v2(input)
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input(f'input{day()}.txt')
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    instructions = ['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
                    'mem[8] = 11',
                    'mem[7] = 101',
                    'mem[8] = 0']
    return instructions

def test_day14_part1(puzzle_input):
    instructions = puzzle_input
    assert sum_not_zero(instructions) == 165

def test_day14_part2(puzzle_input):
    instructions = ['mask = 000000000000000000000000000000X1001X',
                    'mem[42] = 100',
                    'mask = 00000000000000000000000000000000X0XX',
                    'mem[26] = 1']
    assert sum_not_zero_v2(instructions) == 208