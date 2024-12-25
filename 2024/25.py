import pytest
from typing import List, Tuple
from aoc import day, get_input


def getKeysAndLocks(input: List[str]) -> Tuple[List[List[int]], List[List[int]]]:
    keys = []
    locks = []
    is_key = False
    new_item = True
    current = [0] * len(input[0])
    for line in input:
        if line == '':
            new_item = True
            if is_key:
                current = [c - 1 for c in current]
                keys.append(current)
            else:
                locks.append(current)
            current = [0] * len(input[0])
            continue
        if new_item:
            is_key = '.' in line
            new_item = False
            continue
        num_line = [0 if c == '.' else 1 for c in line]
        current = [c + n for c, n in zip(current, num_line)]
    if is_key:
        current = [c - 1 for c in current]
        keys.append(current)
    else:
        locks.append(current)
    return locks, keys


def part1(input: List[str]) -> int:
    result = 0
    locks, keys = getKeysAndLocks(input)
    for lock in locks:
        for key in keys:
            if all(lo + ke <= 5 for lo, ke in zip(lock, key)):
                result += 1
    print(f'Day {day()}, Part 1: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)


@pytest.fixture
def puzzle_input():
    return [
        '#####',
        '.####',
        '.####',
        '.####',
        '.#.#.',
        '.#...',
        '.....',
        '',
        '#####',
        '##.##',
        '.#.##',
        '...##',
        '...#.',
        '...#.',
        '.....',
        '',
        '.....',
        '#....',
        '#....',
        '#...#',
        '#.#.#',
        '#.###',
        '#####',
        '',
        '.....',
        '.....',
        '#.#..',
        '###..',
        '###.#',
        '###.#',
        '#####',
        '',
        '.....',
        '.....',
        '.....',
        '#....',
        '#.#..',
        '#.#.#',
        '#####',
    ]


def test_day25_part1(puzzle_input):
    assert part1(puzzle_input) == 3
