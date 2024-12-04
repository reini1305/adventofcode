import pytest
from typing import List
from aoc import day, get_input, pad_array


def countXmas(input: List[str], start_x: int, start_y: int) -> int:
    directions = [
        [(1, 0), (2, 0), (3, 0)],        # horizontal
        [(-1, 0), (-2, 0), (-3, 0)],     # horizontal
        [(0, 1), (0, 2), (0, 3)],        # vertical
        [(0, -1), (0, -2), (0, -3)],     # vertical
        [(1, 1), (2, 2), (3, 3)],        # diagonal
        [(-1, -1), (-2, -2), (-3, -3)],  # diagonal
        [(1, -1), (2, -2), (3, -3)],     # diagonal
        [(-1, 1), (-2, 2), (-3, 3)],     # diagonal
        ]
    text = "MAS"
    count = 0
    if input[start_y][start_x] == "X":
        for dir in directions:
            if all([input[start_y+d[1]][start_x+d[0]] == text[i] for i, d in enumerate(dir)]):
                count += 1
    return count


def countMas(input: List[str], start_x: int, start_y: int) -> int:
    directions = [
        [(-1, 1), (1, -1)],  # diagonal
        [(-1, -1), (1, 1)],  # diagonal
        [(1, -1), (-1, 1)],  # diagonal
        [(1, 1), (-1, -1)],  # diagonal
        ]
    text = "MS"
    count = 0
    if input[start_y][start_x] == "A":
        for dir in directions:
            if all([input[start_y+d[1]][start_x+d[0]] == text[i] for i, d in enumerate(dir)]):
                count += 1
    return count == 2


def part1(input: List[str]) -> int:
    input = pad_array(input, '.', 3)
    result = sum([countXmas(input, x, y) for x in range(len(input[0])) for y in range(len(input))])
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    input = pad_array(input, '.', 1)
    result = sum([countMas(input, x, y) for x in range(len(input[0])) for y in range(len(input))])
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]


def test_day4_part1(puzzle_input):
    assert part1(puzzle_input) == 18


def test_day4_part2(puzzle_input):
    assert part2(puzzle_input) == 9
