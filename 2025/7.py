from functools import cache
import pytest
from typing import List, Set, Tuple
from aoc import day, get_input


def parseGrid(input: List[str]) -> Tuple[complex, Set[complex], int]:
    start = 0j
    splitters: Set[complex] = set()
    for r, row in enumerate(input):
        for c, char in enumerate(row):
            if char == "S":
                start = r * 1j + c
            elif char == "^":
                splitters.add(r * 1j + c)
    return (start, splitters, len(input))


def traceBeam(
        start: complex,
        splitters: Set[complex],
        height: int,
        visited_splitters: Set[complex]):
    col = int(start.real)
    for row in range(int(start.imag), height):
        curr = col + row * 1j
        if curr in splitters:
            if curr in visited_splitters:
                break
            visited_splitters.add(curr)
            # continue tracing left and right of current position
            traceBeam(curr - 1, splitters, height, visited_splitters)
            traceBeam(curr + 1, splitters, height, visited_splitters)
            break


@cache
def traceTimelines(
        start: complex,
        splitters: Tuple[complex, ...],
        height: int) -> int:

    if (start.imag == height):
        return 1
    curr = start + 1j
    if curr in splitters:
        return traceTimelines(curr - 1, splitters, height) + traceTimelines(curr + 1, splitters, height)
    else:
        return traceTimelines(curr, splitters, height)


def part1(input: List[str]) -> int:
    result = 0
    visited_splitters: Set[complex] = set()
    traceBeam(*parseGrid(input), visited_splitters)
    result = len(visited_splitters)
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    start, splitters, height = parseGrid(input)
    result = traceTimelines(start, tuple(splitters), height)
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        ".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "...............",
    ]


def test_day7_part1(puzzle_input: List[str]):
    assert part1(puzzle_input) == 21


def test_day7_part2(puzzle_input: List[str]):
    assert part2(puzzle_input) == 40
