import pytest
from typing import List
from aoc import day, get_input

def parse_input(input: List[str]) -> List[List[int]]:
    output:List[List[int]] = []
    for line in input:
        output.append([int(c) for c in line.strip()])
    return output

def check_visible(grid:List[List[int]], x:int, y:int) -> bool:
    # check if border
    if x==0 or y==0 or x==len(grid[0])-1 or y == len(grid)-1:
        return True
    # check from the left
    if all([grid[y][xr] < grid[y][x] for xr in range(x)]):
        return True
    # check from the top
    if all([grid[yr][x] < grid[y][x] for yr in range(y)]):
        return True
    # check from the right
    if all([grid[y][xr] < grid[y][x] for xr in range(x+1, len(grid[x]))]):
        return True
    # check from the top
    if all([grid[yr][x] < grid[y][x] for yr in range(y+1, len(grid))]):
        return True

    return False

def get_scenic(grid:List[List[int]], x:int, y:int) -> int:
    total_scenic = 1
    scenic = 0
    for xr in reversed(range(x)):
        if grid[y][xr] >= grid[y][x]:
            scenic +=1
            break
        scenic +=1
    total_scenic *= scenic
    scenic = 0
    for yr in reversed(range(y)):
        if grid[yr][x] >= grid[y][x]:
            scenic +=1
            break
        scenic +=1
    total_scenic *= scenic
    scenic = 0
    for xr in range(x+1, len(grid[x])):
        if grid[y][xr] >= grid[y][x]:
            scenic +=1
            break
        scenic +=1
    total_scenic *= scenic
    scenic = 0
    for yr in range(y+1, len(grid)):
        if grid[yr][x] >= grid[y][x]:
            scenic +=1
            break
        scenic +=1
    total_scenic *= scenic
    return total_scenic

def part1(input: List[str])-> None:
    grid = parse_input(input)
    result = sum([check_visible(grid,x,y) for x in range(len(grid)) for y in range(len(grid))])
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    grid = parse_input(input)
    result = max([get_scenic(grid,x,y) for x in range(len(grid)) for y in range(len(grid))])
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390",
    ]

def test_day8_part1(puzzle_input):
    grid = parse_input(puzzle_input)
    assert check_visible(grid, 0, 0) == True
    assert check_visible(grid, 1, 1) == True
    assert check_visible(grid, 3, 1) == False
    assert sum([check_visible(grid,x,y) for x in range(len(grid)) for y in range(len(grid))]) == 21

def test_day8_part2(puzzle_input):
    grid = parse_input(puzzle_input)
    assert get_scenic(grid, 2, 1) == 4
    assert get_scenic(grid, 2, 3) == 8