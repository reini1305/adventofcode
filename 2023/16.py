from collections import deque
import pytest
from typing import List, Set, Tuple
from aoc import day, get_input


def parse_input(input: List[str]) -> List[List[str]]:
    output = []
    for line in input:
        output.append(list(line))
    return output


def get_beam(grid: List[List[str]], start: Tuple[int, int, str]) -> Set[Tuple[int, int, str]]:
    beam = set()
    directions = {'W': (-1, 0), 'E': (1, 0), 'N': (0, -1), 'S': (0, 1)}
    hit_from = {'.': {'N': ['N'], 'S': ['S'], 'E': ['E'], 'W': ['W']},
                '\\': {'N': ['W'], 'S': ['E'], 'E': ['S'], 'W': ['N']},
                '/': {'N': ['E'], 'S': ['W'], 'E': ['N'], 'W': ['S']},
                '|': {'N': ['N'], 'S': ['S'], 'E': ['N', 'S'], 'W': ['N', 'S']},
                '-': {'N': ['E', 'W'], 'S': ['E', 'W'], 'E': ['E'], 'W': ['W']}}
    to_visit = deque()
    to_visit.append(start)
    while to_visit:
        current = to_visit.popleft()
        if current in beam:
            continue
        x, y, dir = current
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
            continue
        beam.add(current)
        # look where to go next
        g = grid[y][x]
        to_go = hit_from[g][dir]
        for next_dir in to_go:
            to_visit.append((x + directions[next_dir][0], y + directions[next_dir][1], next_dir))
    return beam


def get_num_energized_tiles(grid: List[List[str]], start: Tuple[int, int, str]) -> int:
    beam = get_beam(grid, start)
    tiles = set()
    for tile in beam:
        tiles.add((tile[0], tile[1]))
    return len(tiles)


def part1(input: List[str]) -> int:
    grid = parse_input(input)
    result = get_num_energized_tiles(grid, (0, 0, 'E'))
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    grid = parse_input(input)
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if not (x == 0 or y == 0 or x == len(grid[0]) - 1 or y == len(grid) - 1):
                continue
            for direction in 'NSEW':
                result = max(result, get_num_energized_tiles(grid, (x, y, direction)))
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        '.|...\\....',
        '|.-.\\.....',
        '.....|-...',
        '........|.',
        '..........',
        '.........\\',
        '..../.\\\\..',
        '.-.-/..|..',
        '.|....-|.\\',
        '..//.|....',
    ]


def test_day16_part1(puzzle_input):
    assert part1(puzzle_input) == 46


def test_day16_part2(puzzle_input):
    assert part2(puzzle_input) == 51
