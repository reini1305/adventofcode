import pytest
from typing import List
from aoc import day, get_input, tuple_add


def getEquations(input: List[str]):
    equations = []
    a = (0, 0)
    b = (0, 0)
    prize = (0, 0)
    for line in input:
        if 'A' in line:
            a = (int(line.split(' ')[2][2:-1]), int(line.split(' ')[3][2:]))
        elif 'B' in line:
            b = (int(line.split(' ')[2][2:-1]), int(line.split(' ')[3][2:]))
        elif 'Prize' in line:
            prize = (int(line.split(' ')[1][2:-1]), int(line.split(' ')[2][2:]))
        else:
            equations.append((a, b, prize))
    equations.append((a, b, prize))
    return equations


def solveEquation(equation, part2=False): 
    a, b, prize = equation
    if part2:
        prize = tuple_add(prize, (10_000_000_000_000, 10_000_000_000_000))
    A_moves = (prize[0] * b[1] - prize[1] * b[0]) / (a[0] * b[1] - a[1] * b[0])
    B_moves = (prize[1] * a[0] - prize[0] * a[1]) / (a[0] * b[1] - a[1] * b[0])
    if int(A_moves) == A_moves and int(B_moves) == B_moves:
        return int(3 * A_moves + B_moves)
    return 0


def part1(input: List[str]) -> int:
    result = 0
    equations = getEquations(input)
    for equation in equations:
        result += solveEquation(equation)
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    equations = getEquations(input)
    for equation in equations:
        result += solveEquation(equation, True)
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        'Button A: X+94, Y+34',
        'Button B: X+22, Y+67',
        'Prize: X=8400, Y=5400',
        '',
        'Button A: X+26, Y+66',
        'Button B: X+67, Y+21',
        'Prize: X=12748, Y=12176',
        '',
        'Button A: X+17, Y+86',
        'Button B: X+84, Y+37',
        'Prize: X=7870, Y=6450',
        '',
        'Button A: X+69, Y+23',
        'Button B: X+27, Y+71',
        'Prize: X=18641, Y=10279',
    ]


def test_day13_part1(puzzle_input):
    assert part1(puzzle_input) == 480


def test_day13_part2(puzzle_input):
    assert part2(puzzle_input) == 875318608908
