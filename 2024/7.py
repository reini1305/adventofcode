import pytest
from typing import List, Tuple
from aoc import day, get_input
from itertools import product
from operator import add, mul


def parseInput(input: List[str]) -> List[Tuple[int, List[int]]]:
    equations = []
    for line in input:
        result, inputs = line.split(':')
        equations.append((int(result), list(map(int, inputs.split()))))
    return equations


def isSolvable(equation: Tuple[int, List[int]]) -> bool:
    result, inputs = equation
    operators = product([add, mul], repeat=len(inputs) - 1)

    for operator in operators:
        result_is = inputs[0]
        for a, o in zip(inputs[1:], operator):
            result_is = o(result_is, a)
            if result_is > result:
                break
        if result_is == result:
            return True

    return False


def isSolvable2(equation: Tuple[int, List[int]]) -> bool:
    result, inputs = equation

    def concat(a, b):
        return int(str(a) + str(b))
    operators = product([add, mul, concat], repeat=len(inputs) - 1)

    for operator in operators:
        result_is = inputs[0]
        for a, o in zip(inputs[1:], operator):
            result_is = o(result_is, a)
            if result_is > result:
                break
        if result_is == result:
            return True

    return False


def part1(input: List[str]) -> int:
    result = 0
    equations = parseInput(input)
    for equation in equations:
        if isSolvable(equation):
            result += equation[0]
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    equations = parseInput(input)
    for equation in equations:
        if isSolvable2(equation):
            result += equation[0]
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        '190: 10 19',
        '3267: 81 40 27',
        '83: 17 5',
        '156: 15 6',
        '7290: 6 8 6 15',
        '161011: 16 10 13',
        '192: 17 8 14',
        '21037: 9 7 18 13',
        '292: 11 6 16 20',
    ]


def test_day7_part1(puzzle_input):
    equations = parseInput(puzzle_input)
    assert equations[0][0] == 190
    assert part1(puzzle_input) == 3749


def test_day7_part2(puzzle_input):
    assert part2(puzzle_input) == 11387
