import pytest
from typing import List, Tuple
from aoc import day, get_input


def getProgram(input: List[str]) -> Tuple[Tuple[int, int, int], List[int]]:
    A = int(input[0].split()[-1])
    B = int(input[1].split()[-1])
    C = int(input[2].split()[-1])
    program = [int(c) for c in input[4].split(' ')[1].split(',')]
    return (A, B, C), program


def execute(A: int, B: int, C: int, program: List[int]) -> List[int]:
    output = []
    ip = 0
    while ip < len(program) - 1:
        instruction = program[ip]
        literal_operand = program[ip + 1]
        combo_operand = literal_operand
        match literal_operand:
            case 4:
                combo_operand = A
            case 5:
                combo_operand = B
            case 6:
                combo_operand = C
            case _:
                pass
        match instruction:
            case 0:  # adv
                A = A // 2**combo_operand
            case 1:  # bxl
                B = B ^ literal_operand
            case 2:  # bst
                B = combo_operand % 8
            case 3:  # jnz
                if A:
                    ip = literal_operand
                    continue
            case 4:  # bxc
                B = B ^ C
            case 5:  # out
                output.append(combo_operand % 8)
            case 6:  # bdv
                B = A // 2**combo_operand
            case 7:  # cdv
                C = A // 2**combo_operand
        ip += 2
    return output


def part1(input: List[str]) -> str:
    registers, program = getProgram(input)
    result = ','.join(map(str, execute(*registers, program)))
    print(f'Day {day()}, Part 1: {result}')
    return result


def getBestQuineInput(program, cursor, sofar):
    for candidate in range(8):
        if execute(sofar * 8 + candidate, 0, 0, program) == program[cursor:]:
            if cursor == 0:
                return sofar * 8 + candidate
            ret = getBestQuineInput(program, cursor - 1, sofar * 8 + candidate)
            if ret is not None:
                return ret
    return None


def part2(input: List[str]) -> int:
    _, program = getProgram(input)
    result = getBestQuineInput(program, len(program) - 1, 0)
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        'Register A: 729',
        'Register B: 0',
        'Register C: 0',
        '',
        'Program: 0,1,5,4,3,0',
    ]


def test_day17_part1(puzzle_input):
    assert part1(puzzle_input) == '4,6,3,5,6,3,5,2,1,0'


def test_day17_part2():
    input = [
        'Register A: 2024',
        'Register B: 0',
        'Register C: 0',
        '',
        'Program: 0,3,5,4,3,0',]
    assert part2(input) == 117440
