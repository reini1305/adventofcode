import pytest
from typing import Any, DefaultDict, List, Tuple
from collections import defaultdict
from aoc import day, get_input

def draw_line(field:DefaultDict[Any, int], pt1:Tuple[int, int], pt2:Tuple[int, int], diagonal:bool) -> None:
    diff_x = abs(pt1[0] - pt2[0])
    diff_y = abs(pt1[1] - pt2[1])
    if diff_x == 0 or diff_y == 0 or (diagonal and diff_x == diff_y):
        dir_x = 1 if pt2[0] > pt1[0] else -1 if pt2[0] < pt1[0] else 0
        dir_y = 1 if pt2[1] > pt1[1] else -1 if pt2[1] < pt1[1] else 0
        it_x = range(pt1[0], pt2[0]+dir_x, dir_x) if dir_x else [pt1[0]] * (diff_y + 1)
        it_y = range(pt1[1], pt2[1]+dir_y, dir_y) if dir_y else [pt1[1]] * (diff_x + 1)
        for x, y in zip(it_x,it_y):
            field[(x, y)] += 1

def parse_input(input: List[str]) -> Tuple[List[Tuple[int, int]],List[Tuple[int, int]]]:
    pts1 = []
    pts2 = []
    for line in input:
        f, t = line.split(' -> ')
        pts1.append((int(f.split(',')[0]),int(f.split(',')[1])))
        pts2.append((int(t.split(',')[0]),int(t.split(',')[1])))
    return pts1, pts2

def part1(pts1:List[Tuple[int, int]], pts2:List[Tuple[int, int]])-> None:
    field:DefaultDict[Any, int] = defaultdict(int)
    for i in range(len(pts1)):
        draw_line(field, pts1[i], pts2[i], False)
    result = sum([1 for v in field.values() if v > 1])
    print(f'Day {day()}, Part 1: {result}')

def part2(pts1:List[Tuple[int, int]], pts2:List[Tuple[int, int]])-> None:
    field: DefaultDict[Any, int] = defaultdict(int)
    for i in range(len(pts1)):
        draw_line(field, pts1[i], pts2[i], True)
    result = sum([1 for v in field.values() if v > 1])
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    pts1, pts2 = parse_input(input)
    part1(pts1, pts2)
    part2(pts1, pts2)

@pytest.fixture
def puzzle_input():
    return [
        "0,9 -> 5,9",
        "8,0 -> 0,8",
        "9,4 -> 3,4",
        "2,2 -> 2,1",
        "7,0 -> 7,4",
        "6,4 -> 2,0",
        "0,9 -> 2,9",
        "3,4 -> 1,4",
        "0,0 -> 8,8",
        "5,5 -> 8,2"]

def test_day5_part1(puzzle_input):
    pts1, pts2 = parse_input(puzzle_input)
    assert pts1[0] == (0, 9)
    assert pts2[0] == (5, 9)
    field = defaultdict(int)
    for i in range(len(pts1)):
        draw_line(field, pts1[i], pts2[i], False)
    result = sum([1 for v in field.values() if v > 1])
    assert result == 5

def test_day5_part2(puzzle_input):
    pts1, pts2 = parse_input(puzzle_input)
    assert pts1[0] == (0, 9)
    assert pts2[0] == (5, 9)
    field = defaultdict(int)
    for i in range(len(pts1)):
        draw_line(field, pts1[i], pts2[i], True)
    result = sum([1 for v in field.values() if v > 1])
    assert result == 12