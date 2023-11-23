import pytest
from typing import List, Tuple
from aoc import day, get_input

def coordinates_after_moves(input: List[str])->Tuple[int,int]:
    dir = {'N':(0,1), 'S':(0,-1), 'W':(-1,0), 'E':(1,0)}
    transition = {('E','R'):'S',
                  ('E','L'):'N',
                  ('W','R'):'N',
                  ('W','L'):'S',
                  ('N','R'):'E',
                  ('N','L'):'W',
                  ('S','R'):'W',
                  ('S','L'):'E'}
    orientation = 'E'
    x = 0
    y = 0
    for instruction in input:
        i = instruction[0]
        val = int(instruction[1:])
        if i in dir:
            x += dir[i][0] * val
            y += dir[i][1] * val
        elif i == 'F':
            x += dir[orientation][0] * val
            y += dir[orientation][1] * val
        else:
            for _ in range(val//90):
                orientation = transition[(orientation,i)]
    return (x,y)

def part1(input: List[str])-> None:
    result = coordinates_after_moves(input)
    print(f'Day {day()}, Part 1: {abs(result[0])+abs(result[1])}')

def coordinates_after_moves2(input: List[str])->Tuple[int,int]:
    dir = {'N':(0,1), 'S':(0,-1), 'W':(-1,0), 'E':(1,0)}
    transition = lambda wx,wy,o:(wy,-wx) if o=='R' else (-wy,wx)
    x = 0
    y = 0
    wx = 10
    wy = 1
    for instruction in input:
        i = instruction[0]
        val = int(instruction[1:])
        if i in dir:
            wx += dir[i][0] * val
            wy += dir[i][1] * val
        elif i == 'F':
            x += wx * val
            y += wy * val
        else:
            for _ in range(val//90):
                wx,wy  = transition(wx,wy,i)
    return (x,y)

def part2(input: List[str])-> None:
    result = coordinates_after_moves2(input)
    print(f'Day {day()}, Part 2: {abs(result[0])+abs(result[1])}')

if __name__ == "__main__":
    input = get_input(f'input{day()}.txt')
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    instructions = ['F10',
                    'N3',
                    'F7',
                    'R90',
                    'F11']
    return instructions

def test_day12_part1(puzzle_input):
    input = puzzle_input
    assert coordinates_after_moves(input) == (17,-8)

def test_day12_part2(puzzle_input):
    input = puzzle_input
    assert coordinates_after_moves2(input) == (214,-72)