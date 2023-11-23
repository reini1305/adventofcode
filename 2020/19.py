import pytest
from typing import List, Optional, Tuple,Dict
from aoc import day, get_input

def parse_input(input):
    messages: List[str] = []
    rules = {}
    # parse rules
    for line in input:
        if line == '':
            break
        id, rest = line.split(': ')
        content = [seq.split(' ') for seq in rest.split(' | ')]
        rules[id] = content
    # parse messages
    for line in input:
        if not (line.startswith('a') or line.startswith('b')):
            continue
        messages.append(line)
    return rules, messages

def check(rules, id, sample, start):
    rule = rules[id]
    if rule[0][0][0] == '"':
        return {start + 1} if start < len(sample) and  rule[0][0][1] == sample[start] else set()
    else:
        match = set()
        for subrule in rule:
            rule_match = {start}
            for part in subrule:
                part_match = set()
                for loc in rule_match:
                    part_match |= check(rules, part, sample, loc)
                rule_match = part_match
            match |= rule_match
        return match

def part1(input: List[str])-> None:
    rules , messages = parse_input(input)
    result = sum([1 for m in messages if len(m) in check(rules, '0', m, 0)])
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    rules , messages = parse_input(input)
    rules['8'] = [['42'],['42','8']]
    rules['11'] = [['42','31'],['42','11','31']]
    result = sum([1 for m in messages if len(m) in check(rules, '0', m, 0)])
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input(f'input{day()}.txt')
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    input = ['0: 4 1 5',
            '1: 2 3 | 3 2',
            '2: 4 4 | 5 5',
            '3: 4 5 | 5 4',
            '4: "a"',
            '5: "b"',
            '',
            'ababbb',
            'bababa',
            'abbbab',
            'aaabbb',
            'aaaabbb']
    return input

def test_day19_part1(puzzle_input):
    rules , messages = parse_input(puzzle_input)
    assert sum([1 for m in messages if len(m) in check(rules, '0', m, 0)]) == 2
