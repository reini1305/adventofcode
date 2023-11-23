import pytest
from typing import Dict, List, Tuple
from aoc import day, get_num_input

def get_num_differences(input:List[int])->Tuple[int,int]:
    num_one = 0
    num_three = 0
    sorted_input = list(sorted(input))
    for i in range(len(sorted_input)-1):
        if sorted_input[i+1] - sorted_input[i] == 1:
            num_one += 1
        elif sorted_input[i+1] - sorted_input[i] == 3:
            num_three += 1
    num_three+=1
    return (num_one, num_three)

def part1(input: List[int])-> None:
    result = get_num_differences(input)
    print(f'Day {day()}, Part 1: {result[0]*result[1]}')

def get_num_reachable(input:List[int],cache:Dict[int,int])->int:
    last = input[-1]
    if last in cache:
        return cache[last]
    if len(input) <= 2:
        return 1
    num_reachable = 0
    if last - input[-2] <= 3:
        num_reachable += get_num_reachable(input[:-1],cache)
    if len(input) >= 3 and last - input[-3] <= 3:
        num_reachable += get_num_reachable(input[:-2],cache)
    if len(input) >= 4 and last - input[-4] <= 3:
        num_reachable += get_num_reachable(input[:-3],cache)
    cache[last] = num_reachable
    return num_reachable

def part2(input: List[int])-> None:
    s = list(sorted(input))
    result = get_num_reachable(s,{})
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_num_input(f'input{day()}.txt')
    input.append(0)
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    input = [16,10,15,5,1,11,7,19,6,12,4]
    return input

def test_day10_part1(puzzle_input):
    input = puzzle_input
    input.append(0)
    one, three = get_num_differences(input)
    assert one == 7
    assert three == 5

def test_day10_part2(puzzle_input):
    input = puzzle_input
    input.append(0)
    s = list(sorted(input))
    assert get_num_reachable(s,{}) == 8
    larger_input=[28,
                33,
                18,
                42,
                31,
                14,
                46,
                20,
                48,
                47,
                24,
                23,
                49,
                45,
                19,
                38,
                39,
                11,
                1,
                32,
                25,
                35,
                8,
                17,
                7,
                9,
                4,
                2,
                34,
                10,
                3]
    s = list(sorted(larger_input))
    s.insert(0,0)
    s.append(s[-1]+3)
    assert get_num_reachable(s,{}) == 19208