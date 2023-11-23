import pytest
from typing import List
from aoc import day, get_input

def get_most_common_bit(input: List[str])->str:
    one_count = [0] * len(input[0])
    for line in input:
        for i,c in enumerate(line):
            if c == "1":
                one_count[i] += 1

    return "".join(["1" if one >= len(input)/2 else "0" for one in one_count])

def to_dec(input: str)->int:
    return sum([2**i if c =="1" else 0 for i,c in enumerate(reversed(input))])

def one_complement(input: str)->str:
    return "".join(["1" if c == "0" else "0" for c in input])

def get_rating(input: List[str], most_common: bool)->str:
    pattern = get_most_common_bit(input)
    if not most_common:
       pattern = one_complement(pattern)
    curr_id = 0
    while len(input) > 1:
        input = [l for l in input if l[curr_id] == pattern[curr_id]]
        if len(input) > 1:
            curr_id += 1
            pattern = get_most_common_bit(input)
            if not most_common:
                pattern = one_complement(pattern)
    return input[0]

def part1(input: List[str])-> None:
    common = get_most_common_bit(input)
    result = to_dec(common) * to_dec(one_complement(common))
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    result = to_dec(get_rating(input,False)) * to_dec(get_rating(input,True))
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

def test_day3_part1(puzzle_input):
    assert get_most_common_bit(puzzle_input) =="10110"
    assert to_dec(get_most_common_bit(puzzle_input)) == 22
    assert one_complement("10110") == "01001"

def test_day3_part2(puzzle_input):
    # assert get_rating(puzzle_input,True) == "10111"
    assert get_rating(puzzle_input,False) == "01010"