from copy import deepcopy
import re
import pytest
from typing import List, Tuple
from aoc import day, get_input


def check_sum(springs: str, checksum: List[int]) -> bool:
    state = (springs[0] == '#')
    curr_count = 0
    checksum_id = 0
    for s in springs:
        if s == '#':
            if state:
                curr_count += 1
            else:
                curr_count = 1
                state = True
        elif s == '.':
            if state:
                if curr_count != checksum[checksum_id]:
                    return False
                state = False
                checksum_id += 1
    return curr_count == checksum[checksum_id]


def expand(springs: List[str]) -> List[List[str]]:
    num_wildcards = springs.count('?')

    output = []
    for state in range(2**num_wildcards):
        output_springs = deepcopy(springs)
        sb = format(state, f'0{num_wildcards}b')
        for i, m in enumerate(re.finditer(r'\?', ''.join(springs))):
            output_springs[m.start()] = '#' if sb[i] == '1' else '.'
        output.append(output_springs)
    return output


def parse_input(input: List[str]) -> List[Tuple[List[str], List[int]]]:
    output = []
    for line in input:
        spring, checksum = line.split(' ')
        checksum_list = [int(i) for i in checksum.split(',')]
        output.append((list(spring), checksum_list))
    return output


def part1(input: List[str]) -> int:
    result = 0
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        '???.### 1,1,3',
        '.??..??...?##. 1,1,3',
        '?#?#?#?#?#?#?#? 1,3,1,6',
        '????.#...#... 4,1,1',
        '????.######..#####. 1,6,5',
        '?###???????? 3,2,1',
    ]


def test_day12_part1(puzzle_input):
    assert check_sum('#.#.###', [1, 1, 3])
    parsed_input = parse_input(puzzle_input)
    expanded = expand(parsed_input[0][0])
    assert sum([check_sum(e, parsed_input[0][1]) for e in expanded]) == 1


def test_day12_part2(puzzle_input):
    assert 1
