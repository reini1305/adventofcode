from math import gcd
import pytest
from typing import Dict, List, Tuple
from aoc import day, get_input


def parse_input(input: List[str]) -> Tuple[str, Dict[str, Tuple[str, str]]]:
    instructions = input[0]
    nodes = {}

    for line in input[2:]:
        name, children = line.split(' = ')
        left, right = children.split(', ')
        nodes[name] = (left[1:], right[:-1])

    return instructions, nodes


def follow_instructions(instructions: str, nodes: Dict[str, Tuple[str, str]]) -> int:
    curr = 'AAA'
    ic = 0
    count = 0
    while curr != 'ZZZ':
        curr = nodes[curr][0] if instructions[ic] == 'L' else nodes[curr][1]
        count += 1
        ic = (ic + 1) % len(instructions)
    return count


def follow_instructions_parallel(instructions: str, nodes: Dict[str, Tuple[str, str]]) -> int:
    curr = []
    for n in nodes:
        if n.endswith('A'):
            curr.append(n)
    ic = 0
    count = 0
    loop = [0] * len(curr)
    while not all([lo > 0 for lo in loop]):
        curr = [nodes[c][0] if instructions[ic] == 'L' else nodes[c][1] for c in curr]
        count += 1
        for i, c in enumerate(curr):
            if c.endswith('Z') and loop[i] == 0:
                loop[i] = count
        ic = (ic + 1) % len(instructions)
    lcm = 1
    for lo in loop:
        lcm = lcm * lo // gcd(lcm, lo)
    return lcm


def part1(input: List[str]) -> int:
    result = follow_instructions(*parse_input(input))
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = follow_instructions_parallel(*parse_input(input))
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        'LLR',
        '',
        'AAA = (BBB, BBB)',
        'BBB = (AAA, ZZZ)',
        'ZZZ = (ZZZ, ZZZ)',
    ]


def test_day8_part1(puzzle_input):
    instructions, nodes = parse_input(puzzle_input)
    assert follow_instructions(instructions, nodes) == 6


def test_day8_part2():
    input = [
        'LR',
        '',
        '11A = (11B, XXX)',
        '11B = (XXX, 11Z)',
        '11Z = (11B, XXX)',
        '22A = (22B, XXX)',
        '22B = (22C, 22C)',
        '22C = (22Z, 22Z)',
        '22Z = (22B, 22B)',
        'XXX = (XXX, XXX)',
    ]
    assert follow_instructions_parallel(*parse_input(input)) == 6
