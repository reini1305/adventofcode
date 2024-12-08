import pytest
from typing import List, Set, Tuple
from aoc import day, get_input, tuple_add


def parseInput(input: List[str]) -> Tuple[Tuple[int, int], Set[Tuple[int, int]]]:
    guard = (0, 0)
    obstacles = set()
    for y, line in enumerate(input):
        for x, c in enumerate(line):
            if c == '^':
                guard = (x, y)
            elif c == '#':
                obstacles.add((x, y))
    return guard, obstacles


def getVisitedNodes(
        guard: Tuple[int, int],
        obstacles: Set[Tuple[int, int]],
        sizex: int,
        sizey: int) -> Tuple[Set[Tuple[int, int]], bool]:
    nodes = set()
    nodes_dirs = set()
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    cur_dir = 0
    cur_pos = guard
    loop_detected = False
    while cur_pos[0] >= 0 and cur_pos[1] >= 0 and cur_pos[0] < sizex and cur_pos[1] < sizey:
        nodes.add(cur_pos)
        nodes_dirs.add((cur_pos, cur_dir))
        next_pos = tuple_add(cur_pos, directions[cur_dir])
        if next_pos in obstacles:
            cur_dir = (cur_dir + 1) % 4
        else:
            cur_pos = next_pos
        if (cur_pos, cur_dir) in nodes_dirs:
            loop_detected = True
            break
    return nodes, loop_detected


def part1(input: List[str]) -> int:
    guard, obstacles = parseInput(input)
    sizex = len(input[0])
    sizey = len(input)
    result = len(getVisitedNodes(guard, obstacles, sizex, sizey)[0])
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    guard, obstacles = parseInput(input)
    sizex = len(input[0])
    sizey = len(input)
    result = 0
    for x in range(sizex):
        for y in range(sizey):
            if (x, y) == guard:
                continue
            _, loop_detected = getVisitedNodes(guard, obstacles | {(x, y)}, sizex, sizey)
            if loop_detected:
                result += 1
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        '....#.....',
        '.........#',
        '..........',
        '..#.......',
        '.......#..',
        '..........',
        '.#..^.....',
        '........#.',
        '#.........',
        '......#...',
    ]


def test_day6_part1(puzzle_input):
    guard, obstacles = parseInput(puzzle_input)
    assert guard == (4, 6)
    assert len(obstacles) == 8
    assert part1(puzzle_input) == 41


def test_day6_part2(puzzle_input):
    assert part2(puzzle_input) == 6
