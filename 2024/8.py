import pytest
from typing import Dict, List, Tuple
from aoc import day, get_input, tuple_add, tuple_diff


def getAntennas(input: List[str]) -> Dict[str, List[Tuple[int, int]]]:
    antennas: Dict[str, List[Tuple[int, int]]] = {}
    for y, line in enumerate(input):
        for x, c in enumerate(line):
            if c.isalpha() or c.isdigit():
                if c not in antennas:
                    antennas[c] = []
                antennas[c].append((x, y))

    return antennas


def getAntiNodes(
        antenna_1: Tuple[int, int],
        antenna_2: Tuple[int, int]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    diff = tuple_diff(antenna_2, antenna_1)
    return tuple_diff(antenna_1, diff), tuple_add(antenna_2, diff)


def getAntiNodesHarmonic(
        antenna_1: Tuple[int, int],
        antenna_2: Tuple[int, int],
        sizex: int,
        sizey: int) -> List[Tuple[int, int]]:
    diff = tuple_diff(antenna_2, antenna_1)
    anti_nodes = [antenna_1, antenna_2]
    nx, ny = tuple_diff(antenna_1, diff)
    while nx >= 0 and ny >= 0 and nx < sizex and ny < sizey:
        anti_nodes.append((nx, ny))
        nx, ny = tuple_diff((nx, ny), diff)
    nx, ny = tuple_add(antenna_2, diff)
    while nx >= 0 and ny >= 0 and nx < sizex and ny < sizey:
        anti_nodes.append((nx, ny))
        nx, ny = tuple_add((nx, ny), diff)
    return anti_nodes


def part1(input: List[str]) -> int:
    result = 0
    antennas = getAntennas(input)
    nodes = set()
    for frequency in antennas:
        for ant1 in antennas[frequency]:
            for ant2 in antennas[frequency]:
                if ant1 == ant2:
                    continue
                c1, c2 = getAntiNodes(ant1, ant2)
                nodes.add(c1)
                nodes.add(c2)
    sizex = len(input[0])
    sizey = len(input)
    for nx, ny in nodes:
        if nx >= 0 and ny >= 0 and nx < sizex and ny < sizey:
            result += 1
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    antennas = getAntennas(input)
    sizex = len(input[0])
    sizey = len(input)
    nodes = set()
    for frequency in antennas:
        for ant1 in antennas[frequency]:
            for ant2 in antennas[frequency]:
                if ant1 == ant2:
                    continue
                for node in getAntiNodesHarmonic(ant1, ant2, sizex, sizey):
                    nodes.add(node)
    result = len(nodes)
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        "............",
        "........0...",
        ".....0......",
        ".......0....",
        "....0.......",
        "......A.....",
        "............",
        "............",
        "........A...",
        ".........A..",
        "............",
        "............",
    ]


def test_day8_part1(puzzle_input):
    antennas = getAntennas(puzzle_input)
    assert antennas["0"][0] == (8, 1)
    nodes = getAntiNodes(antennas["0"][0], antennas["0"][1])
    assert nodes[1] == (2, 3)
    assert nodes[0] == (11, 0)
    assert part1(puzzle_input) == 14


def test_day8_part2(puzzle_input):
    assert part2(puzzle_input) == 34
