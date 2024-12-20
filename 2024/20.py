import heapq
import pytest
from typing import Iterable, List, Tuple
from aoc import day, get_input, tuple_add


def parseGrid(input: List[str]) -> Tuple[List[List[str]], Tuple[int, int]]:
    grid = []
    start = (0, 0)
    for y, line in enumerate(input):
        if 'S' in line:
            start = (line.find('S'), y)
            line.replace('S', '.')
        grid.append([c for c in line])
    return grid, start


def solveMaze(
        grid: List[List[str]],
        start: Tuple[int, int]) -> Tuple[int, List[Tuple[int, int]]]:
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    candidates = [(0, start, [start])]
    visited = set()
    while candidates:
        score, pos, path = heapq.heappop(candidates)
        visited.add(pos)
        if grid[pos[1]][pos[0]] == 'E':
            return score, path
        for dir in directions:
            nx, ny = tuple_add(pos, dir)
            if grid[ny][nx] == '#' or (nx, ny) in visited:
                continue
            new_path = path.copy()
            new_path.append((nx, ny))
            heapq.heappush(candidates, (score + 1, (nx, ny), new_path))
    return -1, []


def manhattanDistance(p1: Iterable[int], p2: Iterable[int]) -> int:
    return sum(abs(pp1 - pp2) for pp1, pp2 in zip(p1, p2))


def part1(input: List[str]) -> int:
    result = 0
    result2 = 0
    grid = parseGrid(input)
    _, path = solveMaze(*grid)
    for i, p in enumerate(path[:-100]):
        difference = 99
        for q in path[i + 100:]:
            difference += 1
            distance = manhattanDistance(p, q)
            if difference - distance < 100 or distance > 20:
                continue
            result2 += 1
            if distance <= 2:
                result += 1
    print(f'Day {day()}, Part 1: {result}')
    print(f'Day {day()}, Part 2: {result2}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)


@pytest.fixture
def puzzle_input():
    return [
        '###############',
        '#...#...#.....#',
        '#.#.#.#.#.###.#',
        '#S#...#.#.#...#',
        '#######.#.#.###',
        '#######.#.#...#',
        '#######.#.###.#',
        '###..E#...#...#',
        '###.#######.###',
        '#...###...#...#',
        '#.#####.#.###.#',
        '#.#...#.#.#...#',
        '#.#.#.#.#.#.###',
        '#...#...#...###',
        '###############',
    ]


def test_day20_part1(puzzle_input):
    assert part1(puzzle_input) == 0
