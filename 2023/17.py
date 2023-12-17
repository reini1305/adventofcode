import heapq
import pytest
from typing import List, Tuple
from aoc import day, get_input


def parse_input(input: List[str]) -> List[List[int]]:
    output = []
    for line in input:
        output.append([int(i) for i in line])
    return output


def find_path(grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int], least, most) -> int:
    queue = [(0, *start, 0, 0)]
    rows = len(grid)
    cols = len(grid[0])
    seen = set()
    while queue:
        heat, x, y, px, py = heapq.heappop(queue)
        if (x, y) == end:
            return heat
        if (x, y, px, py) in seen:
            continue
        seen.add((x, y, px, py))
        # calculate turns only
        for dx, dy in {(1, 0), (0, 1), (-1, 0), (0, -1)}-{(px, py), (-px, -py)}:
            a, b, h = x, y, heat
            # enter 4-10 moves in the chosen direction
            for i in range(1, most+1):
                a, b = a + dx, b + dy
                if not (a < 0 or b < 0 or a >= cols or b >= rows):
                    h += grid[b][a]
                    if i >= least:
                        heapq.heappush(queue, (h, a, b, dx, dy))
    return 0


def part1(input: List[str]) -> int:
    grid = parse_input(input)
    result = find_path(grid, (0, 0), (len(grid[0]) - 1, len(grid) - 1), 1, 3)
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    grid = parse_input(input)
    result = find_path(grid, (0, 0), (len(grid[0]) - 1, len(grid) - 1), 4, 10)
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        [2, 4, 1, 3, 4, 3, 2, 3, 1, 1, 3, 2, 3,],
        [3, 2, 1, 5, 4, 5, 3, 5, 3, 5, 6, 2, 3,],
        [3, 2, 5, 5, 2, 4, 5, 6, 5, 4, 2, 5, 4,],
        [3, 4, 4, 6, 5, 8, 5, 8, 4, 5, 4, 5, 2,],
        [4, 5, 4, 6, 6, 5, 7, 8, 6, 7, 5, 3, 6,],
        [1, 4, 3, 8, 5, 9, 8, 7, 9, 8, 4, 5, 4,],
        [4, 4, 5, 7, 8, 7, 6, 9, 8, 7, 7, 6, 6,],
        [3, 6, 3, 7, 8, 7, 7, 9, 7, 9, 6, 5, 3,],
        [4, 6, 5, 4, 9, 6, 7, 9, 8, 6, 8, 8, 7,],
        [4, 5, 6, 4, 6, 7, 9, 9, 8, 6, 4, 5, 3,],
        [1, 2, 2, 4, 6, 8, 6, 8, 6, 5, 5, 6, 3,],
        [2, 5, 4, 6, 5, 4, 8, 8, 8, 7, 7, 3, 5,],
        [4, 3, 2, 2, 6, 7, 4, 6, 5, 5, 5, 3, 3,],
    ]


def test_day17_part1(puzzle_input):
    assert find_path(puzzle_input, (0, 0), (len(puzzle_input[0]) - 1, len(puzzle_input) - 1), 1, 3) == 102


def test_day17_part2(puzzle_input):
    assert find_path(puzzle_input, (0, 0), (len(puzzle_input[0]) - 1, len(puzzle_input) - 1), 4, 10) == 94
