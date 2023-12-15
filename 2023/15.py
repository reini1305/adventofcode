from collections import defaultdict
import pytest
from typing import List
from aoc import day, get_input


def hash(input: str) -> int:
    output = 0
    for char in input:
        output += ord(char)
        output *= 17
        output %= 256
    return output


def part1(input: List[str]) -> int:
    result = 0
    for line in input:
        for instruction in line.split(","):
            result += hash(instruction)
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    boxes = defaultdict(dict)
    for line in input:
        for instruction in line.split(","):
            if "=" in instruction:
                key, value = instruction.split("=")
                box = hash(key)
                boxes[box][key] = value
            else:
                key = instruction[:-1]
                box = hash(key)
                try:
                    del boxes[box][key]
                except KeyError:
                    pass
    for box in boxes:
        for slot, lens in enumerate(boxes[box]):
            result += (1 + box) * (1 + slot) * int(boxes[box][lens])
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return ["rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"]


def test_day15_part1(puzzle_input):
    assert hash("HASH") == 52
    assert part1(puzzle_input) == 1320


def test_day15_part2(puzzle_input):
    assert part2(puzzle_input) == 145
