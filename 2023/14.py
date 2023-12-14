import pytest
from typing import List
from aoc import day, get_input


def parse_input(input: List[str]) -> List[List[str]]:
    output = []
    for line in input:
        output.append(list(line))
    return output


def move_up(input: List[List[str]]) -> List[List[str]]:
    move_happened = True
    while move_happened:
        move_happened = False
        for i in range(1, len(input)):
            for j in range(len(input[i])):
                if input[i][j] == 'O':
                    if input[i - 1][j] == '.':
                        input[i][j] = '.'
                        input[i - 1][j] = 'O'
                        move_happened = True
    return input


def move_down(input: List[List[str]]) -> List[List[str]]:
    move_happened = True
    while move_happened:
        move_happened = False
        for i in range(len(input) - 1):
            for j in range(len(input[i])):
                if input[i][j] == 'O':
                    if input[i + 1][j] == '.':
                        input[i][j] = '.'
                        input[i + 1][j] = 'O'
                        move_happened = True
    return input


def move_left(input: List[List[str]]) -> List[List[str]]:
    move_happened = True
    while move_happened:
        move_happened = False
        for i in range(len(input)):
            for j in range(1, len(input[i])):
                if input[i][j] == 'O':
                    if input[i][j - 1] == '.':
                        input[i][j] = '.'
                        input[i][j - 1] = 'O'
                        move_happened = True
    return input


def move_right(input: List[List[str]]) -> List[List[str]]:
    move_happened = True
    while move_happened:
        move_happened = False
        for i in range(len(input)):
            for j in range(len(input[i]) - 1):
                if input[i][j] == 'O':
                    if j < len(input[i]) and input[i][j + 1] == '.':
                        input[i][j] = '.'
                        input[i][j + 1] = 'O'
                        move_happened = True
    return input


def move_cycle(input: List[List[str]]) -> List[List[str]]:
    return move_right(move_down(move_left(move_up(input))))


def count_load(input: List[List[str]]) -> int:
    result = 0
    lines = len(input)
    for i, line in enumerate(input):
        for char in line:
            if char == 'O':
                result += lines - i
    return result


def hash_grid(input: List[List[str]]) -> str:
    result = ''
    for line in input:
        result += ''.join(line)
    return result


def part1(input: List[str]) -> int:
    result = count_load(move_up(parse_input(input)))
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    grid = parse_input(input)
    seen_grids = {}
    start = 0
    end = 0
    for iter in range(1000000000):
        grid = move_cycle(grid)
        hash = hash_grid(grid)
        if hash in seen_grids:
            start = seen_grids[hash]
            end = iter
            break
        seen_grids[hash] = iter
    # unroll loop
    todo = (1000000000 - start) % (end - start)
    for _ in range(todo - 1):
        grid = move_cycle(grid)
    result = count_load(grid)
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        'O....#....',
        'O.OO#....#',
        '.....##...',
        'OO.#O....O',
        '.O.....O#.',
        'O.#..O.#.#',
        '..O..#O..O',
        '.......O..',
        '#....###..',
        '#OO..#....',
    ]


def test_day14_part1(puzzle_input):
    grid = move_up(parse_input(puzzle_input))
    assert count_load(grid) == 136


def test_day14_part2(puzzle_input):
    assert part2(puzzle_input) == 64
