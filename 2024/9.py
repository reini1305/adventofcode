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


def defragFiles(blocks: List[int],
                files: Dict[int, Tuple[int, int]],
                free: Dict[int, Tuple[int, int]]) -> List[int]:
    for file in reversed(list(files.keys())):
        pos, size = files[file]
        # get first free space with size of file
        next_free_id = 0
        try:
            while free[next_free_id][1] < size:
                next_free_id += 1
        except KeyError:
            continue
        pos_free, size_free = free[next_free_id]
        for i in range(size):
            blocks[pos_free + i] = file
            blocks[pos + i] = -1
        free[next_free_id] = (pos_free + size, size_free - size)

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
    blocks = defragFiles(getBlocks(input), *getFiles(input))
    for i, file in enumerate(blocks):
        if file != -1:
            result += i * file
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
