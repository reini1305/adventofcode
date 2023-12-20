from collections import deque
from math import gcd
import pytest
from typing import List
from aoc import day, get_input


def parse_input(input: List[str]):
    and_nodes = {}
    flip_flop_nodes = {}
    starter_node = []
    for line in input:
        node_name, connections = line.split(' -> ')
        childs = connections.split(", ")
        if node_name.startswith('&'):
            and_nodes[node_name[1:]] = {'inputs': {}, 'childs': childs}
        elif node_name.startswith('%'):
            flip_flop_nodes[node_name[1:]] = {'state': 0, 'childs': childs}
        else:
            starter_node = childs
    # Iterate second time, add all the inputs to and_nodes
    for line in input:
        node_name, connections = line.split(' -> ')
        childs = connections.split(", ")
        for c in childs:
            if c in and_nodes:
                and_nodes[c]['inputs'][node_name[1:]] = 0
    return starter_node, and_nodes, flip_flop_nodes


def part1(input: List[str]) -> int:
    result = 0
    starter_node, and_nodes, flip_flop_nodes = parse_input(input)
    pulse_count = [0, 0]
    instructions = deque()
    for _ in range(1000):
        # Button press
        pulse_count[0] += 1
        for node in starter_node:
            instructions.append(('broadcaster', node, 0))
            pulse_count[0] += 1
        while instructions:
            source, target, value = instructions.popleft()
            if target in and_nodes:
                and_nodes[target]['inputs'][source] = value
                output = 0 if all(i == 1 for i in and_nodes[target]['inputs'].values()) else 1
                pulse_count[output] += len(and_nodes[target]['childs'])
                for c in and_nodes[target]['childs']:
                    instructions.append((target, c, output))
            elif target in flip_flop_nodes:
                if value == 0:
                    flip_flop_nodes[target]['state'] = 1 if flip_flop_nodes[target]['state'] == 0 else 0
                    pulse_count[flip_flop_nodes[target]['state']] += len(flip_flop_nodes[target]['childs'])
                    for c in flip_flop_nodes[target]['childs']:
                        instructions.append((target, c, flip_flop_nodes[target]['state']))
            else:
                pass
    result = pulse_count[0] * pulse_count[1]
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    starter_node, and_nodes, flip_flop_nodes = parse_input(input)
    instructions = deque()
    loop = {}
    for iter in range(10000):
        # Button press
        result += 1
        for node in starter_node:
            instructions.append(('broadcaster', node, 0))
        while instructions:
            source, target, value = instructions.popleft()
            if target in and_nodes:
                and_nodes[target]['inputs'][source] = value
                output = 0 if all(i == 1 for i in and_nodes[target]['inputs'].values()) else 1
                for c in and_nodes[target]['childs']:
                    instructions.append((target, c, output))
                if target == 'gf' and value:
                    if source not in loop:
                        loop[source] = iter + 1
            elif target in flip_flop_nodes:
                if value == 0:
                    flip_flop_nodes[target]['state'] = 1 if flip_flop_nodes[target]['state'] == 0 else 0
                    for c in flip_flop_nodes[target]['childs']:
                        instructions.append((target, c, flip_flop_nodes[target]['state']))
            else:
                pass
    lcm = 1
    for lo in loop.values():
        lcm = lcm * lo // gcd(lcm, lo)
    result = lcm
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        'broadcaster -> a',
        '%a -> inv, con',
        '&inv -> b',
        '%b -> con',
        '&con -> output'
    ]


def test_day20_part1(puzzle_input):
    starter_node, and_nodes, flip_flop_nodes = parse_input(puzzle_input)
    assert len(and_nodes) == 2
    assert len(flip_flop_nodes) == 2
    assert part1(puzzle_input) == 11687500
    assert part1([
        'broadcaster -> a, b, c',
        '%a -> b',
        '%b -> c',
        '%c -> inv',
        '&inv -> a'
    ]) == 32000000


def test_day20_part2(puzzle_input):
    assert 1
