import pytest
from typing import List, Tuple
from aoc import day, get_input


def nCrossZero(start: int, move: int) -> int:
    # full rotations
    n_rots = abs(move) // 100
    # remove those full rotations
    move = move - n_rots * 100 if move > 0 else move + n_rots * 100
    # count crossing if we got past 0, but only if we didn't start at 0
    n_rots += abs((start + move) // 100) if start > 0 else 0
    # if we ended at zero we count it as crossing (here, not in the next
    # iteration)
    n_rots += (start + move) == 0
    return n_rots


def turnDial(instructions: List[str]) -> Tuple[List[int], int]:
    output: List[int] = [50]
    overflows = 0
    for i in instructions:
        if i.startswith('L'):
            turn = -int(i[1:])
        else:
            turn = int(i[1:])
        overflows += nCrossZero(output[-1], turn)
        output.append((output[-1] + turn) % 100)
    return output, overflows


def part1(input: List[str]) -> int:
    positions, _ = turnDial(input)
    result = sum([1 if p == 0 else 0 for p in positions])
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    _, overflows = turnDial(input)
    result = overflows
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]


def test_day1_part1(puzzle_input):
    assert part1(puzzle_input) == 3


def test_day1_part2(puzzle_input):
    assert part2(puzzle_input) == 6
