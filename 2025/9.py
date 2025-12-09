import pytest
from itertools import combinations
from typing import List, Tuple
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


def part12(input: List[str]) -> Tuple[int, int]:
    result_p2 = 0
    result_p1 = 0
    coordinates = getCoordinates(input)
    big_poly = Polygon([(p.real, p.imag) for p in coordinates])
    for p1, p2 in combinations(coordinates, 2):
        area = getArea(p1, p2)
        result_p1 = max(result_p1, area)
        # create polygon from two points
        poly = Polygon([(p1.real, p1.imag), (p1.real, p2.imag), (p2.real, p2.imag), (p2.real, p1.imag)])
        if big_poly.contains(poly):
            result_p2 = max(result_p2, area)

    print(f'Day {day()}, Part 1: {result_p1}')
    print(f'Day {day()}, Part 2: {result_p2}')
    return result_p1, result_p2


if __name__ == "__main__":
    input = get_input()
    part12(input)


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
    assert part12(puzzle_input)[0] == 50


def test_day9_part2(puzzle_input: List[str]):
    assert part12(puzzle_input)[1] == 24
