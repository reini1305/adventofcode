import pytest
from typing import Dict, List
from aoc import day, get_input


def get_mappings(input: List[str]) -> List[Dict[int, int]]:
    mappings: List[Dict[int, int]] = []
    curr_dict = {}
    for line in input:
        if line.startswith('seeds:'):
            _, seed_str = line.split(': ')
            curr_dict = {int(x): int(x) for x in seed_str.split()}
        elif line == '':
            mappings.append(curr_dict)
            curr_dict = {}
        elif line[0].isdigit():
            source_start, dest_start, length = line.split()
            ss = int(source_start)
            ds = int(dest_start)
            le = int(length)
            for s, d in zip(range(ss, ss + le), range(ds, ds + le)):
                curr_dict[s] = d
        else:
            continue  # Description
    return mappings        


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
        'seeds: 79 14 55 13',
        '',
        'seed-to-soil map:',
        '50 98 2',
        '52 50 48',
        '',
        'soil-to-fertilizer map:',
        '0 15 37',
        '37 52 2',
        '39 0 15',
        '',
        'fertilizer-to-water map:',
        '49 53 8',
        '0 11 42',
        '42 0 7',
        '57 7 4',
        '',
        'water-to-light map:',
        '88 18 7',
        '18 25 70',
        '',
        'light-to-temperature map:',
        '45 77 23',
        '81 45 19',
        '68 64 13',
        '',
        'temperature-to-humidity map:',
        '0 69 1',
        '1 0 69',
        '',
        'humidity-to-location map:',
        '60 56 37',
        '56 93 4',
    ]


def test_day5_part1(puzzle_input):
    get_mappings(puzzle_input)


def test_day5_part2(puzzle_input):
    assert 1
