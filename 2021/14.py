import pytest
from typing import DefaultDict, Dict, List, Tuple
from typing import Counter as TCounter
from collections import Counter, defaultdict
from aoc import day, get_input

def parse_input(input: List[str])-> Tuple[str,Dict[str,str]]:
    replacements = {}
    for line in input[2:]:
        k,v = line.split(' -> ')
        replacements[k] = v
    return input[0], replacements

def replace(start:str, rules:Dict[str,str], steps:int) -> str:
    output = start
    for s in range(steps):
        replacements = [rules[''.join((a,b))] for a,b in zip(output[:-1],output[1:])]
        last = output[-1]
        output = ''.join([''.join((a,b)) for a,b in zip(output,replacements)]) + last
    return output


def count_replacements(key, rules, step, processed)->DefaultDict[str,int]:
    count:DefaultDict[str,int] = defaultdict(int)
    if step == 0:
        for ch in key:
            count[ch] += 1
        return count

    processed_key = (key, step)
    if processed_key in processed:
        return processed[processed_key]

    mid = rules[key]
    count1 = count_replacements(key[0] + mid, rules, step - 1, processed)
    count2 = count_replacements(mid + key[1], rules, step - 1, processed)

    for ch, idx in count1.items():
        count[ch] += idx
    for ch, idx in count2.items():
        count[ch] += idx
    count[mid] -= 1

    processed[processed_key] = count
    return count

def part1(input: List[str])-> None:
    start, rules = parse_input(input)
    polymer = replace(start,rules,10)
    elements = Counter(polymer).most_common()
    result = elements[0][1] - elements[-1][1]
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    start, rules = parse_input(input)
    counter = Counter()
    processed = {}
    for a,b in zip(start[:-1],start[1:]):
        count = count_replacements(''.join((a,b)), rules, 40, processed)
        counter += Counter(count)
    elements = counter.most_common()
    result = elements[0][1] - elements[-1][1] + 1
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        "NNCB",
        "",
        "CH -> B",
        "HH -> N",
        "CB -> H",
        "NH -> C",
        "HB -> C",
        "HC -> B",
        "HN -> C",
        "NN -> C",
        "BH -> H",
        "NC -> B",
        "NB -> B",
        "BN -> B",
        "BB -> N",
        "BC -> B",
        "CC -> N",
        "CN -> C",
    ]

def test_day14_part1(puzzle_input):
    start, rules = parse_input(puzzle_input)
    assert start == "NNCB"
    rules["NC"] == "B"
    assert replace(start, rules, 1) == "NCNBCHB"
    assert replace(start, rules, 2) =="NBCCNBBBCBHCB"
    elements = Counter(replace(start, rules, 10)).most_common()
    assert elements[0][1] - elements[-1][1] == 1588

def test_day14_part2(puzzle_input):
    start, rules = parse_input(puzzle_input)
    counter = Counter()
    processed = {}
    for a,b in zip(start[:-1],start[1:]):
        count = count_replacements(''.join((a,b)), rules, 40, processed)
        counter += Counter(count)
    elements = counter.most_common()
    assert elements[0][1] ==2192039569602
    assert elements[-1][1] == 3849876073