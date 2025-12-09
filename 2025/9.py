import pytest
from itertools import combinations
from typing import List
from shapely import Polygon
from aoc import day, get_input


def getCoordinates(input: List[str]) -> List[complex]:
    coordinates: List[complex] = []

    for line in input:
        x, y = line.split(',')
        coordinates.append(int(y) * 1j + int(x))
    return coordinates


def getArea(p1: complex, p2: complex) -> int:
    return int((abs(p1.real - p2.real) + 1) * (abs(p1.imag - p2.imag) + 1))


def part1(input: List[str]) -> int:
    result = 0
    for p1, p2 in combinations(getCoordinates(input), 2):
        result = max(result, getArea(p1, p2))
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    coordinates = getCoordinates(input)
    big_poly = Polygon([(p.real, p.imag) for p in coordinates])
    for p1, p2 in combinations(coordinates, 2):
        # create polygon from two points
        poly = Polygon([(p1.real, p1.imag), (p1.real, p2.imag), (p2.real, p2.imag), (p2.real, p1.imag)])
        if big_poly.contains(poly):
            result = max(result, getArea(p1, p2))

    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        "7,1",
        "11,1",
        "11,7",
        "9,7",
        "9,5",
        "2,5",
        "2,3",
        "7,3",
    ]


def test_day9_part1(puzzle_input: List[str]):
    assert part1(puzzle_input) == 50


def test_day9_part2(puzzle_input: List[str]):
    assert part2(puzzle_input) == 24
