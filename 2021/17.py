import pytest
from typing import Dict, List, Tuple
from itertools import product
from aoc import day, get_input

def get_path(vx:int, vy:int, x_range, y_range)->Tuple[bool,int]:
    x, y = (0,0)
    max_y = 0
    while y > y_range[0]:
        x += vx
        y += vy
        max_y = max(max_y, y)
        vx += 1 if vx < 0 else -1 if vx > 0 else 0
        vy -= 1
        if x_range[0] <= x <= x_range[1] and  y_range[0] <= y <= y_range[1]:
            return True, max_y
    return False, max_y

def part1(input:Dict[str,Tuple[int,int]])-> int:
    vx_range = range(input['x'][0] // 2)
    vy_range = range(-input['y'][0])
    max_y = 0
    for vx,vy in product(vx_range, vy_range):
        hit, y = get_path(vx,vy,input['x'], input['y'])
        if hit:
            max_y = max(max_y, y)
    print(f'Day {day()}, Part 1: {max_y}')
    return max_y

def part2(input:Dict[str,Tuple[int,int]])-> int:
    vx_range = range(input['x'][1]+1)
    vy_range = range(input['y'][0],-input['y'][0]+1)
    count = 0
    for vx,vy in product(vx_range, vy_range):
        hit, _ = get_path(vx,vy,input['x'], input['y'])
        if hit:
            count += 1
    print(f'Day {day()}, Part 2: {count}')
    return count

if __name__ == "__main__":
    # input = get_input() x=287..309, y=-76..-48
    part1({'x':(287,309), 'y':(-76,-48)})
    part2({'x':(287,309), 'y':(-76,-48)})

@pytest.fixture
def puzzle_input():
    return {'x':(20,30), 'y':(-10,-5)}

def test_day17_part1(puzzle_input):
    assert get_path(6,9,puzzle_input['x'],puzzle_input['y']) == (True, 45)
    assert get_path(17,-4,puzzle_input['x'],puzzle_input['y']) == (False, 0)
    assert part1(puzzle_input) == 45

def test_day17_part2(puzzle_input):
    assert part2(puzzle_input) == 112