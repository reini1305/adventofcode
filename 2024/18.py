import heapq
import pytest
from typing import List, Set, Tuple
from aoc import day, get_input, tuple_add


def getGrid(input: List[str]) -> List[Tuple[int, int]]:
    output = []
    for line in input:
        c = line.split(',')
        output.append((int(c[0]), int(c[1])))
    return output


def solveMaze(
        grid: Set[Tuple[int, int]],
        sizex: int,
        sizey: int,
        start: Tuple[int, int],
        end: Tuple[int, int]) -> int:
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    candidates = [(0, start)]
    visited = set()
    while candidates:
        score, pos = heapq.heappop(candidates)
        visited.add(pos)
        if pos == end:
            return score
        for dir in directions:
            nx, ny = tuple_add(pos, dir)
            if nx < 0 or ny < 0 or nx >= sizex or ny >= sizey or\
               (nx, ny) in grid or (nx, ny) in visited or (score + 1, (nx, ny)) in candidates:
                continue
            heapq.heappush(candidates, (score + 1, (nx, ny)))
    return -1


def part1(input: List[str]) -> int:
    result = 0
    obstacles = getGrid(input)
    grid = set()
    grid.update(obstacles[:1024])
    result = solveMaze(grid, 71, 71, (0, 0), (70, 70))
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> str:
    result = ""
    obstacles = getGrid(input)
    lower = 0
    upper = len(obstacles)
    while upper != lower + 1:
        n = (upper + lower) // 2
        grid = set()
        grid.update(obstacles[:n])
        if solveMaze(grid, 71, 71, (0, 0), (70, 70)) < 0:
            result = f"{obstacles[n - 1][0]},{obstacles[n - 1][1]}"
            upper = n
        else:
            lower = n
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        '5,4',
        '4,2',
        '4,5',
        '3,0',
        '2,1',
        '6,3',
        '2,4',
        '1,5',
        '0,6',
        '3,3',
        '2,6',
        '5,1',
        '1,2',
        '5,5',
        '2,5',
        '6,5',
        '1,4',
        '0,4',
        '6,4',
        '1,1',
        '6,1',
        '1,0',
        '0,5',
        '1,6',
        '2,0',
    ]


def test_day18_part1(puzzle_input):
    obstacles = getGrid(puzzle_input)
    grid = set()
    for i in range(12):
        grid.add(obstacles[i])
    result = solveMaze(grid, 7, 7, (0, 0), (6, 6))
    assert result == 22


def test_day18_part2(puzzle_input):
    obstacles = getGrid(puzzle_input)
    lower = 0
    upper = len(obstacles)
    while upper != lower + 1:
        n = (upper + lower) // 2
        grid = set()
        grid.update(obstacles[:n])
        if solveMaze(grid, 7, 7, (0, 0), (6, 6)) < 0:
            result = f"{obstacles[n - 1][0]},{obstacles[n - 1][1]}"
            upper = n
        else:
            lower = n
    assert result == "6,1"
