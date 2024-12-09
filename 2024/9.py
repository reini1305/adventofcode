import pytest
from typing import Dict, List, Tuple
from aoc import day, get_input


def getBlocks(input: List[str]) -> List[int]:
    blocks: List[int] = []

    is_block = True
    id = 0
    for line in input:
        for c in line:
            for _ in range(int(c)):
                if is_block:
                    blocks.append(id)
                else:
                    blocks.append(-1)
            if is_block:
                id += 1
            is_block = not is_block
    return blocks


def getFiles(input: List[str]) -> Tuple[Dict[int, Tuple[int, int]], Dict[int, Tuple[int, int]]]:
    files: Dict[int, Tuple[int, int]] = dict()
    free: Dict[int, Tuple[int, int]] = dict()

    is_block = True
    id = 0
    pos = 0
    free_id = 0
    for line in input:
        for c in line:
            if is_block:
                files[id] = (pos, int(c))
                id += 1
            else:
                free[free_id] = (pos, int(c))
                free_id += 1
            pos += int(c)
            is_block = not is_block
    return files, free


def defrag(blocks: List[int]) -> List[int]:
    first_free = 0
    while blocks[first_free] != -1:
        first_free += 1
    last_file = len(blocks) - 1
    while blocks[last_file] == -1:
        last_file -= 1
    while first_free < last_file:
        blocks[first_free] = blocks[last_file]
        blocks[last_file] = -1
        while blocks[first_free] != -1:
            first_free += 1
        while blocks[last_file] == -1:
            last_file -= 1
    return blocks


def part1(input: List[str]) -> int:
    result = 0
    blocks = defrag(getBlocks(input))
    for i, file in enumerate(blocks):
        if file != -1:
            result += i * file
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    line = input[0]
    blocks = [(None if i % 2 else i // 2, int(d)) for i, d in enumerate(line)]

    for i in range(len(blocks) - 1, -1, -1):
        for j in range(i):
            i_data, i_size = blocks[i]
            j_data, j_size = blocks[j]

            if i_data is not None and j_data is None and i_size <= j_size:
                blocks[i] = (None, i_size)
                blocks[j] = (None, j_size - i_size)
                blocks.insert(j, (i_data, i_size))

    out = [[data if data else 0] * size for data, size in blocks]

    def flatten(x):
        return [x for x in x for x in x]
    result = sum(i*c for i, c in enumerate(flatten(out)) if c)
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return ['12345']


def test_day9_part1(puzzle_input):
    blocks = getBlocks(puzzle_input)
    assert blocks[0] == 0
    assert blocks[1] == -1
    assert blocks[5] == 1
    assert defrag(blocks) == [0, 2, 2, 1, 1, 1, 2, 2, 2, -1, -1, -1, -1, -1, -1]
    assert part1(['2333133121414131402']) == 1928


def test_day9_part2(puzzle_input):
    files, free = getFiles(puzzle_input)
    assert part2(['2333133121414131402']) == 2858
