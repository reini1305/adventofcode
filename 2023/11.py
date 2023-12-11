import pytest
import re
from typing import List, Set, Tuple
from aoc import day, get_input


def get_galaxies(input: List[str]) -> List[Tuple[int, int]]:
    galaxies = []
    for y, line in enumerate(input):
        for m in re.finditer('#', line):
            galaxies.append((m.start(), y))
    return galaxies


def tuple_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def expand_universe(galaxies: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    # Get size of universe
    Nx = 0
    Ny = 0
    for g in galaxies:
        Nx = max(Nx, g[0])
        Ny = max(Ny, g[1])
    # Find empty rows / cols
    empty_rows = []
    for y in range(Ny):
        is_empty = True
        for g in galaxies:
            if g[1] == y:
                is_empty = False
                break
        if is_empty:
            empty_rows.append(y + len(empty_rows))
    empty_cols = []
    for x in range(Nx):
        is_empty = True
        for g in galaxies:
            if g[0] == x:
                is_empty = False
                break
        if is_empty:
            empty_cols.append(x + len(empty_cols))
    # Expand
    for r in empty_rows:
        for i in range(len(galaxies)):
            if galaxies[i][1] > r:
                galaxies[i] = tuple_add(galaxies[i], (0, 1))
    for c in empty_cols:
        for i in range(len(galaxies)):
            if galaxies[i][0] > c:
                galaxies[i] = tuple_add(galaxies[i], (1, 0))
    return galaxies


def part1(input: List[str]) -> int:
    result = 0
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
        '...#......',
        '.......#..',
        '#.........',
        '..........',
        '......#...',
        '.#........',
        '.........#',
        '..........',
        '.......#..',
        '#...#.....',
    ]


def test_day11_part1(puzzle_input):
    galaxies = get_galaxies(puzzle_input)
    galaxies = expand_universe(galaxies)


def test_day11_part2(puzzle_input):
    assert 1
