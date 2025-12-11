import pytest
from collections import deque
from functools import cache
from itertools import permutations
from math import prod
from typing import Deque, Dict, List, Tuple
from aoc import day, get_input


def getServers(input: List[str]) -> Dict[str, List[str]]:
    servers: Dict[str, List[str]] = {}
    for line in input:
        name = line[:3]
        children = line[5:].split(' ')
        servers[name] = children
    return servers


def getAllPaths(servers: Dict[str, List[str]], start: str, end: str) -> List[List[str]]:
    visited_paths = set()
    good_paths: List[List[str]] = []
    candidates: Deque[Tuple[str, List[str]]] = deque()
    candidates.append((start, []))
    while candidates:
        current, path = candidates.popleft()
        if current == end:
            good_paths.append(path)
            continue
        if current == "out":  # Failsafe if we can't find a path to the real thing
            continue
        tupled_path = tuple(path)
        if tupled_path in visited_paths:
            continue
        if path:
            visited_paths.add(tupled_path)
        for child in servers[current]:
            if child not in path:
                candidates.append((child, path + [child]))
    return good_paths


def part1(input: List[str]) -> int:
    paths = getAllPaths(getServers(input), "you", "out")
    result = len(paths)
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    servers =  getServers(input)
    @cache
    def visit(curr: str, dest: str):
        if curr == dest: 
            return 1
        return sum(visit(n, dest) for n in servers.get(curr, list()))
    for r in [['svr'] + list(p) + ['out'] for p in permutations(['fft', 'dac'])]:
        result += prod((visit(r[i], r[i+1]) for i in range(len(r)-1)))
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        "aaa: you hhh",
        "you: bbb ccc",
        "bbb: ddd eee",
        "ccc: ddd eee fff",
        "ddd: ggg",
        "eee: out",
        "fff: out",
        "ggg: out",
        "hhh: ccc fff iii",
        "iii: out",
    ]


def test_day11_part1(puzzle_input: List[str]):
    assert part1(puzzle_input) == 5


def test_day11_part2(puzzle_input: List[str]):
    puzzle_input = [
        "svr: aaa bbb",
        "aaa: fft",
        "fft: ccc",
        "bbb: tty",
        "tty: ccc",
        "ccc: ddd eee",
        "ddd: hub",
        "hub: fff",
        "eee: dac",
        "dac: fff",
        "fff: ggg hhh",
        "ggg: out",
        "hhh: out",
    ]
    assert part2(puzzle_input) == 2
