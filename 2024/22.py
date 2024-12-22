from collections import defaultdict
import pytest
from typing import DefaultDict, List, Optional, Tuple
from aoc import day, get_num_input


def simulate(start: int, steps: int) -> int:
    for _ in range(steps):
        start = ((start * 64) ^ start) % 16777216
        start = ((start // 32) ^ start) % 16777216
        start = ((start * 2048) ^ start) % 16777216
    return start


def part2(input: List[int]) -> int:
    result = 0
    sequences: DefaultDict[Tuple[int, int, int, int], int] = defaultdict(int)
    for num in input:
        seen_sequences = set()
        window: List[Optional[int]] = [None, None, None, None]
        prev = num % 10
        for _ in range(2000):
            num = simulate(num, 1)
            val = num % 10
            diff = val - prev
            prev = val

            window.append(diff)
            window = window[1:]
            seq = tuple(window)
            if any([s is None for s in seq]):
                continue

            if seq not in seen_sequences:
                seen_sequences.add(seq)
                sequences[seq] += val
        result += num
    result2 = max(sequences.values())
    print(f'Day {day()}, Part 1: {result}')
    print(f'Day {day()}, Part 2: {result2}')
    return result


if __name__ == "__main__":
    input = get_num_input()
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        1,
        10,
        100,
        2024,
    ]


def test_day22_part1(puzzle_input):
    assert simulate(123, 10) == 5908254
    assert part2(puzzle_input) == 37327623
