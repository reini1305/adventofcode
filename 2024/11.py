from collections import defaultdict
import pytest
from typing import DefaultDict, List
from aoc import day, get_input


def blink(numbers: DefaultDict[str, int]) -> DefaultDict[str, int]:
    output: DefaultDict[str, int] = defaultdict(int)
    for number in numbers:
        count = numbers[number]
        if number == '0':
            output['1'] += count
        elif len(number) % 2 == 0:
            output[number[:len(number)//2]] += count
            output[str(int(number[len(number)//2:]))] += count
        else:
            output[str(2024 * int(number))] += count
    return output


def parseInput(input: List[str]) -> DefaultDict[str, int]:
    data = input[0].split()
    counter = defaultdict(int)
    for v in data:
        counter[v] = 1
    return counter


def part1(input: List[str]) -> int:
    counter = parseInput(input)
    for _ in range(25):
        counter = blink(counter)
    result = sum(counter.values())
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    counter = parseInput(input)
    for _ in range(75):
        counter = blink(counter)
    result = sum(counter.values())
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return ['125 17']


def test_day11_part1(puzzle_input):
    assert part1(puzzle_input) == 55312


def test_day11_part2(puzzle_input):
    assert 1
