from collections import defaultdict
from heapq import heappop, heappush
import pytest
from typing import List, Tuple
from aoc import day, get_input, tuple_add


def parse_input(input: List[str]) -> Tuple[List[List[str]], Tuple[int, int], Tuple[int, int]]:
    output = []
    for line in input:
        output.append(list(line))
    start = (1, 0)
    end = (line.index('.'), len(input) - 1)
    return output, start, end


def get_longest_path(grid: List[List[str]], start: Tuple[int, int], end: Tuple[int, int], part2=False) -> int:
    directions = {'N': (0, -1),
                  'S': (0, 1),
                  'W': (-1, 0),
                  'E': (1, 0)}
    possible_neighbors = {'.': ['N', 'S', 'E', 'W'],
                          '^': ['N'],
                          'v': ['S'],
                          '<': ['W'],
                          '>': ['E']} if not part2 else\
                         {'.': ['N', 'S', 'E', 'W'],
                          '^': ['N', 'S', 'E', 'W'],
                          'v': ['N', 'S', 'E', 'W'],
                          '<': ['N', 'S', 'E', 'W'],
                          '>': ['N', 'S', 'E', 'W']}
    visited = set()
    to_visit: List[Tuple[int, int, int, int]] = list()
    heappush(to_visit, (0, *start, 'S'))
    width = len(grid[0])
    height = len(grid)
    while to_visit:
        cost, x, y, curr_dir = heappop(to_visit)
        if (x, y) == end:
            return -cost
        if (x, y, curr_dir) in visited:
            continue
        visited.add((x, y, curr_dir))
        for dir in possible_neighbors[grid[y][x]]:
            nx, ny = tuple_add((x, y), directions[dir])
            if nx < 0 or ny < 0 or nx >= width or ny >= height or grid[ny][nx] == '#':
                continue
            heappush(to_visit, (cost - 1, nx, ny, 'S' if part2 else dir))
    return 0


def part1(input: List[str]) -> int:
    result = get_longest_path(*parse_input(input))
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    grid, start, target = parse_input(input)

    # create graph where the nodes are the intersections of the grid
    graph = defaultdict(list)
    queue = [(start, start, {start, (0, 1)})] 
    while queue:
        curr_xy, prev_node, visited = queue.pop()
        if curr_xy == target:
            final_node = prev_node
            final_steps = len(visited)-1
            continue

        (x, y) = curr_xy
        neighbors = []
        for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if (i, j) not in visited and grid[j][i] != '#':
                neighbors.append((i, j))

        if len(neighbors) == 1:                                 # neither intersection nor dead end
            nxt_xy = neighbors.pop()
            queue.append((nxt_xy, prev_node, visited | {nxt_xy}))

        elif len(neighbors) > 1:                                # found an intersection ( node)
            steps = len(visited) - 1
            if (curr_xy, steps) in graph[prev_node]:            # already been here
                continue
            graph[prev_node].append((curr_xy, steps))
            graph[curr_xy].append((prev_node, steps))    
            while neighbors:                                    # start new paths from current node
                nxt_xy = neighbors.pop()
                queue.append((nxt_xy, curr_xy, {curr_xy, nxt_xy}))

    # traverse graph
    max_steps = 0
    queue = [(start, 0, {start})]
    while queue:
        curr, steps, visited = queue.pop()
        if curr == final_node:
            max_steps = max(steps, max_steps)
            continue
        for nxt, distance in graph[curr]:
            if nxt not in visited:
                queue.append((nxt, steps + distance, visited | {nxt}))

    result = max_steps + final_steps - 1

    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        '#.#####################',
        '#.......#########...###',
        '#######.#########.#.###',
        '###.....#.>.>.###.#.###',
        '###v#####.#v#.###.#.###',
        '###.>...#.#.#.....#...#',
        '###v###.#.#.#########.#',
        '###...#.#.#.......#...#',
        '#####.#.#.#######.#.###',
        '#.....#.#.#.......#...#',
        '#.#####.#.#.#########v#',
        '#.#...#...#...###...>.#',
        '#.#.#v#######v###.###v#',
        '#...#.>.#...>.>.#.###.#',
        '#####v#.#.###v#.#.###.#',
        '#.....#...#...#.#.#...#',
        '#.#########.###.#.#.###',
        '#...###...#...#...#.###',
        '###.###.#.###v#####v###',
        '#...#...#.#.>.>.#.>.###',
        '#.###.###.#.###.#.#v###',
        '#.....###...###...#...#',
        '#####################.#',
    ]


def test_day23_part1(puzzle_input):
    assert part1(puzzle_input) == 94


def test_day23_part2(puzzle_input):
    assert part2(puzzle_input) == 154
