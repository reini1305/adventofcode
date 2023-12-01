import pytest
from typing import List
from aoc import day, get_input


def part1(input: List[str]) -> None:
    result = 0
    print(f'Day {day()}, Part 1: {result}')


def part2(input: List[str]) -> None:
    result = 0
    print(f'Day {day()}, Part 2: {result}')


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return True


def test_dayx_part1(puzzle_input):
    assert 1


def test_dayx_part2(puzzle_input):
    assert 1
