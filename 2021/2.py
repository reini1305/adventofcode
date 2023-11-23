import pytest
from typing import List, Tuple
from aoc import day, get_input

def move(input: List[str])->Tuple[int,int]:
    horiz, depth = (0, 0)
    for line in input:
        value = int(line.split(" ")[1])
        if line.startswith("f"):
            horiz += value
        elif line.startswith("u"):
            depth -= value
        elif line.startswith("d"):
            depth += value
    return (horiz, depth)

def move_advanced(input: List[str])->Tuple[int,int]:
    horiz, depth, aim = (0, 0, 0)
    for line in input:
        value = int(line.split(" ")[1])
        if line.startswith("f"):
            horiz += value
            depth += aim * value
        elif line.startswith("u"):
            aim -= value
        elif line.startswith("d"):
            aim += value
    return (horiz, depth)

def part1(input: List[str])-> None:
    position = move(input)
    result = position[0] * position[1]
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    position = move_advanced(input)
    result = position[0] * position[1]
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return ["forward 5","down 5","forward 8","up 3","down 8","forward 2"]

def test_day2_part1(puzzle_input):
    position = move(puzzle_input)
    assert position[0] * position[1] == 150

def test_day2_part2(puzzle_input):
    position = move_advanced(puzzle_input)
    assert position[0] * position[1] == 900