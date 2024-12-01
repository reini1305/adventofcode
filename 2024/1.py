import pytest
from typing import List, Tuple
from aoc import day, get_input


def getLists(input: List[str]) -> Tuple[List[int], List[int]]:
    left: List[int] = []
    right: List[int] = []
    for line in input:
        l, r = line.split('   ')
        left.append(int(l))
        right.append(int(r))
    return left, right


def part1(input: List[str]) -> int:
    result = 0
    left, right = getLists(input)
    for le, ri in zip(sorted(left), sorted(right)):
        result += abs(le-ri)
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    left, right = getLists(input)
    result = sum([le * right.count(le) for le in left])
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3",
    ]


def test_day1_part1(puzzle_input):
    l, r = getLists(puzzle_input)
    assert l[0] == 3
    assert r[0] == 4
    assert part1(puzzle_input) == 11


def test_day1_part2(puzzle_input):
    assert part2(puzzle_input) == 31
