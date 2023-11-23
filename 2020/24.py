import pytest
from typing import List, Set, Tuple
from aoc import day, get_input
from copy import deepcopy

Coordinate = Tuple[int,int,int]

def coordinate_add(a:Coordinate,b:Coordinate)->Coordinate:
    return (a[0]+b[0],a[1]+b[1],a[2]+b[2])

def black_tiles(input:List[str])->Set[Tuple[int,int,int]]:
    tiles:Set[Coordinate] = set()
    directions = {'w': (-1, 1, 0),
                  'e': ( 1,-1, 0),
                  'nw':( 0, 1,-1),
                  'ne':( 1, 0,-1),
                  'se':( 0,-1, 1),
                  'sw':(-1, 0, 1)}
    for line in input:
        curr_char = 0
        coordinate = (0,0,0)
        while curr_char < len(line):
            if line[curr_char] in ['s', 'n']:
                instruction = line[curr_char:curr_char+2]
                curr_char += 2
            else:
                instruction = line[curr_char]
                curr_char += 1
            coordinate = coordinate_add(coordinate,directions[instruction])
        if coordinate in tiles:
            tiles.remove(coordinate)
        else:
            tiles.add(coordinate)
    return tiles

def flip_n_times(tiles:Set[Coordinate], n:int)->Set[Coordinate]:
    neighbors = [(-1, 1, 0),
                 ( 1,-1, 0),
                 ( 0, 1,-1),
                 ( 1, 0,-1),
                 ( 0,-1, 1),
                 (-1, 0, 1)]

    for _ in range(n):
        to_check:Set[Coordinate] = set()
        new_tiles = deepcopy(tiles)
        # first check all active fields
        for active in tiles:
            sum_active = 0
            for nb in neighbors:
                new_coord = coordinate_add(active, nb)
                to_check.add(new_coord)
                if new_coord in tiles:
                    sum_active+=1
            if sum_active == 0 or sum_active > 2:
                new_tiles.remove(active)
        # now check all the fields adjacent to active fields
        for inactive in to_check:
            if inactive in tiles:
                continue # not actually inactive
            sum_active = 0
            for nb in neighbors:
                new_coord = coordinate_add(inactive, nb)
                if new_coord in tiles:
                    sum_active+=1
            if sum_active == 2:
                new_tiles.add(inactive)
        tiles = new_tiles
    return tiles

def part1(input: List[str])-> None:
    result = len(black_tiles(input))
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    result = len(flip_n_times(black_tiles(input),100))
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input(f'input{day()}.txt')
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    input = ['sesenwnenenewseeswwswswwnenewsewsw',
            'neeenesenwnwwswnenewnwwsewnenwseswesw',
            'seswneswswsenwwnwse',
            'nwnwneseeswswnenewneswwnewseswneseene',
            'swweswneswnenwsewnwneneseenw',
            'eesenwseswswnenwswnwnwsewwnwsene',
            'sewnenenenesenwsewnenwwwse',
            'wenwwweseeeweswwwnwwe',
            'wsweesenenewnwwnwsenewsenwwsesesenwne',
            'neeswseenwwswnwswswnw',
            'nenwswwsewswnenenewsenwsenwnesesenew',
            'enewnwewneswsewnwswenweswnenwsenwsw',
            'sweneswneswneneenwnewenewwneswswnese',
            'swwesenesewenwneswnwwneseswwne',
            'enesenwswwswneneswsenwnewswseenwsese',
            'wnwnesenesenenwwnenwsewesewsesesew',
            'nenewswnwewswnenesenwnesewesw',
            'eneswnwswnwsenenwnwnwwseeswneewsenese',
            'neswnwewnwnwseenwseesewsenwsweewe',
            'wseweeenwnesenwwwswnew']
    return input

def test_day24_part1(puzzle_input):
    input = puzzle_input
    assert len(black_tiles(input)) == 10

def test_day24_part2(puzzle_input):
    input = puzzle_input
    tiles = black_tiles(input)
    assert len(flip_n_times(tiles,1)) == 15
    assert len(flip_n_times(tiles,100)) == 2208