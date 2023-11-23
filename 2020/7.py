import pytest
from typing import Dict, List, Set, Tuple
import aoc

def parse_contains(input:List[str])-> Tuple[Dict[str,List[Tuple[str,int]]],Dict[str,List[str]]]:
    contains: Dict[str,List[Tuple[str,int]]] = {}
    contained_by: Dict[str,List[str]] = {}
    for line in input:
        outer, inner = line.strip('.').split('contain')
        inner_bags = inner.split(',')
        outer_color = ' '.join(outer.split()[:2])
        contains[outer_color] = []
        if inner_bags[0].startswith(' no'):
            continue
        for bag in inner_bags:
            inner_color = ' '.join(bag.split()[1:3])
            inner_count = int(bag.split()[0])
            contains[outer_color].append((inner_color,inner_count))
            if inner_color not in contained_by:
                contained_by[inner_color] = []
            contained_by[inner_color].append(outer_color)
    return contains, contained_by

def contained_by(data:Dict[str,List[str]], bag:str)->Set[str]:
    if bag in data:
        parents = data[bag]
        data.pop(bag)
        output = set()
        for p in parents:
            output.add(p)
            for other in contained_by(data, p):
                output.add(other)
        return output
    else:
        return set()

def part1(input: List[str])-> None:
    _, cb = parse_contains(input)
    print(f'Day {aoc.day()}, Part 1: {len(contained_by(cb, "shiny gold"))}')

def contained_inside_count(data:Dict[str,List[Tuple[str,int]]], bag:str, z:int=1)->int:
    count=0
    for inner in data[bag]:
        count+=inner[1]*z
        count+=contained_inside_count(data, inner[0], inner[1]*z)
    return count

def part2(input: List[str])-> None:
    contains, _ = parse_contains(input)
    print(f'Day {aoc.day()}, Part 2: {contained_inside_count(contains, "shiny gold")}')

if __name__ == "__main__":
    input = aoc.get_input(f'input{aoc.day()}.txt')
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    input = ['light red bags contain 1 bright white bag, 2 muted yellow bags.',
            'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
            'bright white bags contain 1 shiny gold bag.',
            'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
            'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
            'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
            'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
            'faded blue bags contain no other bags.',
            'dotted black bags contain no other bags.']
    return input

def test_day7_part1(puzzle_input):
    input = puzzle_input
    contains, cb = parse_contains(input)
    assert len(contained_by(cb,'shiny gold')) == 4

def test_day7_part2(puzzle_input):
    input = puzzle_input
    contains, _ = parse_contains(input)
    assert contained_inside_count(contains, 'shiny gold')