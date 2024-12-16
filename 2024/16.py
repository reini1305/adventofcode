import heapq
import pytest
from typing import List, Tuple
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
        start: Tuple[int, int],
        max_cost: int = 200_000) -> Tuple[int, List[Tuple[int, int]]]:
    directions = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
    possible_directions = {
        'N': [('N', 1), ('E', 1001), ('W', 1001)],
        'S': [('S', 1), ('E', 1001), ('W', 1001)],
        'E': [('E', 1), ('N', 1001), ('S', 1001)],
        'W': [('W', 1), ('N', 1001), ('S', 1001)]}
    candidates = [(0, 'E', start, [start])]
    visited = set()
    while candidates:
        score, orientation, pos, path = heapq.heappop(candidates)
        if score > max_cost:
            return -1, []
        visited.add(pos)
        if grid[pos[1]][pos[0]] == 'E':
            return score, path
        for dir in possible_directions[orientation]:
            new_pos = tuple_add(pos, directions[dir[0]])
            if grid[new_pos[1]][new_pos[0]] == '#' or new_pos in visited:
                continue
            new_path = path.copy()
            new_path.append(new_pos)
            heapq.heappush(candidates, (score + dir[1], dir[0], new_pos, new_path))
    return -1, []


def part1(input: List[str]) -> int:
    result = 0
    grid, start = parseGrid(input)
    result, _ = solveMaze(grid, start)
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    grid, start = parseGrid(input)
    lowest_cost, path = solveMaze(grid, start)
    spots = set()
    for px, py in path:
        grid[py][px] = '#'
        cost, shortest_path = solveMaze(grid, start, lowest_cost)
        if cost == lowest_cost:
            spots.update(shortest_path)
        grid[py][px] = '.'
    result = len(spots)
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        '###############',
        '#.......#....E#',
        '#.#.###.#.###.#',
        '#.....#.#...#.#',
        '#.###.#####.#.#',
        '#.#.#.......#.#',
        '#.#.#####.###.#',
        '#...........#.#',
        '###.#.#####.#.#',
        '#...#.....#.#.#',
        '#.#.#.###.#.#.#',
        '#.....#...#.#.#',
        '#.###.#.#.#.#.#',
        '#S..#.....#...#',
        '###############',
    ]


def test_day16_part1(puzzle_input):
    assert part1(puzzle_input) == 7036


def test_day16_part2(puzzle_input):
    assert part2(puzzle_input) == 44
