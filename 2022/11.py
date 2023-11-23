from collections import deque
from copy import deepcopy
from math import gcd
import pytest
from typing import Deque, List, Optional
from tqdm import tqdm
from aoc import day

class Monkey:
    def __init__(self, items, operation, divisible_by, true_monkey, false_monkey) -> None:
        self.items:Deque[int] = deque(items)
        self.operation = operation
        self.divisible_by = divisible_by
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

    def throw(self, lcm_num=0) -> Optional[int]:
        if not self.items:
            return None, None
        item = self.operation(self.items.popleft())
        if lcm_num != 0:
            item %= lcm_num
        else:
            item //= 3
        if item % self.divisible_by == 0:
            monkey = self.true_monkey
        else:
            monkey = self.false_monkey
        return monkey, item

    def add_item(self, item):
        self.items.append(item)

def lcm(a,b):
  return (a * b) // gcd(a,b)

def play_round(monkeys:List[Monkey], lcm_num=0):
    throws = [0] * len(monkeys)
    for i, monkey in enumerate(monkeys):
        # play until there is no move left
        throw_monkey, item = monkey.throw(lcm_num)
        while throw_monkey is not None:
            monkeys[throw_monkey].add_item(item)
            throws[i] += 1
            throw_monkey, item = monkey.throw()
    return throws

def part1(input: List[Monkey])-> None:
    monkeys = deepcopy(input)
    throws = [0] * len(monkeys)
    for _ in range(20):
        throws = [a+b for a,b in zip(throws, play_round(monkeys))]
    throws = sorted(throws, reverse=True)
    result = throws[0] * throws[1]
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[Monkey])-> None:
    monkeys = deepcopy(input)
    throws = [0] * len(monkeys)
    # Find the LCM of all operations
    lcm_all = 1
    for m in monkeys:
        lcm_all = lcm(m.divisible_by, lcm_all)
    for _ in range(10000):
        throws = [a+b for a,b in zip(throws, play_round(monkeys, lcm_all))]
    throws = sorted(throws, reverse=True)
    result = throws[0] * throws[1]
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = [
        Monkey([91, 66],lambda x: x*13, 19, 6, 2),
        Monkey([78, 97, 59],lambda x: x+7, 5, 0, 3),
        Monkey([57, 59, 97, 84, 72, 83, 56, 76],lambda x: x+6, 11, 5, 7),
        Monkey([81, 78, 70, 58, 84],lambda x: x+5, 17, 6, 0),
        Monkey([60],lambda x: x+8, 7, 1, 3),
        Monkey([57, 69, 63, 75, 62, 77, 72],lambda x: x*5, 13, 7, 4),
        Monkey([73, 66, 86, 79, 98, 87],lambda x: x*x, 3, 5, 2),
        Monkey([95, 89, 63, 67],lambda x: x+2, 2, 1, 4)
    ]
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        Monkey([79, 98],lambda x: x*19, 23, 2, 3),
        Monkey([54, 65, 75, 74],lambda x: x+6, 19, 2, 0),
        Monkey([79, 60, 97],lambda x: x*x, 13, 1, 3),
        Monkey([74],lambda x: x+3, 17, 0, 1)
    ]

def test_day11_part1(puzzle_input:List[Monkey]):
    throws = [0] * len(puzzle_input)
    for _ in range(20):
        throws = [a+b for a,b in zip(throws, play_round(puzzle_input))]
    throws = sorted(throws, reverse=True)
    result = throws[0] * throws[1]
    assert result == 10605

def test_day11_part2(puzzle_input):
    throws = [0] * len(puzzle_input)
    # Find the LCM of all operations
    lcm_all = 1
    for m in puzzle_input:
        lcm_all = lcm(m.divisible_by, lcm_all)
    for _ in range(20):
        throws = [a+b for a,b in zip(throws, play_round(puzzle_input, lcm_all))]
    throws = sorted(throws, reverse=True)
    result = throws[0] * throws[1]
    assert result == 2713310158