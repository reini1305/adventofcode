import pytest
from typing import List
from aoc import day, get_input

def run(instructions, input):
    regs = {'x':0, 'y':0, 'z':0, 'w':0}
    curr_input = 0
    for line in instructions:
        op, out, *var = line.split()
        if op == 'inp':
            regs[out] = int(input[curr_input])
            curr_input += 1
        elif op == 'add':
            regs[out] += regs[var[0]] if var[0] in regs else int(var[0])
        elif op == 'mul':
            regs[out] *= regs[var[0]] if var[0] in regs else int(var[0])
        elif op == 'div':
            regs[out] //= regs[var[0]] if var[0] in regs else int(var[0])
        elif op == 'mod':
            regs[out] %= regs[var[0]] if var[0] in regs else int(var[0])
        elif op == 'eql':
            v = regs[var[0]] if var[0] in regs else int(var[0])
            regs[out] = 1 if regs[out] == v else 0
    return regs

def get_rules(x_add, w_add, z_div):
    stack = [0]
    rules = {}
    for i in range(1,len(z_div)):
        if z_div[i] == 26:
            match = stack.pop()
            rules[match] = (i, -x_add[i] - w_add[match])
        else:
            stack.append(i)
    return rules

x_add = [11, 14, 13, -4, 11, 10, -4, -12, 10, -11, 12, -1,  0, -11]
w_add = [ 3,  7,  1,  6, 14,  7,  9,   9,  6,   4,  0,  7, 12, 1]
z_div = [ 1,  1,  1, 26,   1, 1, 26,  26,  1,  26,  1, 26, 26, 26]

def get_max_num(rules, length):
    number = ['9'] * length
    for pos in rules:
        match, offset = rules[pos]
        if offset > 0:
            number[match] = str(9-offset)
        else:
            number[pos] = str(9+offset)
        pass
    return ''.join(number)

def get_min_num(rules, length):
    number = ['1'] * length
    for pos in rules:
        match, offset = rules[pos]
        if offset > 0:
            number[pos] = str(1+offset)
        else:
            number[match] = str(1-offset)
        pass
    return ''.join(number)

def part1(input:List[str])-> None:
    rules = get_rules(x_add, w_add, z_div)
    result = get_max_num(rules, 14)
    regs = run(input, result)
    assert regs['z'] == 0
    print(f'Day {day()}, Part 1: {result}')

def part2(input:List[str])-> None:
    rules = get_rules(x_add, w_add, z_div)
    result = get_min_num(rules, 14)
    regs = run(input, result)
    assert regs['z'] == 0
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        "inp w",
        "mul x 0",
        "add x z",
        "mod x 26",
        "div z 1",
        "add x 11",
        "eql x w",
        "eql x 0",
        "mul y 0",
        "add y 25",
        "mul y x",
        "add y 1",
        "mul z y",
        "mul y 0",
        "add y w",
        "add y 3",
        "mul y x",
        "add z y",
    ]

def test_day24_part1(puzzle_input):
    regs = run(puzzle_input, '8')
    assert regs['z'] == 11
