import pytest
from typing import List, Tuple
from heapq import heappop, heappush
from aoc import day, get_input

def parse_input(input: List[str])->List[List[int]]:
    field = []
    for line in input:
        field.append([int(c) for c in line])
    return field

def min_path_length(field:List[List[int]], start:Tuple[int,int], end:Tuple[int,int], repeat:int=1):
    neighbors = [(-1,0), (1,0), (0,-1), (0,1)]
    seen = set()
    heap=[(0, start)]
    n = len(field)

    while len(heap):
        risk, curr = heappop(heap)
        if curr in seen:
            continue
        seen.add(curr)
        if curr == end:
            return risk
        for nx,ny in neighbors:
            dx = nx + curr[0]
            dy = ny + curr[1]
            if dx >= 0 and dy >= 0 and dx < n*repeat and dy < n*repeat:
                cost = field[dy%n][dx%n] + dy // n + dx // n 
                while cost > 9:
                    cost -= 9
                heappush(heap, (cost+risk, (dx,dy)))

def part1(input: List[str])-> None:
    field = parse_input(input)
    n = len(field[0]) - 1
    result = min_path_length(field,(0,0),(n,n))
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    field = parse_input(input)
    n = len(field[0])*5 - 1
    result = min_path_length(field,(0,0),(n,n),5)
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        "1163751742",
        "1381373672",
        "2136511328",
        "3694931569",
        "7463417111",
        "1319128137",
        "1359912421",
        "3125421639",
        "1293138521",
        "2311944581",
    ]

def test_day15_part1(puzzle_input):
    field = parse_input(puzzle_input)
    assert len(field) == 10
    assert len(field[0]) == 10
    assert min_path_length(field,(0,0),(9,9)) == 40

def test_day15_part2(puzzle_input):
    field = parse_input(puzzle_input)
    assert min_path_length(field,(0,0),(49,49),5) == 315