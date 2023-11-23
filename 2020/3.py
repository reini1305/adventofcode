from typing import List
import pytest
from functools import reduce
from operator import mul

from aoc import day, get_input

def count_trees(maze: List[str], dx: int, dy: int) -> int:
    x=dx
    width=len(maze[0])
    count = 0
    for y in range(dy, len(maze), dy):
        if maze[y][x%width] == '#':
            count += 1
        x += dx
    return count

def part1(maze: List[str]) -> int:
    return count_trees(maze,3,1)

def part2(maze: List[str]) -> int:
    return reduce(mul,[count_trees(maze,dx,dy) for dx, dy in [(1,1),(3,1),(5,1),(7,1),(1,2)]])

if __name__ == "__main__":
    maze = get_input(f'input{day()}.txt')

    print(f'Day {day()}, Part 1: {part1(maze)}')
    print(f'Day {day()}, Part 2: {part2(maze)}')

@pytest.fixture
def example_maze():
    maze =['..##.......',
        '#...#...#..',
        '.#....#..#.',
        '..#.#...#.#',
        '.#...##..#.',
        '..#.##.....',
        '.#.#.#....#',
        '.#........#',
        '#.##...#...',
        '#...##....#',
        '.#..#...#.#']
    return maze

def test_day3_part1(example_maze):
    assert count_trees(example_maze,3,1) == 7

def test_day3_part2(example_maze):
    assert count_trees(example_maze,1,1) == 2
    assert count_trees(example_maze,3,1) == 7
    assert count_trees(example_maze,5,1) == 3
    assert count_trees(example_maze,7,1) == 4
    assert count_trees(example_maze,1,2) == 2
