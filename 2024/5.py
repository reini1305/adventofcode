import pytest
from typing import Dict, List, Tuple
from aoc import day, get_input


def getRulesAndUpdates(input: List[str]) -> Tuple[List[Tuple[int, int]], List[Dict[int, int]]]:
    rules: List[Tuple[int, int]] = []
    updates: List[Dict[int, int]] = []

    parse_rules = True
    for line in input:
        if line == "":
            parse_rules = False
        elif parse_rules:
            r = list(map(int, line.split('|')))
            rules.append((r[0], r[1]))
        else:
            update = {}
            for i, item in enumerate(line.split(',')):
                update[int(item)] = i
            updates.append(update)
    return rules, updates


def checkUpdate(update: Dict[int, int], rules: List[Tuple[int, int]]) -> Tuple[bool, Dict[int, int]]:
    for rule in rules:
        try:
            if update[rule[0]] > update[rule[1]]:
                temp = update[rule[0]]
                update[rule[0]] = update[rule[1]]
                update[rule[1]] = temp
                return False, update
        except KeyError:
            pass
    return True, update


def part1(input: List[str]) -> int:
    result = 0
    rules, updates = getRulesAndUpdates(input)
    for update in updates:
        if checkUpdate(update, rules)[0]:
            result += list(update.keys())[list(update.values()).index(len(update)//2)]
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    rules, updates = getRulesAndUpdates(input)
    for update in updates:
        status, update = checkUpdate(update, rules)
        if not status:
            while not status:
                status, update = checkUpdate(update, rules)
            result += list(update.keys())[list(update.values()).index(len(update)//2)]
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        '47|53',
        '97|13',
        '97|61',
        '97|47',
        '75|29',
        '61|13',
        '75|53',
        '29|13',
        '97|29',
        '53|29',
        '61|53',
        '97|53',
        '61|29',
        '47|13',
        '75|47',
        '97|75',
        '47|61',
        '75|61',
        '47|29',
        '75|13',
        '53|13',
        '',
        '75,47,61,53,29',
        '97,61,53,29,13',
        '75,29,13',
        '75,97,47,61,53',
        '61,13,29',
        '97,13,75,29,47',
    ]


def test_day5_part1(puzzle_input):
    rules, updates = getRulesAndUpdates(puzzle_input)
    assert rules[0] == (47, 53)
    assert updates[0][75] == 0
    assert checkUpdate(updates[0], rules)[0]
    assert checkUpdate(updates[1], rules)[0]
    assert checkUpdate(updates[2], rules)[0]
    assert not checkUpdate(updates[3], rules)[0]
    assert not checkUpdate(updates[4], rules)[0]
    assert not checkUpdate(updates[5], rules)[0]
    assert part1(puzzle_input) == 143


def test_day5_part2(puzzle_input):
    assert part2(puzzle_input) == 123
