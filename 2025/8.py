from math import prod, sqrt
import pytest
import heapq
from typing import List, Tuple
from aoc import day, get_input


def getNodes(input: List[str]) -> List[List[int]]:
    nodes = []
    for line in input:
        nodes.append([int(c) for c in line.split(',')])
    return nodes


def getSortedDistances(nodes: List[List[int]]) -> List[Tuple[float, int, int]]:
    distances: List[Tuple[float, int, int]] = []
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            n_i = nodes[i]
            n_j = nodes[j]
            distance = sqrt((n_i[0] - n_j[0]) ** 2.0 + (n_i[1] - n_j[1]) ** 2.0 + (n_i[2] - n_j[2]) ** 2.0)
            heapq.heappush(distances, (distance, i, j))
    return distances


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1


def part1(input: List[str], num_connections: int = 1000) -> int:
    result = 0
    nodes = getNodes(input)
    distances = getSortedDistances(nodes)
    uf = UnionFind(len(nodes))
    for _ in range(num_connections):
        _, i, j = heapq.heappop(distances)
        uf.union(i, j)
    sizes = [0] * len(nodes)
    for node in range(len(nodes)):
        sizes[uf.find(node)] += 1
    result = prod(sorted(sizes, reverse=True)[:3])
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    nodes = getNodes(input)
    distances = getSortedDistances(nodes)
    uf = UnionFind(len(nodes))
    for _ in range(len(distances)):
        _, i, j = heapq.heappop(distances)
        uf.union(i, j)
        parent = uf.find(0)
        all_same = True
        for n in range(1, len(nodes)):
            if uf.find(n) != parent:
                all_same = False
                break
        if all_same:
            result = nodes[i][0] * nodes[j][0]
            break

    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        "162,817,812",
        "57,618,57",
        "906,360,560",
        "592,479,940",
        "352,342,300",
        "466,668,158",
        "542,29,236",
        "431,825,988",
        "739,650,466",
        "52,470,668",
        "216,146,977",
        "819,987,18",
        "117,168,530",
        "805,96,715",
        "346,949,466",
        "970,615,88",
        "941,993,340",
        "862,61,35",
        "984,92,344",
        "425,690,689",
    ]


def test_day8_part1(puzzle_input):
    assert part1(puzzle_input, 10) == 40


def test_day8_part2(puzzle_input):
    assert part2(puzzle_input) == 25272
