from itertools import combinations
from operator import mul
from functools import reduce
from typing import List, Optional, Tuple
from aoc import day, get_num_input

def find_sum_n(expenses: List[int], n: int) -> Tuple[Optional[int], ...]:
    for e in combinations(expenses,n):
        if sum(e) == 2020:
            return e
    return (None, None)

def part1(expenses: List[int]) -> None:
    items = find_sum_n(expenses,2)
    print(f"Day {day()}, Part 1: {reduce(mul,items)}")

def part2(expenses: List[int]) -> None:
    items = find_sum_n(expenses,3)
    print(f"Day {day()}, Part 2: {reduce(mul,items)}")

if __name__ == "__main__":
    expenses = get_num_input(f'input{day()}.txt')
    part1(expenses)
    part2(expenses)

def test_day1_part1():
    assert find_sum_n([1721,979,366,299,675,1456],2) == (1721, 299)

def test_day1_part2():
    assert find_sum_n([1721,979,366,299,675,1456],3) == (979, 366, 675)