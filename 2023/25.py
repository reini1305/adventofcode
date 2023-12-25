from itertools import combinations
import pytest
import networkx as nx
from typing import List
from aoc import day, get_input


def parse_input(input: List[str]) -> nx.Graph:
    graph = nx.Graph()
    for line in input:
        parent, childs = line.split(': ')
        for c in childs.split(' '):
            graph.add_edge(parent, c, capacity=1)
    return graph


def part1(input: List[str]) -> int:
    result = 0
    graph = parse_input(input)
    for start, end in combinations(graph.nodes(), 2):
        cut_value, partition = nx.minimum_cut(graph, start, end)
        if cut_value == 3:
            result = len(partition[0]) * len(partition[1])
            break
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
        'jqt: rhn xhk nvd',
        'rsh: frs pzl lsr',
        'xhk: hfx',
        'cmg: qnr nvd lhk bvb',
        'rhn: xhk bvb hfx',
        'bvb: xhk hfx',
        'pzl: lsr hfx nvd',
        'qnr: nvd',
        'ntq: jqt hfx bvb xhk',
        'nvd: lhk',
        'lsr: lhk',
        'rzs: qnr cmg lsr rsh',
        'frs: qnr lhk lsr',
    ]


def test_day25_part1(puzzle_input):
    assert part1(puzzle_input) == 54


def test_day25_part2(puzzle_input):
    assert 1
