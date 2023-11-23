import pytest
from typing import List
import numpy as np
from aoc import day, get_input

def get_min_align(input:str)->int:
    crabs = np.array([int(i) for i in input.split(',')])
    i = round(np.median(crabs))
    return int(np.sum(np.abs(crabs - i)))

def get_min_align_non_linear(input:str)->int:
    crabs = np.array([int(i) for i in input.split(',')])
    start = int(np.mean(crabs))

    return min([sum([n*(n+1)//2 for n in np.abs(crabs - i)]) for i in range(start - 1, start + 2)])

def part1(input: List[str])-> None:
    result = get_min_align(input[0])
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    result = get_min_align_non_linear(input[0])
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return "16,1,2,0,4,2,7,1,2,14"

def test_day7_part1(puzzle_input):
    assert get_min_align(puzzle_input) == 37

def test_day7_part2(puzzle_input):
    assert get_min_align_non_linear(puzzle_input) == 168