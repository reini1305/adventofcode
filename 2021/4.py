import pytest
from typing import List, Tuple
import numpy as np
from aoc import day, get_input

class BingoField:
    def __init__(self, input:List[str]) -> None:
        self.field = np.zeros((5,5))
        for y, line in enumerate(input):
            for x, val in enumerate(line.split()):
                self.field[y,x] = int(val)

    def check_victory(self) -> bool:
        return np.any(np.sum(self.field,axis=0)==-5) or\
            np.any(np.sum(self.field,axis=1)==-5)

    def play(self, value: int) -> bool:
        if value in self.field:
            self.field[self.field == value] = -1
            return self.check_victory()
        else:
            return False

    def get_score(self) -> int:
        return int(np.sum(self.field[self.field != -1]))

def parse_input(input: List[str])-> Tuple[str, List[BingoField]]:
    bingo_fields = []
    num_bingo_fields = (len(input) - 1) // 6
    for i in range(num_bingo_fields):
        bingo_fields.append(BingoField(input[2 + i * 6:2 + (i + 1) * 6]))
    return (input[0], bingo_fields)

def play(input:str, fields:List[BingoField], last:bool)-> Tuple[int, int, int]:
    won = [False] * len(fields)
    for val in input.split(','):
        v = int(val)
        for i,f in enumerate(fields):
            if f.play(v):
                won[i] = True
                if (last and all(won)) or not last:
                    return v, f.get_score(), i
    return 0, 0, 0

def part1(input: List[str])-> None:
    numbers, fields = parse_input(input)
    winning, score, _ = play(numbers, fields, last=False)
    result = winning * score
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    numbers, fields = parse_input(input)
    winning, score, _ = play(numbers, fields, last=True)
    result = winning * score
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return ["7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
            "",
            "22 13 17 11  0",
            " 8  2 23  4 24",
            "21  9 14 16  7",
            " 6 10  3 18  5",
            " 1 12 20 15 19",
            "",
            " 3 15  0  2 22",
            " 9 18 13 17  5",
            "19  8  7 25 23",
            "20 11 10 24  4",
            "14 21 16 12  6",
            "",
            "14 21 17 24  4",
            "10 16 15  9 19",
            "18  8 23 26 20",
            "22 11 13  6  5",
            " 2  0 12  3  7"]

def test_day4_part1(puzzle_input):
    input, fields = parse_input(puzzle_input)
    assert len(fields) == 3
    assert input == "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1"
    num, score, id = play(input, fields, last=False)
    assert num == 24
    assert score == 188
    assert id == 2

def test_day4_part2(puzzle_input):
    input, fields = parse_input(puzzle_input)
    num, score, id = play(input, fields, last=True)
    assert num == 13
    assert score == 148
    assert id == 1