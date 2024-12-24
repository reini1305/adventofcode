from itertools import combinations
import pytest
from typing import List, Set, Tuple
from aoc import day, get_input
import networkx as nx  # type: ignore


def getEdgesAndNodes(input: list[str]) -> Tuple[Set[Tuple[str, str]], Set[str]]:
    edges = set()
    nodes = set()
    for line in input:
        e1, e2 = line.split('-')
        edges.add((e1, e2))
        edges.add((e2, e1))
        nodes.add(e1)
        nodes.add(e2)
    return edges, nodes


def part1(input: List[str]) -> int:
    result = 0
    edges, nodes = getEdgesAndNodes(input)
    for n1, n2, n3 in combinations(nodes, 3):
        if n1.startswith('t') or n2.startswith('t') or n3.startswith('t'):
            if (n1, n2) in edges and\
               (n2, n3) in edges and\
               (n1, n3) in edges:
                result += 1
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> str:
    result = ""
    G = nx.Graph()
    edges, nodes = getEdgesAndNodes(input)
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    max_len = 0
    for component in nx.find_cliques(G):
        if len(component) > max_len:
            max_len = len(component)
            result = ",".join(sorted(component))
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        'kh-tc',
        'qp-kh',
        'de-cg',
        'ka-co',
        'yn-aq',
        'qp-ub',
        'cg-tb',
        'vc-aq',
        'tb-ka',
        'wh-tc',
        'yn-cg',
        'kh-ub',
        'ta-co',
        'de-co',
        'tc-td',
        'tb-wq',
        'wh-td',
        'ta-ka',
        'td-qp',
        'aq-cg',
        'wq-ub',
        'ub-vc',
        'de-ta',
        'wq-aq',
        'wq-vc',
        'wh-yn',
        'ka-de',
        'kh-ta',
        'co-tc',
        'wh-qp',
        'tb-vc',
        'td-yn',
    ]


def test_day23_part1(puzzle_input):
    assert part1(puzzle_input) == 7


def test_day23_part2(puzzle_input):
    assert part2(puzzle_input) == 'co,de,ka,ta'
