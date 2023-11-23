import pytest
from typing import List, Set, Tuple
from aoc import day, get_input
from copy import deepcopy
from itertools import product

def initialize_seat_map(input:List[str], dimensions:int)->Set[Tuple[int,...]]:
    seat_map:Set[Tuple[int,...]] = set()
    for y,line in enumerate(input):
        for x,c in enumerate(line):
            if c == '#':
                seat_map.add((x,y,*[0 for _ in range(dimensions - 2)]))
    return seat_map

def simulate_seating(seat_map: Set[Tuple[int,...]], cycles:int)->int:
    dimensions = len(next(iter(seat_map)))
    neighbors = list(product(*[[-1, 0, 1] for _ in range(dimensions)]))
    neighbors.remove(tuple([0 for _ in range(dimensions)]))
    for _ in range(cycles):
        to_check:Set[Tuple[int,...]] = set()
        new_seat_map = deepcopy(seat_map)
        # first check all active fields
        for active in seat_map:
            sum_active = 0
            for n in neighbors:
                new_coord = tuple(map(sum, zip(active, n)))
                to_check.add(new_coord)
                if new_coord in seat_map:
                    sum_active+=1
            if not(sum_active == 2 or sum_active == 3):
                new_seat_map.remove(active)
        # now check all the fields adjacent to active fields
        for inactive in to_check:
            if inactive in seat_map:
                continue # not actually inactive
            sum_active = 0
            for n in neighbors:
                if tuple(map(sum, zip(inactive, n))) in seat_map:
                    sum_active+=1
            if sum_active == 3:
                new_seat_map.add(inactive)
        seat_map = new_seat_map
    return len(seat_map)

def part1(input: List[str])-> None:
    result = simulate_seating(initialize_seat_map(input,3),6)
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    result = simulate_seating(initialize_seat_map(input,4),6)
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input(f'input{day()}.txt')
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    input = ['.#.',
            '..#',
            '###']
    
    return input

def test_day17_part1(puzzle_input):
    seat_map = initialize_seat_map(puzzle_input,3)
    assert len(seat_map) == 5
    assert simulate_seating(seat_map,6) == 112

def test_day17_part2(puzzle_input):
    seat_map = initialize_seat_map(puzzle_input,4)
    assert len(seat_map) == 5
    assert simulate_seating(seat_map,6) == 848