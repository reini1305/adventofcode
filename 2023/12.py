from copy import deepcopy
import re
import pytest
from typing import List, Tuple
from aoc import day, get_input


def check_sum(springs: List[str], checksum: List[int]) -> bool:
    state = (springs[0] == '#')
    curr_count = 0
    checksum_id = 0
    for s in springs + ['.']:
        if s == '#':
            if state:
                curr_count += 1
            else:
                curr_count = 1
                state = True
        elif s == '.':
            if state:
                if checksum_id >= len(checksum):
                    return False
                if curr_count != checksum[checksum_id]:
                    return False
                state = False
                checksum_id += 1
    return checksum_id >= len(checksum)


def expand(springs: List[str]) -> List[List[str]]:
    num_wildcards = springs.count('?')
    springs_string = ''.join(springs)
    matches = [m.start() for m in re.finditer(r'\?', springs_string)]
    for state in range(2**num_wildcards):
        output_springs = deepcopy(springs)
        sb = format(state, f'0{num_wildcards}b')
        for i, m in enumerate(matches):
            output_springs[m] = '#' if sb[i] == '1' else '.'
        yield output_springs


def parse_input(input: List[str]) -> List[Tuple[List[str], List[int]]]:
    output = []
    for line in input:
        spring, checksum = line.split(' ')
        checksum_list = [int(i) for i in checksum.split(',')]
        output.append((list(spring), checksum_list))
    return output


def part1(input: List[str]) -> int:
    result = 0
    parsed_input = parse_input(input)
    for springs, checksum in parsed_input:
        result += sum([check_sum(e, checksum) for e in expand(springs)])
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
    parsed_input = parse_input(puzzle_input)
    assert sum([check_sum(e, parsed_input[0][1]) for e in expand(parsed_input[0][0])]) == 1
    assert sum([check_sum(e, parsed_input[1][1]) for e in expand(parsed_input[1][0])]) == 4
    assert sum([check_sum(e, parsed_input[2][1]) for e in expand(parsed_input[2][0])]) == 1
    assert sum([check_sum(e, parsed_input[3][1]) for e in expand(parsed_input[3][0])]) == 1
    assert sum([check_sum(e, parsed_input[4][1]) for e in expand(parsed_input[4][0])]) == 4
    assert sum([check_sum(e, parsed_input[5][1]) for e in expand(parsed_input[5][0])]) == 10
    assert part1(puzzle_input) == 21


def test_day12_part2(puzzle_input):
    assert 1
