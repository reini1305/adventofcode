import pytest
from typing import List, Tuple, Dict
import numpy as np
from aoc import day, get_input

def parse_input(input: List[str])->Tuple[List[Tuple[int,int]],List[Dict[str,int]]]:
    coordinates = []
    folds = []
    for line in input:
        if line == '':
            continue
        if line.startswith('fold'):
            text, val = line.split('=')
            folds.append({text[-1]:int(val)})
        else:
            x, y = line.split(',')
            coordinates.append((int(x), int(y)))
    return coordinates, folds

def create_field(coordinates):
    max_x = max([x for x,_ in coordinates]) + 1
    max_y = max([y for _,y in coordinates]) + 1
    field = np.zeros((max_y,max_x))
    for x,y in coordinates:
        field[y,x] = 1
    return field

def fold_field(field, fold):
    if 'y' in fold:
        coord = fold['y']
        dist = field.shape[0] - coord - 1
        return np.vstack((field[:coord-dist, :], field[coord-dist:coord, :] + np.flipud(field[coord+1:, :])))
    else:
        coord = fold['x']
        dist = field.shape[1] - coord - 1 
        return np.hstack((field[:, :coord-dist], field[:, coord-dist:coord] + np.fliplr(field[:, coord+1:])))

def part1(input: List[str])-> None:
    coordinates, folds = parse_input(input)
    field = create_field(coordinates)
    first = fold_field(field,folds[0])
    result = int(np.sum(first>0))
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    coordinates, folds = parse_input(input)
    field = create_field(coordinates)
    for fold in folds:
        field = fold_field(field, fold)
    np.set_printoptions(linewidth = 130,formatter={'all':lambda x: ' ' if x==0 else '#'})
    print(f'Day {day()}, Part 2: \n{field}')

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        "6,10",
        "0,14",
        "9,10",
        "0,3",
        "10,4",
        "4,11",
        "6,0",
        "6,12",
        "4,1",
        "0,13",
        "10,12",
        "3,4",
        "3,0",
        "8,4",
        "1,10",
        "2,14",
        "8,10",
        "9,0",
        "",
        "fold along y=7",
        "fold along x=5",
    ]

def test_day13_part1(puzzle_input):
    coordinates, folds = parse_input(puzzle_input)
    assert folds[0]['y'] == 7
    assert coordinates[0] == (6,10)
    field = create_field(coordinates)
    first = fold_field(field,folds[0])
    assert np.sum(first>0) == 17

def test_day13_part2(puzzle_input):
    assert 1