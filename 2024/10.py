import pytest
from typing import List, Set, Tuple
from aoc import day, get_input, tuple_add


def getGrid(input: List[str]) -> List[List[int]]:
    out = []
    for line in input:
        out.append([int(c) for c in line])
    return out


def getTrailHeadGoals(grid: List[List[int]], start: Tuple[int, int]) -> Set[Tuple[int, int]]:
    candidates = []
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    cur_val = grid[start[1]][start[0]]
    if cur_val == 9:
        return {start}
    for d in directions:
        nx, ny = tuple_add(start, d)
        if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid) or grid[ny][nx] != cur_val + 1:
            continue
        candidates.append((nx, ny))

    trail_goals: Set[Tuple[int, int]] = set()
    for c in candidates:
        trail_goals = trail_goals | getTrailHeadGoals(grid, c)
    return trail_goals


def getTrailHeadCounts(grid: List[List[int]], start: Tuple[int, int]) -> int:
    candidates = []
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    cur_val = grid[start[1]][start[0]]
    if cur_val == 9:
        return 1
    for d in directions:
        nx, ny = tuple_add(start, d)
        if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid) or grid[ny][nx] != cur_val + 1:
            continue
        candidates.append((nx, ny))

    return sum([getTrailHeadCounts(grid, c) for c in candidates])


def part1(input: List[str]) -> int:
    result = 0
    grid = getGrid(input)
    for y in range(len(input)):
        for x in range(len(input[0])):
            if grid[y][x] == 0:
                result += len(getTrailHeadGoals(grid, (x, y)))

    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    grid = getGrid(input)
    for y in range(len(input)):
        for x in range(len(input[0])):
            if grid[y][x] == 0:
                result += getTrailHeadCounts(grid, (x, y))
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        '89010123',
        '78121874',
        '87430965',
        '96549874',
        '45678903',
        '32019012',
        '01329801',
        '10456732',
    ]


def test_day10_part1(puzzle_input):
    assert part1(puzzle_input) == 36


def test_day10_part2(puzzle_input):
    assert part2(puzzle_input) == 81
