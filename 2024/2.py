import pytest
from typing import List
from aoc import day, get_input


def getReports(input: List[str]) -> List[List[int]]:
    reports: List[List[int]] = []
    for line in input:
        reports.append([int(n) for n in line.split()])
    return reports


def checkSafe(report: List[int]) -> bool:
    isAscending = all([a > b and a <= b + 3 for a, b in zip(report[1:], report[:-1])])
    isDescending = all([a < b and a >= b - 3 for a, b in zip(report[1:], report[:-1])])
    return isAscending or isDescending


def checkSafe2(report: List[int]) -> bool:
    for i in range(len(report)):
        if checkSafe(report[:i] + report[i+1:]):
            return True
    return False


def part1(input: List[str]) -> int:
    result = sum([checkSafe(r) for r in getReports(input)])
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = sum([checkSafe2(r) for r in getReports(input)])
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9",
    ]


def test_day2_part1(puzzle_input):
    reports = getReports(puzzle_input)
    assert sum([checkSafe(r) for r in reports]) == 2


def test_day2_part2(puzzle_input):
    reports = getReports(puzzle_input)
    assert sum([checkSafe2(r) for r in reports]) == 4
