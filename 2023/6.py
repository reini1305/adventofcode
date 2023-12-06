import pytest
from typing import List, Tuple
from aoc import day


def count_ways_to_win(time: int, distance: int) -> int:
    distances = [(time - t) * t for t in range(time + 1)]
    return sum([d > distance for d in distances])


def part1(input: List[Tuple[int, int]]) -> int:
    result = 1
    for race in input:
        result *= count_ways_to_win(*race)
    print(f'Day {day()}, Part 1: {result}')
    return result


if __name__ == "__main__":
    input = [(52, 426), (94, 1374), (75, 1279), (94, 1216)]
    part1(input)
    input = [(52947594, 426137412791216)]
    part1(input)


@pytest.fixture
def puzzle_input():
    return [
        (7, 9), (15, 40), (30, 200)
    ]


def test_day6_part1(puzzle_input):
    assert count_ways_to_win(*puzzle_input[0]) == 4
    assert count_ways_to_win(*puzzle_input[1]) == 8
    assert count_ways_to_win(*puzzle_input[2]) == 9
    assert part1(puzzle_input) == 288
