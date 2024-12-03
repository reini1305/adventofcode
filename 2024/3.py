import pytest
from typing import List, Tuple
from aoc import day, get_input
import re


def parseMul(instruction: str) -> Tuple[int, int]:
    left = int(instruction.split('(')[1].split(',')[0])
    right = int(instruction.split(',')[1][:-1])
    return left, right


def part1(input: List[str]) -> int:
    regex = r"mul\(\d+,\d+\)"

    result = 0
    for line in input:
        matches = re.finditer(regex, line, re.MULTILINE)
        for match in matches:
            instruction = match.group()
            left, right = parseMul(instruction)
            result += left * right
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    regex = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

    result = 0
    enabled = True
    for line in input:
        matches = re.finditer(regex, line, re.MULTILINE)
        for match in matches:
            instruction = match.group()
            if instruction.startswith("don't"):
                enabled = False
            elif instruction.startswith("do"):
                enabled = True
            elif enabled:
                left, right = parseMul(instruction)
                result += left * right
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]


def test_day3_part1(puzzle_input):
    assert part1(puzzle_input) == 161


def test_day3_part2(puzzle_input):
    puzzle_input = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
    assert part2(puzzle_input) == 48
