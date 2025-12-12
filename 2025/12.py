import pytest
from typing import List, Tuple
from aoc import day, get_input


def getTiles(input: List[str]) -> List[int]:
    tiles = []
    num_set = 0
    for line in input:
        if line.startswith("#") or line.startswith("."):
            num_set += line.count('#')
        if line == "":
            tiles.append(num_set)
            num_set = 0
        
    return tiles


def getRegions(input: List[str]) -> List[Tuple[int, int, List[int]]]:
    regions: List[Tuple[int, int, List[int]]] = []
    for line in input:
        if not "x" in line:
            continue
        x, y = line[:line.find(":")].split("x")
        num_tiles = line[line.find(":")+2:].split(" ")
        regions.append((int(x), int(y), [int(c) for c in num_tiles]))

    return regions


def part1(input: List[str]) -> int:
    result = 0
    tiles = getTiles(input)
    regions = getRegions(input)
    for x, y, curr_tiles in regions:
        area = x * y
        grid = (x // 3) * (y // 3)
        num_tiles = sum(curr_tiles)
        sum_tiles = sum([tiles[i] * c for i, c in enumerate(curr_tiles)])
        # definitely possible, even without tiling
        if grid > num_tiles:
            result += 1
        # definitely not possible:
        elif area < sum_tiles:
            continue
        # in between, assume it works
        else:
            result += 1
        
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
        "0:",
        "###",
        "##.",
        "##.",
        "",
        "1:",
        "###",
        "##.",
        ".##",
        "",
        "2:",
        ".##",
        "###",
        "##.",
        "",
        "3:",
        "##.",
        "###",
        "##.",
        "",
        "4:",
        "###",
        "#..",
        "###",
        "",
        "5:",
        "###",
        ".#.",
        "###",
        "",
        "4x4: 0 0 0 0 2 0",
        "12x5: 1 0 1 0 2 2",
        "12x5: 1 0 1 0 3 2",
    ]


def test_day12_part1(puzzle_input: List[str]):
    assert part1(puzzle_input) == 3


def test_day12_part2(puzzle_input: List[str]):
    assert part2(puzzle_input) == 0
