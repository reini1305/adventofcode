import pytest
from typing import List
from aoc import day, get_input


def to_int(input: str) -> List[int]:
    return [int(i) for i in input.split()]


def extrapolate(input: List[int], left=False) -> int:
    last_val = [input[0] if left else input[-1]]
    diffs = [b - a for a, b in zip(input[:-1], input[1:])]
    last_val.insert(0, diffs[0] if left else diffs[-1])
    while not all([diff == 0 for diff in diffs]):
        diffs = [b - a for a, b in zip(diffs[:-1], diffs[1:])]
        last_val.insert(0, diffs[0] if left else diffs[-1])
    for id in range(len(last_val) - 1):
        if left:
            last_val[id + 1] -= last_val[id]
        else:
            last_val[id + 1] += last_val[id]
    return last_val[-1]


def part1(input: List[str]) -> int:
    result = 0
    for line in input:
        result += extrapolate(to_int(line))
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    for line in input:
        result += extrapolate(to_int(line), True)
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        '0 3 6 9 12 15',
        '1 3 6 10 15 21',
        '10 13 16 21 30 45',
    ]


def test_day9_part1(puzzle_input):
    assert extrapolate(to_int(puzzle_input[0])) == 18
    assert extrapolate(to_int(puzzle_input[1])) == 28
    assert extrapolate(to_int(puzzle_input[2])) == 68


def test_day9_part2(puzzle_input):
    assert extrapolate(to_int(puzzle_input[0]), True) == -3
    assert extrapolate(to_int(puzzle_input[1]), True) == 0
    assert extrapolate(to_int(puzzle_input[2]), True) == 5
