import pytest
from typing import List, Set, Tuple
from aoc import day, get_input

def parse(input:List[str])->Tuple[str,Set[Tuple[int,int]]]:
    lookup = input[0].replace('.','0').replace('#','1')
    image = set()
    for y,line in enumerate(input[2:]):
        for x, val in enumerate(line):
            if val == '#':
                image.add((x,y))
    return lookup, image

def get_bit(x:int, 
            y:int, 
            image:Set[Tuple[int,int]], 
            boundary:Set[Tuple[int,int]], 
            outside_on:bool
        )->str:
    if (x, y) in image:
        return '1'
    if outside_on:
        return '1' if (x, y) not in boundary else '0'
    else:
        return '0'

def enhance(image:Set[Tuple[int,int]], lookup:str, times:int)->Set[Tuple[int,int]]:
    neighbors = [(-1,-1),(-1,0),(-1,1),
                 (0, -1),(0, 0),(0, 1),
                 (1, -1),(1, 0),(1, 1)]
    min_x = min([p[0] for p in image])
    min_y = min([p[1] for p in image])
    max_x = max([p[0] for p in image])
    max_y = max([p[1] for p in image])
    boundary = {
        (x, y) 
        for x in range(min_x, max_x + 1)
        for y in range(min_y, max_y + 1)
    }
    x_range = (min_x-1, max_x+2)
    y_range = (min_y-1, max_y+2)
    for step in range(times):
        new_image = set()
        outside_on = step%2==1 and lookup[0] == '1'
        for x in range(*x_range):
            for y in range(*y_range):
                l=int(''.join([
                    get_bit(x+nx, y+ny, image, boundary, outside_on) 
                    for ny, nx in neighbors]), 2)
                if lookup[l] == '1':
                    new_image.add((x,y))
        image = new_image
        boundary = {
            (x, y) 
            for x in range(*x_range)
            for y in range(*y_range)
        }
        x_range = (x_range[0]-1, x_range[1]+1)
        y_range = (y_range[0]-1, y_range[1]+1)
        
    return image

def part1and2(input: List[str])-> None:
    lookup, image = parse(input)
    image = enhance(image, lookup, 2)
    result = len(image)
    print(f'Day {day()}, Part 1: {result}')
    image = enhance(image, lookup, 48)
    result = len(image)
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    part1and2(input)

@pytest.fixture
def puzzle_input():
    return [
        '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##'
        '#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###'
        '.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.'
        '.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....'
        '.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..'
        '...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....'
        '..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#',
        '',
        '#..#.',
        '#....',
        '##..#',
        '..#..',
        '..###',
    ]

def test_day20_part1(puzzle_input):
    lookup, image = parse(puzzle_input)
    assert len(image) == 10
    assert len(lookup) == 512
    image = enhance(image, lookup, 2)
    assert len(image) == 35

def test_day20_part2(puzzle_input):
    lookup, image = parse(puzzle_input)
    image = enhance(image, lookup, 50)
    assert len(image) == 3351