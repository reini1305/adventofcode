import pytest
from typing import List, Dict
from aoc import day, get_input


def getGrid(input: List[str]) -> Dict[complex, str]:
    grid: Dict[complex, str] = {}
    for r, row in enumerate(input):
        for c, char in enumerate(row):
            if char == "@":
                grid[r * 1j + c] = char
    return grid


def getNumNeighbors(grid: Dict[complex, str], coordinate: complex) -> int:
    rolls = 0
    dirs = [1, -1, 1j, -1j, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j]
    for d in dirs:
        if coordinate + d in grid:
            rolls += 1
    return rolls


def part1(input: List[str]) -> int:
    result = 0
    grid = getGrid(input)
    for g in list(grid.keys()):
        if getNumNeighbors(grid, g) < 4:
            result += 1
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    removed = 1
    grid = getGrid(input)
    while removed > 0:
        removed = 0
        for g in list(grid.keys()):
            if getNumNeighbors(grid, g) < 4:
                result += 1
                removed += 1
                grid.pop(g)
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]


def test_day4_part1(puzzle_input):
    assert part1(puzzle_input) == 13


def test_day4_part2(puzzle_input):
    assert part2(puzzle_input) == 43
