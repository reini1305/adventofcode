import pytest
from typing import List, Tuple
from aoc import day, get_input
from math import prod


def getEquations(input: List[str]) -> List[Tuple[List[int], str]]:
    equations: List[Tuple[List[int], str]] = []
    numbers: List[List[int]] = []
    for line in input:
        try:
            numbers.append([int(s) for s in line.split()])
        except ValueError:
            pass
    # last line is the operants
    operants = input[-1].split()
    for idx, op in enumerate(operants):
        equations.append(([n[idx] for n in numbers], op))
    return equations


def part1(input: List[str]) -> int:
    result = 0
    for numbers, operand in getEquations(input):
        if operand == "+":
            result += sum(numbers)
        else:
            result += prod(numbers)
    print(f'Day {day()}, Part 1: {result}')
    return result


def getEquationsRTL(input: List[str]) -> List[Tuple[List[int], str]]:
    equations: List[Tuple[List[int], str]] = []
    numbers: List[int] = []
    for idx in reversed(range(len(input[0]))):
        column = "".join([i[idx] for i in input])
        try:
            numbers.append(int(column))
        except ValueError:
            try:
                numbers.append(int(column[:-1]))
            except ValueError:
                continue
            operand = column[-1]
            equations.append((numbers, operand))
            numbers = []
    return equations


def part2(input: List[str]) -> int:
    result = 0
    for numbers, operand in getEquationsRTL(input):
        if operand == "+":
            result += sum(numbers)
        else:
            result += prod(numbers)
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        "123 328  51 64 ",
        " 45 64  387 23 ",
        "  6 98  215 314",
        "*   +   *   +  ",
    ]


def test_day6_part1(puzzle_input: List[str]):
    assert part1(puzzle_input) == 4277556


def test_day6_part2(puzzle_input: List[str]):
    assert part2(puzzle_input) == 3263827
