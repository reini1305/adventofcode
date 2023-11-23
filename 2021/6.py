import pytest
from typing import List
import numpy as np
from aoc import day, get_input

def parse_input(input: str)-> List[int]:
    return [int(n) for n in input.split(',')]

def calculate(input: List[int], rounds: int) -> int:
    days = [0] * 9
    for day in input:
        days[day] += 1

    for _ in range(rounds):
        births = days.pop(0)
        days[6] += births
        days.append(births)
    return sum(days)

def part1(input: List[str])-> None:
    result = calculate(parse_input(input[0]), 80)
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    result = calculate(parse_input(input[0]), 256)
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return "3,4,3,1,2"

def test_day6_part1(puzzle_input):
    assert len(parse_input(puzzle_input)) == 5
    assert calculate(parse_input(puzzle_input), 18) == 26
    assert calculate(parse_input(puzzle_input), 80) == 5934

def test_day6_part2(puzzle_input):
    input = parse_input(puzzle_input)
    assert calculate(parse_input(puzzle_input), 18) == 26