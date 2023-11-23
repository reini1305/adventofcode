import pytest
from typing import List
from aoc import day, get_input

def split_answers(input: List[str])->List[List[str]] :
    output = []
    answer:List[str] = []
    for line in input:
        if line == '':
            output.append(answer)
            answer = []
        else:
            answer.append(line)
    output.append(answer)
    return output

def count_answers(answers: List[str])-> int:
    unique_answers = set()
    for answer in answers:
        for a in answer:
            unique_answers.add(a)
    return len(unique_answers)

def part1(input: List[str])-> None:
    answers = split_answers(input)
    sum_counts = sum([count_answers(a) for a in answers])
    print(f'Day {day()}, Part 1: {sum_counts}')

def count_everyone_answers(answers: List[str])-> int:
    unique_answers = []
    for answer in answers:
        unique_answers.append(set([a for a in answer]))
    all_answers = unique_answers[0].intersection(*unique_answers)
    return len(all_answers)

def part2(input: List[str])-> None:
    answers = split_answers(input)
    sum_counts = sum([count_everyone_answers(a) for a in answers])
    print(f'Day {day()}, Part 2: {sum_counts}')

if __name__ == "__main__":
    input = get_input(f'input{day()}.txt')
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    input = ['abc',
            '',
            'a',
            'b',
            'c',
            '',
            'ab',
            'ac',
            '',
            'a',
            'a',
            'a',
            'a',
            '',
            'b']
    answers = split_answers(input)
    return answers

def test_day6_part1(puzzle_input):
    answers = puzzle_input
    assert len(answers) == 5
    assert count_answers(answers[0]) == 3
    assert count_answers(answers[1]) == 3
    assert count_answers(answers[2]) == 3
    assert count_answers(answers[3]) == 1
    assert count_answers(answers[4]) == 1

def test_day6_part2(puzzle_input):
    answers = puzzle_input
    assert count_everyone_answers(answers[0]) == 3
    assert count_everyone_answers(answers[1]) == 0
    assert count_everyone_answers(answers[2]) == 1
    assert count_everyone_answers(answers[3]) == 1
    assert count_everyone_answers(answers[4]) == 1