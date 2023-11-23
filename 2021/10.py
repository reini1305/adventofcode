import pytest
from typing import List
import numpy as np
from aoc import day, get_input

def check_line(input:str)->str:
    closing_mapping = {'(':')', '{':'}','[':']','<':'>'}
    current = []
    for char in input:
        if char in '[{(<':
            current.append(char)
        else:
            top = current.pop()
            if closing_mapping[top] != char:
                return char
    return ''

def autocomplete_line(input:str)->str:
    closing_mapping = {'(':')', '{':'}','[':']','<':'>'}
    current = []
    for char in input:
        if char in '[{(<':
            current.append(char)
        else:
            current.pop()
    return ''.join([closing_mapping[c] for c in reversed(current)])

def part1(input: List[str])-> None:
    map = {')':3, ']':57, '}':1197, '>':25137, '':0}
    result = sum([map[check_line(line)] for line in input])
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> int:
    map = {')':1, ']':2, '}':3, '>':4}
    scores = []
    for line in input:
        if check_line(line) == '':
            complete = autocomplete_line(line)
            score = 0
            for char in complete:
                score = score * 5 + map[char]
            scores.append(score)
    result = int(np.median(np.array(scores)))

    print(f'Day {day()}, Part 2: {result}')
    return result

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]"
    ]

def test_day10_part1(puzzle_input):
    assert check_line(puzzle_input[0]) == ''
    assert check_line(puzzle_input[1]) == ''
    assert check_line(puzzle_input[2]) == '}'

def test_day10_part2(puzzle_input):
    assert autocomplete_line(puzzle_input[0]) == '}}]])})]'
    assert part2(puzzle_input) == 288957