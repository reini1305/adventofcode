import pytest
from typing import List, Tuple
from operator import mul
from functools import reduce
from collections import deque
from aoc import day, get_input

def parse_input(input: List[str])->List[List[int]]:
    output = []
    for line in input:
        output.append([int(i) for i in line])
    return output

def get_local_minima(field: List[List[int]])->List[Tuple[int,int]]:
    neighbors = [(-1,0), (1,0), (0,-1), (0,1)]
    minima = []
    for x in range(len(field[0])):
        for y in range(len(field)):
            is_minimum = True
            for nx, ny in neighbors:
                try:
                    if y+ny>=0 and x+nx>=0 and field[y+ny][x+nx] <= field[y][x]:
                        is_minimum = False
                        break
                except:
                    pass
            if is_minimum:
                minima.append((y,x))
    return minima

def get_basins(field: List[List[int]], minima: List[Tuple[int,int]])->List[int]:
    neighbors = [(-1,0), (1,0), (0,-1), (0,1)]
    sizes = []
    for my, mx in minima:
        to_check = deque([(my,mx)])
        basin = []
        while to_check:
            y,x = to_check.popleft()
            try:
                if (y,x) not in basin and y>=0 and x >=0 and field [y][x] != 9:
                    basin.append((y,x))
                    # check neighbors next
                    for ny, nx in neighbors:
                        to_check.append((y+ny, x+nx))
            except:
                pass # outside of image
        sizes.append(len(basin))
    return sizes

def part1(input: List[List[int]])-> List[Tuple[int,int]]:
    minima = get_local_minima(input)
    result = sum([input[y][x]+1 for y,x in minima])
    print(f'Day {day()}, Part 1: {result}')
    return minima

def part2(input: List[List[int]], minima:List[Tuple[int,int]])-> None:
    result = reduce(mul, sorted(get_basins(input,minima))[-3:], 1)
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    field = parse_input(input)
    minima = part1(field)
    part2(field, minima)

@pytest.fixture
def puzzle_input():
    return [
        "2199943210",
        "3987894921",
        "9856789892",
        "8767896789",
        "9899965678"
    ]

def test_day9_part1(puzzle_input):
    field = parse_input(puzzle_input)
    assert field[0][0] == 2
    assert sorted(get_local_minima(field)) == [(0,1),(0,9),(2,2),(4,6)]
    assert sum([field[y][x]+1 for y,x in get_local_minima(field)]) == 15

def test_day9_part2(puzzle_input):
    field = parse_input(puzzle_input)
    minima = get_local_minima(field)
    assert sorted(get_basins(field,minima)) == [3, 9, 9, 14]