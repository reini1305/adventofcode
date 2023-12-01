import pytest
from typing import List
from aoc import day, get_input

def getdigits(input: str)->str:
    return ''.join([i if i.isdigit() else '' for i in input])

def part1(input: List[str])-> int:
    result = 0
    for line in input:
        digits = getdigits(line)
        result += int(digits[0])*10 + int(digits[-1])
    print(f'Day {day()}, Part 1: {result}')
    return result

def replacewrittendigits(input: str)->str:
    numbers = {
        "oneight": "18",
        "twone": "21",
        "threeight": "38",
        "fiveight": "58",
        "sevenine": "79",
        "eightwo": "82",
        "eighthree": "83",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for number in numbers:
        input = input.replace(number, numbers[number])
    
    return input

def part2(input: List[str])-> None:
    result = 0
    for line in input:
        digits = getdigits(replacewrittendigits(line))
        result += int(digits[0])*10 + int(digits[-1])
    print(f'Day {day()}, Part 2: {result}')
    return result

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        '1abc2',
        'pqr3stu8vwx',
        'a1b2c3d4e5f',
        'treb7uchet',
        'two1nine',
        'eightwothree',
        'abcone2threexyz',
        'xtwone3four',
        '4nineeightseven2',
        'zoneight234',
        '7pqrstsixteen',
    ]

def test_day1_part1(puzzle_input):
    assert getdigits(puzzle_input[0]) == '12'
    assert getdigits(puzzle_input[1]) == '38'
    assert getdigits(puzzle_input[2]) == '12345'
    assert getdigits(puzzle_input[3]) == '7'
    assert part1(puzzle_input[:4]) == 142

def test_day1_part2(puzzle_input):
    assert replacewrittendigits(puzzle_input[4]) == '219'
    assert replacewrittendigits(puzzle_input[5]) == '823'
    assert replacewrittendigits(puzzle_input[6]) == 'abc123xyz'
    assert replacewrittendigits(puzzle_input[7]) == 'x2134'
    assert replacewrittendigits(puzzle_input[8]) == '49872'
    assert replacewrittendigits(puzzle_input[9]) == 'z18234'
    assert replacewrittendigits(puzzle_input[10]) == '7pqrst6teen'
    assert part2(puzzle_input[4:]) == 281