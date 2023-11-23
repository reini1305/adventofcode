import pytest
from typing import List
from aoc import day
from numba import jit

@jit(nopython=True)
def simulate_n_rounds(input:List[int], n:int, largest:int):
    next_cup = [0] * (largest + 1)
    for i in range(len(input)-1):
        next_cup[input[i]] = input[i+1] 
    if largest > max(input):
        next_cup[input[-1]] = max(input)+1 
        for i in range(len(input),largest-1):
            next_cup[i+1] = i+2
        next_cup[-1] = input[0]
    else:
        next_cup[input[-1]] = input[0]
    current_cup = input[0]
    for _ in range(n):
        cup1 = next_cup[current_cup]
        cup2 = next_cup[cup1]
        cup3 = next_cup[cup2]
        next_cup[current_cup] = next_cup[cup3]
        destination_position = (current_cup - 2) % largest + 1
        while destination_position in [cup1, cup2, cup3]:
            destination_position = (destination_position - 2) % largest + 1
        next_cup[cup3] = next_cup[destination_position]
        next_cup[destination_position] = cup1
        current_cup = next_cup[current_cup]
    return next_cup

def part1(input: List[int])-> None:
    next_cups = simulate_n_rounds(input, 100, len(input))
    result = ''
    next = next_cups[1]
    for _ in range(len(next_cups)-3):
        result+=str(next)
        next = next_cups[next]
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[int])-> None:
    cups = simulate_n_rounds(input, 10_000_000, 1_000_000)
    result = cups[1] * cups[cups[1]]
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = [3,6,8,1,9,5,7,4,2]
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [3,8,9,1,2,5,4,6,7]

def test_day23_part1(puzzle_input):
    input = puzzle_input
    next_cups = simulate_n_rounds(input, 100, len(input))
    assert next_cups[1] == 6
    assert next_cups[6] == 7
    assert next_cups[7] == 3
    assert next_cups[3] == 8
    assert next_cups[8] == 4
    assert next_cups[4] == 5
    assert next_cups[5] == 2
    assert next_cups[2] == 9
    assert next_cups[9] == 1

def test_day23_part2(puzzle_input):
    input = puzzle_input
    next_cups = simulate_n_rounds(input, 10_000_000, 1_000_000)
    assert next_cups[1] * next_cups[next_cups[1]] == 149245887792
