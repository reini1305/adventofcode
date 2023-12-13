import pytest
from typing import List, Tuple
from aoc import day, get_input
import functools


def parse_input(input: List[str]) -> List[Tuple[List[int], List[int]]]:
    output = []
    to_int = {'.': 0, '#': 1, '?': 2}
    for line in input:
        spring, checksum = line.split(' ')
        checksum_list = [int(i) for i in checksum.split(',')]
        output.append(([to_int[i] for i in spring], checksum_list))
    return output


@functools.cache  # 1000x+ speedup
def arrangements(springs: Tuple[int], checksum: Tuple[int]) -> int:

    # Base cases
    if (len(checksum) == 0):
        return int(sum(c == 1 for c in springs) == 0)
    if sum(checksum) > len(springs):
        return 0

    # One case for .
    if springs[0] == 0:
        return arrangements(springs[1:], checksum)

    no1, no2 = 0, 0
    # possibility to start next tile
    if springs[0] == 2:
        no2 = arrangements(springs[1:], checksum)

    # possibility to start here
    if all(c != 0 for c in springs[:checksum[0]]) and (springs[checksum[0]] if len(springs) > checksum[0] else 0) != 1:
        no1 = arrangements(springs[(checksum[0] + 1):], checksum[1:])

    return no1 + no2


def part1(input: List[str]) -> int:
    result = 0
    parsed_input = parse_input(input)
    for springs, checksum in parsed_input:
        arr = arrangements(tuple(springs), tuple(checksum))
        result += arr
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    parsed_input = parse_input(input)
    for springs, checksum in parsed_input:

        springs = ((springs + [2]) * 5)[:-1]
        checksum *= 5

        arr = arrangements(tuple(springs), tuple(checksum))
        result += arr
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
    assert arrangements(tuple(parsed_input[0][0]), tuple(parsed_input[0][1])) == 1
    assert arrangements(tuple(parsed_input[1][0]), tuple(parsed_input[1][1])) == 4
    assert arrangements(tuple(parsed_input[2][0]), tuple(parsed_input[2][1])) == 1
    assert arrangements(tuple(parsed_input[3][0]), tuple(parsed_input[3][1])) == 1
    assert arrangements(tuple(parsed_input[4][0]), tuple(parsed_input[4][1])) == 4
    assert arrangements(tuple(parsed_input[5][0]), tuple(parsed_input[5][1])) == 10
    assert part1(puzzle_input) == 21


def test_day12_part2(puzzle_input):
    assert part2(puzzle_input) == 525152
