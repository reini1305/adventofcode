from collections import defaultdict
import pytest
from typing import DefaultDict, List, Tuple
from aoc import day, get_input


def parse_grid(input: List[str]) -> List[List[str]]:
    output = []
    for line in input:
        output.append([x for x in line])
    return output


def get_numbers(input: List[List[str]]) -> List[Tuple[int, List[Tuple[int, int]]]]:
    numbers = []
    for row in range(len(input)):
        curr_num = 0
        curr_coords = []
        for col in range(len(input[row])):
            curr = input[row][col]
            if curr.isdigit():
                curr_num = curr_num * 10 + int(curr)
                curr_coords.append((row, col))
            else:
                if curr_num and is_adjacent(input, curr_coords):
                    numbers.append((curr_num, get_adjacent_gears(input, curr_coords)))
                curr_num = 0
                curr_coords = []
        if curr_num and is_adjacent(input, curr_coords):
            numbers.append((curr_num, get_adjacent_gears(input, curr_coords)))
    return numbers


def get_adjacent_gears(grid: List[List[str]], coordinates: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    gears = set()
    for cx, cy in coordinates:
        for nx, ny in neighbors:
            try:
                if (cx + nx) < 0 or (cy + ny) < 0:
                    continue
                if grid[cx + nx][cy + ny] == '*':
                    gears.add((cx + nx, cy + ny))
            except IndexError:
                pass
    return list(gears)


def is_adjacent(grid: List[List[str]], coordinates: List[Tuple[int, int]]) -> bool:
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for cx, cy in coordinates:
        for nx, ny in neighbors:
            try:
                if (cx + nx) < 0 or (cy + ny) < 0:
                    continue
                if grid[cx + nx][cy + ny] in '+-*/@$#=%&':
                    return True
            except IndexError:
                pass
    return False


def part1(input: List[str]) -> int:
    result = sum([x[0] for x in get_numbers(parse_grid(input))])
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    votes: DefaultDict[Tuple[int, int], int] = defaultdict(int)
    numbers = defaultdict(list)
    numbers_votes = get_numbers(parse_grid(input))
    for n, vs in numbers_votes:
        for v in vs:
            votes[v] += 1
            numbers[v].append(n)
    result = 0
    for v in votes:
        if votes[v] == 2:
            result += numbers[v][0] * numbers[v][1]
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        '467..114..',
        '...*......',
        '..35..633.',
        '......#...',
        '617*......',
        '.....+.58.',
        '..592.....',
        '......755.',
        '...$.*....',
        '.664.598..',
    ]


def test_day3_part1(puzzle_input):
    assert [n for n, _ in get_numbers(parse_grid(puzzle_input))] == [467, 35, 633, 617, 592, 755, 664, 598]
    assert part1(puzzle_input) == 4361


def test_day3_part2(puzzle_input):
    assert get_adjacent_gears(parse_grid(puzzle_input), [(0, 2)]) == [(1, 3)]
    assert get_adjacent_gears(parse_grid(puzzle_input), [(2, 2)]) == [(1, 3)]
    assert part2(puzzle_input) == 467835


def test_day3_bonus():
    input = [
        '12.......*..',
        '+.........34',
        '.......-12..',
        '..78........',
        '..*....60...',
        '78.........9',
        '.5.....23..$',
        '8...90*12...',
        '............',
        '2.2......12.',
        '.*.........*',
        '1.1..503+.56',
    ]
    assert part1(input) == 925
    assert part2(input) == 6756
