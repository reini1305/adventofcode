import pytest
from typing import List, Set, Tuple
from copy import deepcopy
from aoc import Assembler, day, get_input

class Day8Assembler(Assembler):
    def __init__(self) -> None:
        super().__init__()

    def run_until_loop(self)->Tuple[int,bool]:
        visited:Set[int] = set()
        while self.ip not in visited and self.ip<len(self.code):
            op, vals = self.code[self.ip]
            visited.add(self.ip)
            op(*vals)
        return (self.accumulator, self.ip>=len(self.code))

def run_until_terminate(code:List[str])->int:
    asm = Day8Assembler()
    modified_instruction = 0
    while modified_instruction < len(code):
        modified_code = deepcopy(code)
        if modified_code[modified_instruction].startswith('jmp'):
            modified_code[modified_instruction] = 'nop' + modified_code[modified_instruction][3:]
        elif modified_code[modified_instruction].startswith('nop'):
            modified_code[modified_instruction] = 'jmp' + modified_code[modified_instruction][3:]
        else:
            modified_instruction += 1
            continue
        asm.decode(modified_code)
        acc, did_terminate = asm.run_until_loop()
        if did_terminate:
            return acc
        modified_instruction += 1
    return 0

def part1(input: List[str])-> None:
    asm = Day8Assembler()
    asm.decode(input)
    print(f'Day {day()}, Part 1: {asm.run_until_loop()[0]}')

def part2(input: List[str])-> None:
    print(f'Day {day()}, Part 2: {run_until_terminate(input)}')

if __name__ == "__main__":
    input = get_input(f'input{day()}.txt')
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    input = ['nop +0',
            'acc +1',
            'jmp +4',
            'acc +3',
            'jmp -3',
            'acc -99',
            'acc +1',
            'jmp -4',
            'acc +6']
    return input

def test_day8_part1(puzzle_input):
    asm = Day8Assembler()
    asm.decode(puzzle_input)
    assert asm.run_until_loop() == (5, False)

def test_day8_part2(puzzle_input):
    assert run_until_terminate(puzzle_input) == 8