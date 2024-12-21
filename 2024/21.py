from itertools import permutations
import pytest
from typing import Dict, List, Tuple
from aoc import day, get_input
import numpy as np
from numpy.typing import NDArray


DIRECTIONS = {
    "^": np.array([-1, 0]),
    "v": np.array([1, 0]),
    "<": np.array([0, -1]),
    ">": np.array([0, 1]),
}
POSITIONS = {
    "7": np.array([0, 0]),
    "8": np.array([0, 1]),
    "9": np.array([0, 2]),
    "4": np.array([1, 0]),
    "5": np.array([1, 1]),
    "6": np.array([1, 2]),
    "1": np.array([2, 0]),
    "2": np.array([2, 1]),
    "3": np.array([2, 2]),
    "0": np.array([3, 1]),
    "A": np.array([3, 2]),
    "^": np.array([0, 1]),
    "a": np.array([0, 2]),
    "<": np.array([1, 0]),
    "v": np.array([1, 1]),
    ">": np.array([1, 2]),
}


def seeToMoveSet(start: NDArray, fin: NDArray, avoid=np.array([0, 0])):
    delta = fin - start
    string = ""
    dx, dy = delta

    # Generate moves
    if dx < 0:
        string += "^" * abs(dx)
    else:
        string += "v" * dx
    if dy < 0:
        string += "<" * abs(dy)
    else:
        string += ">" * dy

    # Generate unique permutations of moves
    rv = [
        "".join(p) + "a"
        for p in set(permutations(string))
        if not any(
            (sum(DIRECTIONS[move] for move in p[:i]) + start == avoid).all()
            for i in range(len(p))
        )
    ]

    return rv if rv else ["a"]


def minLength(code: str, memoization: Dict[Tuple[str, int, int], int], lim=2, depth=0) -> int:
    key = (code, depth, lim)
    if key in memoization:
        return memoization[key]

    avoid = np.array([3, 0]) if depth == 0 else np.array([0, 0])
    cur = POSITIONS["A"] if depth == 0 else POSITIONS["a"]
    length = 0

    for char in code:
        nextCurrent = POSITIONS[char]
        moveSet = seeToMoveSet(cur, nextCurrent, avoid)
        if depth == lim:
            length += len(moveSet[0])
        else:
            length += min(minLength(move, memoization, lim, depth + 1) for move in moveSet)
        cur = nextCurrent

    memoization[key] = length
    return length


def sumOfFiveCodeComplexities(input: List[str], lim=2) -> int:
    complexityA = 0
    memo: Dict[Tuple[str, int, int], int] = {}
    for code in input:
        lengthA = minLength(code, memo, lim)
        numeric = int(code[:3])
        complexityA += lengthA * numeric
    return complexityA


def part1(input: List[str]) -> int:
    result = sumOfFiveCodeComplexities(input)
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = sumOfFiveCodeComplexities(input, 25)
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return ['029A', '980A', '179A', '456A', '379A']


def test_day21_part1(puzzle_input):
    assert part1(puzzle_input) == 126384


def test_day21_part2(puzzle_input):
    assert part2(puzzle_input) == 154115708116294
