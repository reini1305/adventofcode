import pytest
from typing import List
from aoc import day, get_input


def get_winning_numbers(input: str) -> List[int]:
    _, numbers_str = input.split(':')
    winning_numbers_str, numbers_have_str = numbers_str.split('|')
    winning_numbers_have = []
    winning_numbers = set()
    for w in winning_numbers_str.split(' '):
        try:
            winning_numbers.add(int(w))
        except ValueError:
            pass
    for h in numbers_have_str.split(' '):
        try:
            if int(h) in winning_numbers:
                winning_numbers_have.append(int(h))
        except ValueError:
            pass
    return winning_numbers_have


def part1(input: List[str]) -> int:
    result = 0
    for line in input:
        wn = len(get_winning_numbers(line))
        if wn > 0:
            result += 2**(wn - 1)
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    game_points = {}
    for i, line in enumerate(input):
        game_points[i] = len(get_winning_numbers(line))

    multipliers = [1] * len(game_points)
    for game in game_points:
        won = game_points[game]
        for g in range(game + 1, game + won + 1):
            multipliers[g] += multipliers[game]
    result = sum(multipliers)
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
        'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
        'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
        'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
        'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
        'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
    ]


def test_day4_part1(puzzle_input):
    assert get_winning_numbers(puzzle_input[0]) == [83, 86, 17, 48]
    assert part1(puzzle_input) == 13


def test_day4_part2(puzzle_input):
    assert part2(puzzle_input) == 30
