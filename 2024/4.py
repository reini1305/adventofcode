import pytest
from typing import List
from aoc import day, get_input


def countXmas(input: List[str], start_x: int, start_y: int) -> int:
    directions = [
        [(1,0), (2,0), (3,0)],        # horizontal
        [(-1,0), (-2,0), (-3,0)],     # horizontal
        [(0,1), (0,2), (0,3)],        # vertical
        [(0,-1), (0,-2), (0,-3)],     # vertical
        [(1,1), (2,2), (3,3)],        # diagonal
        [(-1,-1), (-2,-2), (-3,-3)],  # diagonal
        [(1,-1), (2,-2), (3,-3)],     # diagonal
        [(-1,1), (-2,2), (-3,3)],     # diagonal
        ]
    text = "MAS"
    count = 0
    if input[start_y][start_x] == "X":
        for dir in directions:
            try:
                if all([input[start_y+d[1]][start_x+d[0]] == text[i] for i, d in enumerate(dir)]) and\
                   all([start_y+d[1]>=0 and start_x+d[0]>=0 for d in dir]):
                    count += 1
            except IndexError:
                pass
    return count


def part1(input: List[str]) -> int:
    result = sum([countXmas(input, x, y) for x in range(len(input[0])) for y in range(len(input))])
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
    assert 1
