from collections import Counter
import pytest
from typing import List, Tuple
from aoc import day, get_input


def parse_input(input: List[str]) -> List[Tuple[str, int, int]]:
    result = []
    for line in input:
        cards, value = line.split()
        result.append((cards, int(value), get_cards_type(cards)))
    return result


def get_cards_type(cards: str) -> int:
    counts = list(Counter(cards).values())
    # Five of a kind
    if counts == [5]:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts and 2 in counts:
        return 4
    if 3 in counts:
        return 3
    if counts.count(2) == 2:
        return 2
    if 2 in counts:
        return 1
    return 0


def compare_cards(cards1: Tuple[str, int, int], cards2: Tuple[str, int, int]) -> int:
    c1_str, _, val1 = cards1
    c2_str, _, val2 = cards2
    if val1 < val2:
        return -1
    if val1 > val2:
        return 1
    card_strength = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    for c1, c2 in zip(c1_str, c2_str):
        s1 = card_strength.index(c1)
        s2 = card_strength.index(c2)
        if s1 < s2:
            return 1
        if s1 > s2:
            return -1
    return 0


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


def test_day7_part2(puzzle_input):
    assert 1
