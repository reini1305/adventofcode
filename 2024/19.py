import pytest
from typing import List
from aoc import day, get_input


def getDesigns(input: List[str]) -> List[str]:
    return input[2:]


def getTowels(input: List[str]) -> List[str]:
    return input[0].split(', ')


def countWaysToCreateDesign(design: str, towels: List[str]) -> int:
    count = [0] * (len(design) + 1)
    count[0] = 1

    possible_towels = [t for t in towels if t in design]
    for i in range(len(design) + 1):
        for towel in possible_towels:
            if i >= len(towel) and design[i - len(towel):i] == towel:
                count[i] += count[i - len(towel)]

    return count[-1]


def part1(input: List[str]) -> int:
    result = 0
    designs = getDesigns(input)
    towels = getTowels(input)
    for design in designs:
        if countWaysToCreateDesign(design, towels) > 0:
            result += 1
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    designs = getDesigns(input)
    towels = getTowels(input)
    for design in designs:
        result += countWaysToCreateDesign(design, towels)
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        'r, wr, b, g, bwu, rb, gb, br',
        '',
        'brwrr',
        'bggr',
        'gbbr',
        'rrbgbr',
        'ubwu',
        'bwurrg',
        'brgr',
        'bbrgwb',
    ]


def test_day19_part1(puzzle_input):
    assert part1(puzzle_input) == 6


def test_day19_part2(puzzle_input):
    assert part2(puzzle_input) == 16
