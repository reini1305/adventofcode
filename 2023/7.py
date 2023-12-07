from collections import Counter
from functools import cmp_to_key
import pytest
from typing import List, Tuple
from aoc import day, get_input


def parse_input(input: List[str], part1=True) -> List[Tuple[str, int, int]]:
    result = []
    for line in input:
        cards, value = line.split()
        result.append((cards, int(value), get_cards_type(cards, part1)))
    return result


def get_cards_type(cards: str, part1=True) -> int:
    card_counts = Counter(cards)
    acm = max(card_counts.values())
    part2 = not part1 and 'J' in cards
    match acm:
        case 5:
            return 6
        case 4:
            return 6 if part2 else 5
        case 1:
            return 1 if part2 else 0
        case 3:
            if len(card_counts.values()) == 2:
                return 6 if part2 else 4
            return 5 if part2 else 3
        case 2:
            if len(card_counts.values()) == 3:
                return 3 + card_counts['J'] if part2 else 2
            return 3 if part2 else 1
    return 0


def compare_cards(cards1: Tuple[str, int, int], cards2: Tuple[str, int, int], part1=True) -> int:
    c1_str, _, val1 = cards1
    c2_str, _, val2 = cards2
    if val1 < val2:
        return -1
    if val1 > val2:
        return 1
    card_strength = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'] if part1 else\
        ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    for c1, c2 in zip(c1_str, c2_str):
        s1 = card_strength.index(c1)
        s2 = card_strength.index(c2)
        if s1 < s2:
            return 1
        if s1 > s2:
            return -1
    return 0


def part1(input: List[str]) -> int:
    sorted_cards = sorted(parse_input(input, True), key=cmp_to_key(lambda a, b: compare_cards(a, b, True)))
    result = sum([i * s[1] for i, s in enumerate(sorted_cards, 1)])
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    sorted_cards = sorted(parse_input(input, False), key=cmp_to_key(lambda a, b: compare_cards(a, b, False)))
    result = sum([i * s[1] for i, s in enumerate(sorted_cards, 1)])
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        '32T3K 765',
        'T55J5 684',
        'KK677 28',
        'KTJJT 220',
        'QQQJA 483',
    ]


def test_day7_part1(puzzle_input):
    cards = parse_input(puzzle_input)
    assert get_cards_type(cards[0][0]) == 1
    assert get_cards_type(cards[1][0]) == 3
    assert get_cards_type(cards[2][0]) == 2
    assert get_cards_type(cards[3][0]) == 2
    assert get_cards_type(cards[4][0]) == 3
    assert compare_cards(cards[2], cards[3]) == 1
    assert part1(puzzle_input) == 6440


def test_day7_part2(puzzle_input):
    cards = parse_input(puzzle_input)
    assert get_cards_type(cards[0][0], False) == 1
    assert get_cards_type(cards[1][0], False) == 5
    assert get_cards_type(cards[2][0], False) == 2
    assert get_cards_type(cards[3][0], False) == 5
    assert get_cards_type(cards[4][0], False) == 5
    assert part2(puzzle_input) == 5905
