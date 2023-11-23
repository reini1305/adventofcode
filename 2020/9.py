import pytest
from typing import List, Tuple, Optional
from aoc import day, get_num_input
from itertools import combinations

def find_sum_n(input: List[int], n: int, s:int) -> Tuple[Optional[int], ...]:
    for e in combinations(input,n):
        if sum(e) == s:
            return e
    return (None, None)

def find_first_not_sum_to_n(input: List[int], preamble_size: int)->Optional[int]:
    for curr_id in range(preamble_size, len(input)):
        if find_sum_n(input[curr_id-preamble_size:curr_id], 2, input[curr_id])[0] is None:
            return input[curr_id]
    return None

def part1(input: List[int])-> None:
    result = find_first_not_sum_to_n(input, 25)
    print(f'Day {day()}, Part 1: {result}')

def find_contiguous_set_sum_to_n(input: List[int], n:int)->List[int]:
    start_id:int = 0
    stop_id:int = 1
    s = input[start_id]
    while  s != n:
        if s < n:
            s += input[stop_id]
            stop_id+=1
        elif s > n:
            s -= input[start_id]
            start_id+=1

    return input[start_id:stop_id]

def part2(input: List[int])-> None:
    n = find_first_not_sum_to_n(input, 25)
    if n:
        result = find_contiguous_set_sum_to_n(input, n)
        print(f'Day {day()}, Part 2: {min(result) + max(result)}')

if __name__ == "__main__":
    input = get_num_input(f'input{day()}.txt')
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    input = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]
    return input

def test_day9_part1(puzzle_input):
    input = puzzle_input
    assert find_first_not_sum_to_n(input,5) == 127

def test_day9_part2(puzzle_input):
    input = puzzle_input
    contiguous_set = find_contiguous_set_sum_to_n(input, 127)
    assert min(contiguous_set) == 15
    assert max(contiguous_set) == 47