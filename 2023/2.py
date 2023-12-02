import pytest
from typing import List, Dict
from aoc import day, get_input


def count_bags(input: str) -> Dict[int, str]:
    result = {"red": 0, "blue": 0, "green": 0}
    game, contents = input.split(':')
    for draw in contents.split(';'):
        for count, color in [x.split() for x in draw.split(',')]:
            result[color] = max(result[color], int(count))
    return result


def part1(input: List[str]) -> int:
    result = 0
    for i, game in enumerate(input):
        bag = count_bags(game)
        if bag['red'] <= 12 and bag['blue'] <= 14 and bag['green'] <= 13:
            result += i + 1
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    for game in input:
        bag = count_bags(game)
        result += bag['red'] * bag['blue'] * bag['green']
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
        'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
        'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
        'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
    ]


def test_day2_part1(puzzle_input):
    bags = count_bags(puzzle_input[0])
    assert bags['red'] == 4
    assert bags['blue'] == 6
    assert bags['green'] == 2
    assert part1(puzzle_input) == 8


def test_day2_part2(puzzle_input):
    assert part2(puzzle_input) == 2286
