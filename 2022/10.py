import pytest
from typing import List
from aoc import day, get_input

def vm(input: List[str]) -> List[int]:
    register_x:List[int] = [1]
    for instruction in input:
        command = instruction.strip().split(' ')
        if command[0] == 'noop':
            register_x.append(register_x[-1])
        elif command[0] == 'addx':
            register_x.append(register_x[-1])
            register_x.append(register_x[-1] + int(command[1]))
    return register_x

def draw_on_crt(register_x:List[int])->List[str]:
    output:List[str] = [""]
    curr_line = 0
    for cycle, sprite_pos in enumerate(register_x):
        if cycle > 0 and cycle % 40 == 0:
            # new line
            curr_line += 1
            output.append("")
        x = cycle % 40
        if x in [sprite_pos - 1, sprite_pos, sprite_pos + 1]:
            output[-1] += '#'
        else:
            output[-1] += '.'
    return output

def part1(input: List[str])-> None:
    cycles = [20, 60, 100, 140, 180, 220]
    register_x = vm(input)
    result = sum([register_x[c-1] * c for c in cycles])
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    register_x = vm(input)
    result = draw_on_crt(register_x)
    print(f'Day {day()}, Part 2:')
    for line in result:
        print(line)

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        "addx 15",
        "addx -11",
        "addx 6",
        "addx -3",
        "addx 5",
        "addx -1",
        "addx -8",
        "addx 13",
        "addx 4",
        "noop",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx -35",
        "addx 1",
        "addx 24",
        "addx -19",
        "addx 1",
        "addx 16",
        "addx -11",
        "noop",
        "noop",
        "addx 21",
        "addx -15",
        "noop",
        "noop",
        "addx -3",
        "addx 9",
        "addx 1",
        "addx -3",
        "addx 8",
        "addx 1",
        "addx 5",
        "noop",
        "noop",
        "noop",
        "noop",
        "noop",
        "addx -36",
        "noop",
        "addx 1",
        "addx 7",
        "noop",
        "noop",
        "noop",
        "addx 2",
        "addx 6",
        "noop",
        "noop",
        "noop",
        "noop",
        "noop",
        "addx 1",
        "noop",
        "noop",
        "addx 7",
        "addx 1",
        "noop",
        "addx -13",
        "addx 13",
        "addx 7",
        "noop",
        "addx 1",
        "addx -33",
        "noop",
        "noop",
        "noop",
        "addx 2",
        "noop",
        "noop",
        "noop",
        "addx 8",
        "noop",
        "addx -1",
        "addx 2",
        "addx 1",
        "noop",
        "addx 17",
        "addx -9",
        "addx 1",
        "addx 1",
        "addx -3",
        "addx 11",
        "noop",
        "noop",
        "addx 1",
        "noop",
        "addx 1",
        "noop",
        "noop",
        "addx -13",
        "addx -19",
        "addx 1",
        "addx 3",
        "addx 26",
        "addx -30",
        "addx 12",
        "addx -1",
        "addx 3",
        "addx 1",
        "noop",
        "noop",
        "noop",
        "addx -9",
        "addx 18",
        "addx 1",
        "addx 2",
        "noop",
        "noop",
        "addx 9",
        "noop",
        "noop",
        "noop",
        "addx -1",
        "addx 2",
        "addx -37",
        "addx 1",
        "addx 3",
        "noop",
        "addx 15",
        "addx -21",
        "addx 22",
        "addx -6",
        "addx 1",
        "noop",
        "addx 2",
        "addx 1",
        "noop",
        "addx -10",
        "noop",
        "noop",
        "addx 20",
        "addx 1",
        "addx 2",
        "addx 2",
        "addx -6",
        "addx -11",
        "noop",
        "noop",
        "noop",
    ]

def test_day10_part1(puzzle_input):
    register_x = vm(puzzle_input)
    assert register_x[20-1] == 21
    assert register_x[60-1] == 19
    assert register_x[100-1] == 18
    assert register_x[140-1] == 21
    assert register_x[180-1] == 16
    assert register_x[220-1] == 18
    cycles = [20, 60, 100, 140, 180, 220]
    assert sum([register_x[c-1] * c for c in cycles]) == 13140

def test_day10_part2(puzzle_input):
    assert 1