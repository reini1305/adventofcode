import pytest
from typing import List, Tuple
from tqdm import tqdm
from aoc import day, get_input


def get_mappings(input: List[str]) -> List[List[Tuple[int, int, int]]]:
    mappings: List[List[Tuple[int, int, int]]] = []
    curr_mapping: List[Tuple[int, int, int]] = []
    for line in input:
        if line.startswith('seeds:'):
            continue
        elif line == '':
            if curr_mapping:
                mappings.append(curr_mapping)
            curr_mapping = []
        elif line[0].isdigit():
            dest_start, source_start, length = line.split()
            ss = int(source_start)
            ds = int(dest_start)
            le = int(length)
            curr_mapping.append((ds, ss, le))
        else:
            continue  # Description
    mappings.append(curr_mapping)
    return mappings


def get_seeds(input: List[str]) -> List[int]:
    for line in input:
        if line.startswith('seeds:'):
            _, seed_str = line.split(': ')
            return [int(x) for x in seed_str.split()]
    return []


def traverse_mappings(start: int, mappings: List[List[Tuple[int, int, int]]]) -> int:
    source = start
    dest = source
    for mapping in mappings:
        for (ds, ss, le) in mapping:
            if source >= ss and source < ss + le:
                dest = ds + (source - ss)
                break
        else:
            dest = source
        source = dest
    return dest


def part1(input: List[str]) -> int:
    result = 1000000000
    seeds = get_seeds(input)
    mappings = get_mappings(input)
    for seed in seeds:
        result = min(result, traverse_mappings(seed, mappings))
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 1000000000
    seeds = get_seeds(input)
    mappings = get_mappings(input)
    for s in tqdm(range(0, len(seeds), 2)):
        for seed in range(seeds[s], seeds[s] + seeds[s + 1]):
            result = min(result, traverse_mappings(seed, mappings))
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
    assert traverse_mappings(seeds[1], mappings) == 43
    assert traverse_mappings(seeds[2], mappings) == 86
    assert traverse_mappings(seeds[3], mappings) == 35
    assert part1(puzzle_input) == 35


def test_day5_part2(puzzle_input):
    assert part2(puzzle_input) == 46
