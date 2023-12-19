import pytest
from typing import Dict, List, Tuple
from aoc import day, get_input


def parse_input(input: List[str]) -> Tuple[Dict[str, List[Tuple[str, str]]], List[int]]:
    instructions = {}
    parts = []
    is_instructions = True
    for line in input:
        if line == '':
            is_instructions = False
            continue
        if is_instructions:
            name, rest = line.split('{')
            instruction = [tuple(i.split(':')) for i in rest[:-1].split(',')]
            instructions[name] = instruction
        else:
            parts.append([i.split('=')[1] for i in line[1:-1].split(',')])
    return instructions, parts


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
        'px{a<2006:qkq,m>2090:A,rfg}',
        'pv{a>1716:R,A}',
        'lnx{m>1548:A,A}',
        'rfg{s<537:gd,x>2440:R,A}',
        'qs{s>3448:A,lnx}',
        'qkq{x<1416:A,crn}',
        'crn{x>2662:A,R}',
        'in{s<1351:px,qqz}',
        'qqz{s>2770:qs,m<1801:hdj,R}',
        'gd{a>3333:R,R}',
        'hdj{m>838:A,pv}',
        '',
        '{x=787,m=2655,a=1222,s=2876}',
        '{x=1679,m=44,a=2067,s=496}',
        '{x=2036,m=264,a=79,s=2244}',
        '{x=2461,m=1339,a=466,s=291}',
        '{x=2127,m=1623,a=2188,s=1013}'
    ]


def test_day19_part1(puzzle_input):
    instructions, parts = parse_input(puzzle_input)


def test_day19_part2(puzzle_input):
    assert 1
