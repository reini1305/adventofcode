import pytest
from typing import List, Set, Tuple
from aoc import day, get_input, tuple_add


def getGrid(input: List[str]) -> List[List[str]]:
    output = []
    for line in input:
        output.append([c for c in line])
    return output


def getRegions(input: List[List[str]]) -> List[Set[Tuple[int, int]]]:
    regions: List[Set[Tuple[int, int]]] = []
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    sizex = len(input[0])
    sizey = len(input)
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == '.':
                continue
            region = set()
            region.add((x, y))
            candidates = [(x, y)]
            id = input[y][x]
            input[y][x] = '.'
            while candidates:
                c = candidates.pop()
                for d in directions:
                    nx, ny = tuple_add(c, d)
                    if nx >= 0 and ny >= 0 and nx < sizex and ny < sizey\
                       and input[ny][nx] == id and (nx, ny) not in region:
                        region.add((nx, ny))
                        candidates.append((nx, ny))
                        input[ny][nx] = '.'
            regions.append(region)
    return regions


def getBoundaryLength(region: Set[Tuple[int, int]]) -> int:
    length = 4 * len(region)
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for r in region:
        for d in directions:
            if tuple_add(d, r) in region:
                length -= 1
    return length


def getBoundaryCorners(region: Set[Tuple[int, int]]) -> int:
    corners = 0
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for r in region:
        for dx, dy in directions:
            a = tuple_add(r, (dx, 0)) in region
            b = tuple_add(r, (0, dy)) in region
            c = tuple_add(r, (dx, dy)) in region
            if (not a and not b) or (a and b and not c):
                corners += 1
    return corners


def part1(input: List[str]) -> int:
    result = 0
    regions = getRegions(getGrid(input))
    for region in regions:
        result += len(region) * getBoundaryLength(region)
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    regions = getRegions(getGrid(input))
    for region in regions:
        result += len(region) * getBoundaryCorners(region)
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        'RRRRIICCFF',
        'RRRRIICCCF',
        'VVRRRCCFFF',
        'VVRCCCJFFF',
        'VVVVCJJCFE',
        'VVIVCCJJEE',
        'VVIIICJJEE',
        'MIIIIIJJEE',
        'MIIISIJEEE',
        'MMMISSJEEE',
    ]


def test_day12_part1(puzzle_input):
    assert part1(puzzle_input) == 1930


def test_day12_part2(puzzle_input):
    assert part2(puzzle_input) == 1206
