import pytest
from typing import List
import re
from itertools import permutations
from aoc import day, get_input

# [[1,2],3] becomes a list of either brackets or numbers, excluding comas:
# [ [ 1 2 ] 3 ]
def parse(line):
    return re.findall(r"\d+|[\[\]]", line)

def int_to_pair(num):
    return [str(num // 2), str(num - num//2)]

def add(a, b): 
    return ['['] + a + b + [']']

def explode(number, pos):
    def seek_digit(number, pos, direction):
        while 0 < pos < len(number)-1:
            pos += direction
            if number[pos].isdigit(): 
                return pos
        return None
    a,b = int(number[pos]), int(number[pos+1])
    l_pos = seek_digit(number, pos, -1)
    r_pos = seek_digit(number, pos+1, +1)
    if l_pos: 
        number[l_pos] = str(a + int(number[l_pos]))
    if r_pos: 
        number[r_pos] = str(b + int(number[r_pos]))
    return number[0:pos-1] + ['0'] + number[pos+3:]

def split(number, pos):
    return number[0:pos] + ['['] + int_to_pair(int(number[pos])) + [']'] + number[pos+1:]

def reduce_step(number):
    depth = 0
    for pos in range(len(number)):
        if number[pos] == "[": 
            depth += 1
        elif number[pos] == "]": 
            depth -= 1
        elif depth == 5: 
            return explode(number, pos)

    for pos in range(len(number)):
        if number[pos].isdigit() and int(number[pos]) >= 10: 
            return split(number, pos)
    raise EOFError

def reduce_fully(number):
    while True:
        try: 
            number = reduce_step(number)
        except EOFError: 
            break
    return number

def add_list(numbers):
    result = numbers.pop(0)
    for i in numbers:
        result = reduce_fully(add(result, i))
    return(result)

def magnitude(number):
    def p(number):
        for i in range(len(number)-1):
            if number[i].isdigit() and number[i+1].isdigit():
                return number[0:i-1] + [str(int(number[i]) * 3 + int(number[i+1]) * 2)] + number[i+3:]
        raise EOFError
    while True:
        try: number = p(number)
        except EOFError: 
            break
    return int(number[0])

def part1(input: List[str])-> None:
    numbers = [parse(line) for line in input]
    result = magnitude(add_list(numbers))
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    result = 0
    numbers = [parse(line) for line in input]
    for a, b in permutations(numbers, 2):
        val = magnitude(add_list([a, b]))
        result = max(result, val)
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        '[[[[[9,8],1],2],3],4]',
        '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'
    ]

def test_day18_part1(puzzle_input):
    number = parse(puzzle_input[0])
    number = reduce_step(number)
    assert ''.join(number) == '[[[[09]2]3]4]'
    number = parse(puzzle_input[1])
    number = reduce_step(number)
    assert ''.join(number) =='[[3[2[80]]][9[5[4[32]]]]]'

def test_day18_part2(puzzle_input):
    assert 1