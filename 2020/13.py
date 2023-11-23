import pytest
from typing import List, Tuple
from aoc import day, get_input
import math
from functools import reduce

def parse_plan(input:List[str])->Tuple[int,List[int]]:
    timestamp = int(input[0])
    ids = [int(i) if i != 'x' else -1 for i in input[1].split(',')]
    return (timestamp, ids)

def get_next_departure_id(input:Tuple[int,List[int]])->int:
    timestamp, ids = input
    earliest_id = [math.ceil(timestamp / id) * id if id > 0 else 10000000 for id in ids]

    return ids[earliest_id.index(min(earliest_id))]

def part1(input: List[str])-> None:
    plan = parse_plan(input)
    id = get_next_departure_id(plan)
    departure = math.ceil(plan[0] / id) * id
    result = id * (departure - plan[0])
    print(f'Day {day()}, Part 1: {result}')

def crt(ns:List[int], a:List[int])->int:
    # Chinese Remainder Theorem
    # https://brilliant.org/wiki/chinese-remainder-theorem/
    N = math.prod(ns)
    x = sum(b * (N // n) * pow(N // n, -1, n) for b, n in zip(a, ns))
    return x % N

def get_next_departure(input:List[int])->int:
    ns = [i for i in input if i > 0]
    a = [n-input.index(n) for n in ns]
    return crt(ns, a)

def part2(input: List[str])-> None:
    plan = parse_plan(input)
    print(f'Day {day()}, Part 2: {get_next_departure(plan[1])}')

if __name__ == "__main__":
    input = get_input(f'input{day()}.txt')
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    plan=(939,[7,13,-1,-1,59,-1,31,19])
    return plan

def test_day13_part1(puzzle_input):
    plan = puzzle_input
    assert get_next_departure_id(plan) == 59

def test_day13_part2(puzzle_input):
    plan = puzzle_input
    assert get_next_departure(plan[1]) == 1068781
    assert get_next_departure([67,7,59,61]) == 754018
    assert get_next_departure([67,-1,7,59,61]) == 779210
    assert get_next_departure([67,7,-1,59,61]) == 1261476
    assert get_next_departure([1789,37,47,1889]) == 1202161486