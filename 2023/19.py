from copy import deepcopy
from functools import reduce
import operator
import pytest
from typing import Dict, List, Tuple
from aoc import day, get_input


def parse_input(input: List[str]) -> Tuple[Dict[str, List[Tuple[str, str]]], List[List[int]]]:
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
            parts.append([int(i.split('=')[1]) for i in line[1:-1].split(',')])
    return instructions, parts


def run_instructions(instructions: Dict[str, List[Tuple[str, str]]], parts: List[List[int]]) -> List[int]:
    result = []
    for x, m, a, s in parts:
        state = 'in'
        while state not in ['A', 'R']:
            for ins in instructions[state]:
                if len(ins) == 1:
                    state = ins[0]
                    break
                if eval(ins[0]):
                    state = ins[1]
                    break
        result.append(state)
    return result


def pos(var: str) -> int:
    return 'xmas'.index(var)


def replace_range(pos, new_r, orig):
    return [orig[i] if i != pos else new_r for i in range(4)]


def search_space(instructions: Dict[str, List[Tuple[str, str]]], ranges: List[Tuple[int, int]], state: str) -> int:
    if state == 'A':
        return reduce(operator.mul, [(j - i) + 1 for i, j in ranges])
    if state == 'R':
        return 0
    total = 0
    new_ranges = deepcopy(ranges)
    for ins in instructions[state]:
        if len(ins) == 1:
            total += search_space(instructions, new_ranges, ins[0])
        else:
            rule = ins[0]
            ss = "<" if "<" in rule else ">"
            var, val = rule.split(ss)
            rp = pos(var)
            rr = new_ranges[rp]
            val = int(val)
            if val >= rr[0] and val <= rr[1]:
                if ss == ">":
                    total += search_space(instructions, replace_range(rp, (val + 1, rr[1]), new_ranges), ins[1])
                    new_ranges = replace_range(rp, (rr[0], val), new_ranges)
                if ss == "<":
                    total += search_space(instructions, replace_range(rp, (rr[0], val - 1), new_ranges), ins[1])
                    new_ranges = replace_range(rp, (val, rr[1]), new_ranges)
    return total


def part1(input: List[str]) -> int:
    instructions, parts = parse_input(input)
    results = run_instructions(instructions, parts)
    result = 0
    for i, r in enumerate(results):
        if r == 'A':
            result += sum(parts[i])
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    instructions, _ = parse_input(input)
    result = search_space(instructions, [(1, 4_000), (1, 4_000), (1, 4_000), (1, 4_000)], 'in')
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
    assert part1(puzzle_input) == 19114


def test_day19_part2(puzzle_input):
    assert part2(puzzle_input) == 167409079868000
