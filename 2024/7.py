import pytest
from typing import Callable, List, Tuple
from aoc import day, get_input
from operator import add, mul


def parseInput(input: List[str]) -> List[Tuple[int, List[int]]]:
    equations = []
    for line in input:
        result, inputs = line.split(':')
        equations.append((int(result), list(map(int, inputs.split()))))
    return equations


def isSolvable(equations: Tuple[int, List[int]], input_ops: List[Callable]) -> bool:
    target, equation = equations
    all_results = [equation[0]]

    for i in range(1, len(equation)):
        possible_results = []
        for prev_result in all_results:
            for op in input_ops:
                result = op(prev_result, equation[i])
                if result <= target:
                    possible_results.append(result)
        all_results = possible_results

    return target in all_results


def part1(input: List[str]) -> int:
    result = 0
    equations = parseInput(input)
    for equation in equations:
        if isSolvable(equation, [add, mul]):
            result += equation[0]
    print(f'Day {day()}, Part 1: {result}')
    return result


def concat(a, b):
    return int(f"{a}{b}")


def part2(input: List[str]) -> int:
    result = 0
    equations = parseInput(input)
    for equation in equations:
        if isSolvable(equation, [add, mul, concat]):
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
