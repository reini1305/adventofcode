import pytest
from typing import List, Tuple
from aoc import day, get_input
import numpy as np


def get_patterns(input: List[str]) -> List[np.array]:
    output = []
    curr_pattern: List[List[int]] = []
    to_int = {'#': 1, '.': 0}
    for line in input:
        if line == '':
            output.append(np.array(curr_pattern))
            curr_pattern = []
        else:
            curr_pattern.append([to_int[c] for c in line])
    output.append(np.array(curr_pattern))
    return output


def get_reflections(matrix: np.array) -> Tuple[int, int]:
    for col in range(matrix.shape[1] - 1):
        c = col
        reflection = True
        while c >= 0:
            if col + 1 + (col - c) >= matrix.shape[1]:
                break
            if sum(matrix[:, c] == matrix[:, col + 1 + (col - c)]) != matrix.shape[0]:
                reflection = False
                break
            c -= 1
        if reflection:
            return col + 1, 0
    for row in range(matrix.shape[0] - 1):
        r = row
        reflection = True
        while r >= 0:
            if row + 1 + (row - r) >= matrix.shape[0]:
                break
            if sum(matrix[r, :] == matrix[row + 1 + (row - r), :]) != matrix.shape[1]:
                reflection = False
                break
            r -= 1
        if reflection:
            return 0, row + 1
    return 0, 0


def part1(input: List[str]) -> int:
    patterns = get_patterns(input)
    result = 0
    for pattern in patterns:
        h, v = get_reflections(pattern)
        result += h + 100 * v
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        '#.##..##.',
        '..#.##.#.',
        '##......#',
        '##......#',
        '..#.##.#.',
        '..##..##.',
        '#.#.##.#.',
        '',
        '#...##..#',
        '#....#..#',
        '..##..###',
        '#####.##.',
        '#####.##.',
        '..##..###',
        '#....#..#',
    ]


def test_day13_part1(puzzle_input):
    patterns = get_patterns(puzzle_input)
    assert len(patterns) == 2
    assert get_reflections(patterns[0]) == (5, 0)
    assert get_reflections(patterns[1]) == (0, 4)
    assert part1(puzzle_input) == 405


def test_day13_part2(puzzle_input):
    assert 1
