import pytest
from typing import List
from aoc import day, get_num_input
from copy import deepcopy

def index_of_zero(number_list):
    for i in range(len(number_list)):
        if number_list[i][1] == 0:
            return i

def mix(input, mix_count=1, multiplier=1):
    number_list = [x for x in enumerate(input)]
    list_size = len(number_list)
    number_list = [(i, n * multiplier) for i, n in number_list]
    initial_list = deepcopy(number_list)
    for _ in range(mix_count):
        for orig in initial_list:
            j = number_list.index(orig)
            num = number_list[j]
            number_list.pop(j)
            if num[1] == -j:
                number_list.append(num)
            else:
                number_list.insert((j + num[1]) % (list_size-1), num)

    zi = index_of_zero(number_list)
    return sum(number_list[(zi + i) % len(number_list)][1] for i in range(1000, 4000, 1000))

def part1(input: List[str])-> None:
    result = mix(input)
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    result = mix(input, 10, 811589153)
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_num_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [1, 2, -3, 3, -2, 0, 4]

def test_day20_part1(puzzle_input):
    assert mix(puzzle_input) == 3

def test_day20_part2(puzzle_input):
    assert mix(puzzle_input, 10, 811589153)== 1623178306