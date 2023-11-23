from typing import List
import pytest
from functools import reduce

from aoc import day, get_input

def get_id(boarding_pass: str)-> int:
    return sum([2**(9-i) for i in range(len(boarding_pass)) if boarding_pass[i] in ['B','R']])

def part1(input: List[str])-> None:
    max_id: int = 0
    for bp in input:
        id = get_id(bp)
        max_id = max(id, max_id)
    print(f'Day {day()}, Part 1: {max_id}')

def part2(input: List[str])-> None:
    all_ids: List[int] = sorted([get_id(bp) for bp in input])
    for i in range(max(all_ids)):
        if i not in all_ids and i-1 in all_ids and i+1 in all_ids:
            print(f'Day {day()}, Part 2: {i}')
            break

if __name__ == "__main__":
    input = get_input(f'input{day()}.txt')
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    boarding_passes=['BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL']
    return boarding_passes

def test_day5_part1(puzzle_input):
    boarding_passes = puzzle_input
    assert get_id(boarding_passes[0]) == 567
    assert get_id(boarding_passes[1]) == 119
    assert get_id(boarding_passes[2]) == 820
