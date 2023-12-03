import pytest
from typing import List, Tuple
from aoc import day, get_input


def get_mappings(input: List[str]) -> List[List[Tuple[int, int, int]]]:
    mappings: List[List[Tuple[int, int, int]]] = []
    curr_mapping: List[Tuple[int, int, int]] = []
    for line in input:
        if line.startswith('seeds:'):
            # _, seed_str = line.split(': ')
            # curr_dict = {int(x): int(x) for x in seed_str.split()}
            continue
        elif line == '':
            if curr_mapping:
                mappings.append(curr_mapping)
            curr_mapping = []
        elif line[0].isdigit():
            source_start, dest_start, length = line.split()
            ss = int(source_start)
            ds = int(dest_start)
            le = int(length)
            curr_mapping.append((ss, ds, le))
        else:
            continue  # Description
    return mappings


def get_seeds(input: List[str]) -> List[int]:
    for line in input:
        if line.startswith('seeds:'):
            _, seed_str = line.split(': ')
            return [int(x) for x in seed_str.split()]
    return []


def traverse_mappings(start: int, mappings: List[List[Tuple[int, int, int]]]) -> int:
    return 0


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
    seeds = get_seeds(puzzle_input)
    assert seeds == [79, 14, 55, 13]
    mappings = get_mappings(puzzle_input)
    assert traverse_mappings(seeds[0], mappings) == 82


def test_day5_part2(puzzle_input):
    assert 1
