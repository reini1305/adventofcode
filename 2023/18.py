import pytest
from typing import Dict, List, Set, Tuple
from aoc import day, get_input, tuple_add


def parse_input(input: List[str]) -> List[Tuple[str, int, str]]:
    output = []
    for line in input:
        direction, amount, color = line.split()
        output.append((direction, int(amount), color[1:-1]))
    return output


def get_path(instructions: List[Tuple[str, int, str]]) -> Dict[Tuple[int, int], str]:
    path = {}
    directions = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}
    current = (0, 0)
    for direction, amount, color in instructions:
        for _ in range(amount):
            current = tuple_add(current, directions[direction])
            path[current] = color
    return path


def count_inside(path: Dict[Tuple[int, int], str]) -> int:
    wpts = list(path.keys())
    A = sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(wpts, wpts[1:] + [wpts[0]]))
    return A // 2 + len(path) // 2 + 1


def part1(input: List[str]) -> int:
    instruction = parse_input(input)
    path = get_path(instruction)
    result = count_inside(path)
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
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
        'R 6 (#70c710)',
        'D 5 (#0dc571)',
        'L 2 (#5713f0)',
        'D 2 (#d2c081)',
        'R 2 (#59c680)',
        'D 2 (#411b91)',
        'L 5 (#8ceee2)',
        'U 2 (#caa173)',
        'L 1 (#1b58a2)',
        'U 2 (#caa171)',
        'R 2 (#7807d2)',
        'U 3 (#a77fa3)',
        'L 2 (#015232)',
        'U 2 (#7a21e3)',
    ]


def test_day18_part1(puzzle_input):
    instruction = parse_input(puzzle_input)
    path = get_path(instruction)
    assert count_inside(path) == 62


def test_day18_part2(puzzle_input):
    assert part2(puzzle_input) == 952408144115
