import pytest
from typing import List
import numpy as np
from aoc import day, get_input

def parse_input(input: List[str])-> List[List[int]]:
    output = []
    for line in input:
        output.append([int(i) for i in line])
    return output

def simulate_steps(field:List[List[int]], steps:int)->int:
    current_field = np.array(field)
    total_flashes = 0
    neighbors = [(-1,-1),(-1,0),(-1,1),
                 ( 0,-1),       ( 0,1),
                 ( 1,-1),( 1,0),( 1,1)]
    if steps<1:
        steps=1_000
    for step in range(steps):
        flashes = np.zeros(current_field.shape)
        current_field += 1
        new_flashes = True
        while new_flashes:
            new_flashes = False
            for y in range(10):
                for x in range(10):
                    if current_field[y,x] > 9:
                        current_field[y,x] = 0
                        if flashes[y,x] == 0:
                            #increase neighbors
                            new_flashes = True
                            flashes[y,x] = 1
                            for ny,nx in neighbors:
                                dx = x+nx
                                dy = y+ny
                                if 0<=dx<=9 and 0<=dy<=9:
                                    current_field[dy,dx] += 1

        sum_flashes = int(np.sum(flashes))
        if steps == 1_000 and sum_flashes == 100:
            return step + 1
        total_flashes += sum_flashes
        current_field[flashes==1] = 0
    return total_flashes

def part1(input: List[str])-> None:
    result = simulate_steps(parse_input(input),100)
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    result = simulate_steps(parse_input(input),-1)
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        "5483143223",
        "2745854711",
        "5264556173",
        "6141336146",
        "6357385478",
        "4167524645",
        "2176841721",
        "6882881134",
        "4846848554",
        "5283751526"
    ]

def test_day11_part1(puzzle_input):
    assert parse_input(puzzle_input)[0][0] == 5
    assert simulate_steps(parse_input(puzzle_input),10) == 204
    assert simulate_steps(parse_input(puzzle_input),2) == 35

def test_day11_part2(puzzle_input):
    assert simulate_steps(parse_input(puzzle_input),-1) == 195