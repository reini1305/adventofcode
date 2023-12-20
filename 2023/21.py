from collections import deque
from copy import deepcopy
import re
import pytest
from typing import List, Set, Tuple
from aoc import day, get_input, tuple_add


def parse_input(input: List[str]) -> Tuple[Tuple[int, int], Set[Tuple[int, int]]]:
    start = (0, 0)
    plots = set()
    for y, line in enumerate(input):
        if 'S' in line:
            start = (line.index('S'), y)
            plots.add(start)
        for m in re.finditer(r'\.', line):
            plots.add((m.start(), y))
    return start, plots


def get_reachable(start, plots, max_steps):
    start_plots = deque()
    directions = {'N': (0, -1),
                  'S': (0, 1),
                  'W': (-1, 0),
                  'E': (1, 0)}
    start_plots.append(start)
    maxX, maxY = 0, 0
    for x, y in plots:
        maxX = max(x + 1, maxX)
        maxY = max(y + 1, maxY)
    for _ in range(1, max_steps + 1):
        reachable = set()
        while start_plots:
            current = start_plots.popleft()
            for d in directions:
                new_step = tuple_add(current, directions[d])
                if (new_step[0] % maxX, new_step[1] % maxY) in plots:
                    reachable.add(new_step)
        start_plots = deque(reachable)
    return len(reachable)


def part1(input: List[str]) -> int:
    result = get_reachable(*parse_input(input), 64)
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    # result = get_reachable(*parse_input(input), 26501365)
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
        '...........',
        '.....###.#.',
        '.###.##..#.',
        '..#.#...#..',
        '....#.#....',
        '.##..S####.',
        '.##..#...#.',
        '.......##..',
        '.##.#.####.',
        '.##..##.##.',
        '...........',
    ]


def test_day21_part1(puzzle_input):
    start, plots = parse_input(puzzle_input)
    assert get_reachable(start, plots, 6) == 16


def test_day21_part2(puzzle_input):
    assert 1
