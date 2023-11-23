from collections import deque
import pytest
from typing import List
from aoc import day, get_input

def create_grid(input: List[str])-> List[List[int]]:
    costs = {chr(key): value for key,value in zip(range(97, 123), range(1,27))}
    costs['S'] = 1
    costs['E'] = 26
    grid:List[List[int]] = []
    for line in input:
        grid.append([costs[c] for c in line.strip()])
    return grid

def tuple_add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def grid_solve(grid, start, end):
    width = len(grid[0])
    height = len(grid)
    visited = set([start])
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    path_list = [[start]]
    path_index = 0
    while path_index < len(path_list):
        current_path = path_list[path_index]
        curr = current_path[-1]
        # look for feasible neighbors
        curr_height = grid[curr[1]][curr[0]]
        for dir in directions:
            new = tuple_add(curr, dir)
            if new[0]<0 or new[0] >= width or new[1]<0 or new[1] >= height or new in visited:
                continue
            if grid[new[1]][new[0]] - 1 <= curr_height:
                if new == end:
                    return current_path
                new_path = current_path + [new]
                path_list.append(new_path)
                visited.add(new)
        path_index += 1
    return []

def part1(input: List[str])-> None:
    result = len(grid_solve(create_grid(input), (0,20), (107, 20)))
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    grid = create_grid(input)
    shortest = len(grid[0]) * len(grid)
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] == 1:
                path = grid_solve(grid, (x,y), (107, 20))
                if path:
                    shortest = min(shortest, len(path))
    print(f'Day {day()}, Part 2: {shortest}')

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        "Sabqponm",
        "abcryxxl",
        "accszExk",
        "acctuvwj",
        "abdefghi",
    ]

def test_day12_part1(puzzle_input):
    grid = create_grid(puzzle_input)
    assert len(grid) == 5
    assert len(grid[0]) == 8
    cost = 0
    assert len(grid_solve(grid, (0,0), (5,2))) == 31

def test_day12_part2(puzzle_input):
    grid = create_grid(puzzle_input)
    shortest = len(grid[0]) * len(grid)
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] == 1:
                shortest = min(shortest, len(grid_solve(grid, (x,y), (5,2))))
    assert shortest == 29