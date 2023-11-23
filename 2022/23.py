from collections import deque
import pytest
from typing import List, Tuple
from tqdm import tqdm
from aoc import day, get_input

def parse_input(input: List[str])->List[Tuple[int,int]]:
    elves = []
    for y, line in enumerate(input):
        for x, c in enumerate(line.strip()):
            if c == '#':
                elves.append((x,y))
    return elves

def move(elves:List[Tuple[int,int]], rounds:int):
    directions = deque([
        lambda x: [(x[0]+dx,x[1]-1) for dx in [-1, 0, 1]],  #north
        lambda x: [(x[0]+dx,x[1]+1) for dx in [-1, 0, 1]],  #south
        lambda x: [(x[0]-1,x[1]+dy) for dy in [-1, 0, 1]],  #west
        lambda x: [(x[0]+1,x[1]+dy) for dy in [-1, 0, 1]],  #east
    ])
    for round in range(rounds):
        new_positions = []
        any_moved = False
        curr_elves = set(elves)
        for elf in elves:
            if not any([c in curr_elves for dir in directions for c in dir(elf)]):
                new_positions.append(None)
                continue
            moved = False
            for dir in directions:
                candidates = dir(elf)
                if not any([c in curr_elves for c in candidates]):
                    if candidates[1] in new_positions:
                        new_positions[new_positions.index(candidates[1])] = None
                        new_positions.append(None)
                    else:
                        new_positions.append(candidates[1])
                    moved = True
                    break
            if not moved:
                new_positions.append(None)
            else:
                any_moved = True
        for i, new_pos in enumerate(new_positions):
            if new_pos is not None:
                elves[i] = new_pos
        directions.append(directions.popleft())
        if not any_moved:
            break
    return round + 1

def get_bounding_rectangle(elves):
    lu = (min([elf[0] for elf in elves]), min([elf[1] for elf in elves]))
    rb = (max([elf[0] for elf in elves]), max([elf[1] for elf in elves]))
    return lu, rb

def part1(input: List[str])-> None:
    elves = parse_input(input)
    move(elves, 10)
    lu, rb = get_bounding_rectangle(elves)
    width = abs(lu[0] - rb[0]) + 1
    height = abs(lu[1] - rb[1]) + 1
    result = width * height - len(elves)
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    elves = parse_input(input)
    result = move(elves, 1000)
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        "..............",
        "..............",
        ".......#......",
        ".....###.#....",
        "...#...#.#....",
        "....#...##....",
        "...#.###......",
        "...##.#.##....",
        "....#..#......",
        "..............",
        "..............",
        "..............",
    ]

def test_day23_part1(puzzle_input):
    elves = parse_input(puzzle_input)
    move(elves, 10)
    lu, rb = get_bounding_rectangle(elves)
    width = abs(lu[0] - rb[0]) + 1
    height = abs(lu[1] - rb[1]) + 1
    assert width * height - len(elves) == 110

def test_day23_part2(puzzle_input):
    elves = parse_input(puzzle_input)
    assert move(elves, 30) == 20