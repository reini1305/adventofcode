import pytest
from typing import List
from aoc import day, get_input

def parse_input(input: List[str]) -> List[int]:
    calories_per_elf:List[int] = [0]
    for line in input:
        line=line.strip()
        if line == "":
            calories_per_elf.append(0)
        else:
            calories_per_elf[-1] += int(line)
    return calories_per_elf

def part1(input: List[str])-> int:
    cpe = parse_input(input)
    result = max(cpe)
    print(f'Day {day()}, Part 1: {result}')
    return result

def part2(input: List[str])-> int:
    cpe = parse_input(input)
    result = sum(sorted(cpe)[-3:])
    print(f'Day {day()}, Part 2: {result}')
    return result

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000"
    ]

def test_day1_part1(puzzle_input):
    assert part1(puzzle_input) == 24000

def test_day1_part2(puzzle_input):
    assert part2(puzzle_input) == 45000