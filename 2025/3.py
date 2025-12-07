import pytest
from typing import List
from aoc import day, get_input


def getMaxJoltage(bank: List[int], num_batteries: int) -> int:
    max_joltage = 0
    largest_idx = 0
    for i in reversed(range(num_batteries)):
        for j in range(largest_idx + 1, len(bank) - i):
            if bank[j] > bank[largest_idx]:
                largest_idx = j
        max_joltage *= 10
        max_joltage += bank[largest_idx]
        largest_idx += 1
    return max_joltage


def parseInput(input: List[str]) -> List[List[int]]:
    output: List[List[int]] = []
    for line in input:
        output.append([int(c) for c in line])
    return output


def part1(input: List[str]) -> int:
    result = 0
    banks = parseInput(input)
    for bank in banks:
        result += getMaxJoltage(bank, 2)
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    banks = parseInput(input)
    for bank in banks:
        result += getMaxJoltage(bank, 12)
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]


def test_day3_part1(puzzle_input: List[str]):
    assert part1(puzzle_input) == 357


def test_day3_part2(puzzle_input: List[str]):
    assert part2(puzzle_input) == 3121910778619
