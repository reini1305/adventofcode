from collections import deque
import pytest
from typing import Deque, List, Set, Tuple
from aoc import day, get_input, tuple_add


def get_grid(input: List[str]) -> List[List[str]]:
    # pad all around to make neighbour search easier
    output = [['.'] * (len(input[0]) + 2)]
    for line in input:
        output.append(['.'] + [char for char in line] + ['.'])
    output.append(['.'] * (len(input[0]) + 2))
    return output


def get_loop(grid: List[List[str]]) -> Tuple[Set[Tuple[int, int]], str, Tuple[int, int]]:
    # start is the 'S' character
    x = -1
    y = 0
    while x == -1:
        try:
            x = grid[y].index('S')
        except ValueError:
            pass
        y += 1
    loop = set()
    loop.add((x, y - 1))
    neighbors = {'N': ['|', '7', 'F'],
                 'S': ['|', 'L', 'J'],
                 'W': ['-', 'L', 'F'],
                 'E': ['-', 'J', '7']}
    directions = {'N': (0, -1),
                  'S': (0, 1),
                  'W': (-1, 0),
                  'E': (1, 0)}
    possible_neighbors = {'S': ['N', 'S', 'E', 'W'],
                          '|': ['N', 'S'],
                          '7': ['W', 'S'],
                          'F': ['E', 'S'],
                          'L': ['N', 'E'],
                          'J': ['N', 'W'],
                          '-': ['E', 'W']}
    to_visit: Deque[Tuple[int, int]] = deque()
    to_visit.append((x, y-1))
    matched_orientations: List[str] = []
    while to_visit:
        curr = to_visit.popleft()
        curr_val = grid[curr[1]][curr[0]]
        for orientation in possible_neighbors[curr_val]:
            test = tuple_add(curr, directions[orientation])
            test_val = grid[test[1]][test[0]]
            if test_val in neighbors[orientation] and test not in loop:
                loop.add(test)
                to_visit.append(test)
                if curr_val == 'S':
                    matched_orientations += orientation

    # Identify original tile of start tile
    start_value = 'S'
    for original in possible_neighbors:
        if original == start_value:
            continue
        if all([mo in possible_neighbors[original] for mo in matched_orientations]):
            start_value = original
            break
    return loop, start_value, (x, y - 1)


def count_inside(grid: List[List[str]], loop: Set[Tuple[int, int]]) -> int:
    Nr, Nc = len(grid), len(grid[0])
    inside = False
    corner = ""
    res = 0

    for r in range(Nr):
        for c in range(Nc):
            if (c, r) not in loop and inside:
                res += 1
            if (c, r) in loop:
                tile = grid[r][c]
                if tile in "LF":
                    corner = tile
                elif tile == "J":
                    if corner == "L":
                        pass
                    elif corner == "F":
                        inside = not inside
                    corner = ""
                elif tile == "7":
                    if corner == "L":
                        inside = not inside
                    elif corner == "F":
                        pass
                    corner = ""
                elif (tile == "-") and (corner != ""):
                    pass
                elif tile == "|":
                    inside = not inside

    return res


def part1(input: List[str]) -> int:
    result = (len(get_loop(get_grid(input))[0]) + 1) // 2
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    grid = get_grid(input)
    loop, start_val, start_coord = get_loop(grid)
    grid[start_coord[1]][start_coord[0]] = start_val
    result = count_inside(grid, loop)
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        '7-F7-',
        '.FJ|7',
        'SJLL7',
        '|F--J',
        'LJ.LJ',
    ]


def test_day10_part1(puzzle_input):
    assert part1(puzzle_input) == 8


def test_day10_part2(puzzle_input):
    assert 1
