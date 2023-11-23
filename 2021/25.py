import pytest
from typing import List, Tuple
from copy import deepcopy
from aoc import day, get_input

def get_field(input: List[str])->List[List[str]]:
    field = []
    for line in input:
        field.append([c for c in line])
    return field

def move(field:List[List[str]], steps:int)->Tuple[int,List[List[str]]]:
    rows = len(field)
    cols = len(field[0])
    for n in range(steps):
        next_field = deepcopy(field)
        stopped = False
        for y in range(rows):
            for x in range(cols):
                if field[y][x] == '>':
                    if field[y][(x+1)%cols] == '.':
                        next_field[y][(x+1)%cols] = '>'
                        next_field[y][x] = '.'
        if field == next_field:
            stopped = True
        field = next_field
        next_field = deepcopy(field)
        for y in range(rows):
            for x in range(cols):
                if field[y][x] == 'v':
                    if field[(y+1)%rows][x] == '.':
                        next_field[(y+1)%rows][x] = 'v'
                        next_field[y][x] = '.'
        if stopped and field == next_field:
            return n+1, field
        field = next_field
    return n+1, field

def part1(input: List[str])-> None:
    field = get_field(input)
    result, _ = move(field, 10_000)
    print(f'Day {day()}, Part 1: {result}')

if __name__ == "__main__":
    input = get_input()
    part1(input)

@pytest.fixture
def puzzle_input():
    return [
        "v...>>.vv>",
        ".vv>>.vv..",
        ">>.>v>...v",
        ">>v>>.>.v.",
        "v>v.vv.v..",
        ">.>>..v...",
        ".vv..>.>v.",
        "v.v..>>v.v",
        "....v..v.>",
    ]

def test_day25_part1(puzzle_input):
    field = get_field(puzzle_input)
    _, f1 = move(field,1)
    f1_gt = [
        "....>.>v.>",
        "v.v>.>v.v.",
        ">v>>..>v..",
        ">>v>v>.>.v",
        ".>v.v...v.",
        "v>>.>vvv..",
        "..v...>>..",
        "vv...>>vv.",
        ">.v.v..v.v",
    ]
    assert f1 == get_field(f1_gt)
    f30_gt = [
        ".vv.v..>>>",
        "v>...v...>",
        ">.v>.>vv.>",
        ">v>.>.>v.>",
        ".>..v.vv..",
        "..v>..>>v.",
        "....v>..>v",
        "v.v...>vv>",
        "v.v...>vvv",
    ]
    assert move(field, 30)[1] == get_field(f30_gt)
    assert move(field, 60)[0] == 58
