import pytest
from typing import List, Tuple
from aoc import day, get_input


def getRanges(input: List[str]) -> List[Tuple[int, int]]:
    ranges: List[Tuple[int, int]] = []
    for line in input:
        if line == "":
            break
        min_val, max_val = line.split("-")
        ranges.append((int(min_val), int(max_val)))
    return ranges


def getIngredients(input: List[str]) -> List[int]:
    ingredients = []
    for line in input:
        try:
            ingredients.append(int(line))
        except:
            pass
    return ingredients


def mergeRanges(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    # sort by begin
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged = [sorted_ranges[0]]
    for current in sorted_ranges:
        previous = merged[-1]
        if current[0] <= previous[1]:
            previous = (previous[0], max(previous[1], current[1]))
            merged[-1] = previous
        else:
            merged.append(current)
    return merged


def part1(input: List[str]) -> int:
    result = 0
    ranges = getRanges(input)
    ingredients = getIngredients(input)
    for i in ingredients:
        for min_val, max_val in ranges:
            if min_val <= i <= max_val:
                result += 1
                break
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    ranges = mergeRanges(getRanges(input))
    for min_val, max_val in ranges:
        result += max_val - min_val + 1
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        "3-5",
        "10-14",
        "16-20",
        "12-18",
        "",
        "1",
        "5",
        "8",
        "11",
        "17",
        "32",
    ]


def test_day5_part1(puzzle_input):
    assert part1(puzzle_input) == 3


def test_day5_part2(puzzle_input):
    assert part2(puzzle_input) == 14
