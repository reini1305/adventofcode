import pytest
from typing import List

from aoc import day, get_num_input

def count_increased(input: List[int])->int:
    return sum([1 if curr > prev else 0 for curr, prev in zip(input[1:],input[:-1])])

def sum_sliding_window(input: List[int], window_size:int)->List[int]:
    return [sum(input[i:i+window_size]) for i in range(len(input) - window_size + 1)]

def part1(input: List[int])-> None:
    result = count_increased(input)
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[int])-> None:
    result = count_increased(sum_sliding_window(input,3))
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_num_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [199,200,208,210,200,207,240,269,260,263]

def test_day1_part1(puzzle_input):
    assert count_increased(puzzle_input) == 7

def test_day1_part2(puzzle_input):
    print(sum_sliding_window(puzzle_input,3))
    assert count_increased(sum_sliding_window(puzzle_input,3)) == 5