import pytest
from typing import List, Tuple
from aoc import day, get_input
from copy import deepcopy

def simulate_seating(map: List[List[str]])->int:
    neighbors = [(-1,-1), (-1,0), (-1,1),
                 (0,-1),          (0,1),
                 (1,-1),  (1,0),  (1,1)]
    width = len(map[0])
    height = len(map)
    while True:
        new_map = deepcopy(map)
        for col in range(1,width-1):
            for row in range(1,height-1):
                if map[row][col] == 'L':
                    sum_occupied = 0
                    for dx, dy in neighbors:
                        if map[row+dy][col+dx]=='#':
                            sum_occupied += 1
                        if sum_occupied == 1:
                            break 
                    if sum_occupied == 0:
                        new_map[row][col] = '#'
                elif map[row][col] == '#':
                    sum_occupied = 0
                    for dx, dy in neighbors:
                        if map[row+dy][col+dx]=='#':
                            sum_occupied += 1
                        if sum_occupied == 4:
                            new_map[row][col] = 'L'
                            break 
        if new_map == map:
            break
        map = new_map
    return sum([line.count('#') for line in map])

def search_ray(map: List[List[str]], row:int, col:int, dir:Tuple[int,int])->bool:
    dx,dy = dir
    while map[row+dy][col+dx]!='e':
        if map[row+dy][col+dx]=='L':
            return False
        if map[row+dy][col+dx]=='#':
            return True
        dx += dir[0]
        dy += dir[1]
    return False

def simulate_seating2(map: List[List[str]])->int:
    neighbors = [(-1,-1), (-1,0), (-1,1),
                 (0,-1),          (0,1),
                 (1,-1),  (1,0),  (1,1)]
    width = len(map[0])
    height = len(map)
    while True:
        new_map = deepcopy(map)
        for col in range(1,width-1):
            for row in range(1,height-1):
                if map[row][col] in ['L', '#']:
                    sum_occupied = 0
                    for n in neighbors:
                        if search_ray(map,row,col,n):
                            sum_occupied += 1
                        if sum_occupied == 5:
                            break 
                    if map[row][col] == 'L' and sum_occupied == 0:
                        new_map[row][col] = '#'
                    elif map[row][col] == '#' and sum_occupied == 5:
                        new_map[row][col] = 'L'
        if new_map == map:
            break
        map = new_map
    return sum([line.count('#') for line in map])

def part1(input: List[List[str]])-> None:
    result = simulate_seating(input)
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[List[str]])-> None:
    result = simulate_seating2(input)
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = [list("e" + line + "e") for line in get_input(f'input{day()}.txt')]
    input.insert(0,["e" for _ in range(len(input[0]))])
    input.append(["e" for _ in range(len(input[0]))])
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    map = [ 'eeeeeeeeeeee',
            'eL.LL.LL.LLe',
            'eLLLLLLL.LLe',
            'eL.L.L..L..e',
            'eLLLL.LL.LLe',
            'eL.LL.LL.LLe',
            'eL.LLLLL.LLe',
            'e..L.L.....e',
            'eLLLLLLLLLLe',
            'eL.LLLLLL.Le',
            'eL.LLLLL.LLe',
            'eeeeeeeeeeee']
    return [list(line) for line in map]

def test_day11_part1(puzzle_input):
    map = puzzle_input
    assert simulate_seating(map) == 37

def test_day11_part2(puzzle_input):
    map = puzzle_input
    assert simulate_seating2(map) == 26