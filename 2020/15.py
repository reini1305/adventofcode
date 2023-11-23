import pytest
from typing import List
from aoc import day
from numba import jit
from numba.errors import NumbaPendingDeprecationWarning
import warnings

warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)

@jit(nopython=True)
def get_number(input:List[int], end_t:int)->int:
    seen_numbers = [0] * end_t
    for t,i in enumerate(input[:-1]):
        seen_numbers[i] = t + 1
    last_number = input[-1]
    for t in range(len(input), end_t):
        if seen_numbers[last_number] > 0:
            new_number = t - seen_numbers[last_number]
            seen_numbers[last_number] = t
            last_number = new_number
        else:
            seen_numbers[last_number] = t
            last_number = 0
    return last_number

def part1(input: List[int])-> None:
    result = get_number(input,2020)
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[int])-> None:
    result = get_number(input,30000000)
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = [11,0,1,10,5,19]
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [0,3,6]

def test_day15_part1(puzzle_input):
    input = puzzle_input
    assert get_number(input, 2020) == 436
    assert get_number([1,3,2], 2020) == 1
    assert get_number([2,1,3], 2020) == 10
    assert get_number([1,2,3], 2020) == 27
    assert get_number([2,3,1], 2020) == 78

def test_day15_part2(puzzle_input):
    input = puzzle_input
    # assert get_number(input, 30000000) == 175594