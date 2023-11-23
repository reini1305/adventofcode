from math import ceil, floor
import pytest
from typing import List, Set, Tuple
from aoc import day, get_input

def tuple_add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def tuple_diff(a,b):
    return (a[0] - b[0], a[1] - b[1])

def norm(a):
    return max(abs(a[0]), abs(a[1]))

def tuple_ceil_div(a,div):
    return (
        ceil(a[0]/div) if a[0] > 0 else floor(a[0]/div), 
        ceil(a[1]/div) if a[1] > 0 else floor(a[1]/div)
    )

def update_tail(tail, head):
    d_th = tuple_diff(head, tail)
    # still adjacent, no need to update
    if norm(d_th) <= 1:
        return tail
    return tuple_add(tail, tuple_ceil_div(d_th, 2))

def simulate_rope(input: List[str], length:int) -> int:
    rope = [(0,0)] * (length + 1)
    dir = {'R': (1,0), 'L': (-1,0), 'U': (0,-1), 'D': (0,1)}
    visited:Set[Tuple[int,int]] = set([rope[0]])
    for instruction in input:
        direction, amount = instruction.strip().split(' ')
        for _ in range(int(amount)):
            rope[-1] = tuple_add(rope[-1], dir[direction])
            for i in reversed(range(length)):
                rope[i] = update_tail(rope[i], rope[i+1])
            visited.add(rope[0])
    return len(visited)

def part1(input: List[str])-> None:
    result = simulate_rope(input,1)
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    result = simulate_rope(input,9)
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        "R 4",
        "U 4",
        "L 3",
        "D 1",
        "R 4",
        "D 1",
        "L 5",
        "R 2",
    ]

def test_day9_part1(puzzle_input):
    assert simulate_rope(puzzle_input,1) == 13

def test_day9_part2(puzzle_input):
    assert simulate_rope(puzzle_input,9) == 1
    larger_input = [
        "R 5",
        "U 8",
        "L 8",
        "D 3",
        "R 17",
        "D 10",
        "L 25",
        "U 20",
    ]
    assert simulate_rope(larger_input,9) == 36
