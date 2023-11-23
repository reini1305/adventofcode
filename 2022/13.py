import functools
import json
import pytest
from typing import List
from aoc import day, get_input

def get_pairs(input:List[str]):
    pairs = []
    curr_pair = [[],[]]
    curr_item = 0
    for line in input:
        line = line.strip()
        if line == "":
            pairs.append(tuple(curr_pair))
            curr_item = 0
        else:
            curr_pair[curr_item] = json.loads(line)
            curr_item += 1
    pairs.append(tuple(curr_pair))
    return pairs

def compare(left, right):
    for l, r in zip(left, right):
        if isinstance(l, int) and isinstance(r, int):
            if l > r:
                return False
            if l < r:
                return True
        elif isinstance(l, int) and isinstance(r, list):
            result = compare([l],r)
            if result is not None:
                return result
        elif isinstance(l, list) and isinstance(r, int):
            result = compare(l,[r])
            if result is not None:
                return result
        else:
            result = compare(l,r)
            if result is not None:
                return result

    if len(left) == len(right):
        return None
    else: 
        return len(left) < len(right)

def part1(input: List[str])-> None:
    pairs = get_pairs(input)
    result = 0
    for i, pair in enumerate(pairs):
        if compare(pair[0],pair[1]):
            result += i+1
    print(f'Day {day()}, Part 1: {result}')

def list_compare(left, right):
    result = compare(left, right)
    if result ==False:
        return 1
    elif result == True:
        return -1
    return 0

def part2(input: List[str])-> None:
    pairs = get_pairs(input)
    packets = []
    for pair in pairs:
        packets.append(pair[0])
        packets.append(pair[1])
    packets.append([[2]])
    packets.append([[6]])
    sorted_packets = sorted(packets, key=functools.cmp_to_key(list_compare))
    result = (sorted_packets.index([[2]])+1) * (sorted_packets.index([[6]])+1)
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        "[1,1,3,1,1]",
        "[1,1,5,1,1]",
        "",
        "[[1],[2,3,4]]",
        "[[1],4]",
        "",
        "[9]",
        "[[8,7,6]]",
        "",
        "[[4,4],4,4]",
        "[[4,4],4,4,4]",
        "",
        "[7,7,7,7]",
        "[7,7,7]",
        "",
        "[]",
        "[3]",
        "",
        "[[[]]]",
        "[[]]",
        "",
        "[1,[2,[3,[4,[5,6,7]]]],8,9]",
        "[1,[2,[3,[4,[5,6,0]]]],8,9]"
    ]

def test_day13_part1(puzzle_input):
    pairs = get_pairs(puzzle_input)
    assert len(pairs) == 8
    assert compare(pairs[0][0], pairs[0][1]) == True
    assert compare(pairs[1][0], pairs[1][1]) == True
    assert compare(pairs[2][0], pairs[2][1]) == False
    assert compare(pairs[3][0], pairs[3][1]) == True
    assert compare(pairs[4][0], pairs[4][1]) == False
    assert compare(pairs[5][0], pairs[5][1]) == True
    assert compare(pairs[6][0], pairs[6][1]) == False
    assert compare(pairs[7][0], pairs[7][1]) == False
    result = 0
    for i, pair in enumerate(pairs):
        if compare(pair[0],pair[1]):
            result += i+1
    assert result == 13

def test_day13_part2(puzzle_input):
    pairs = get_pairs(puzzle_input)
    packets = []
    for pair in pairs:
        packets.append(pair[0])
        packets.append(pair[1])
    packets.append([[2]])
    packets.append([[6]])
    sorted_packets = sorted(packets, key=functools.cmp_to_key(list_compare))
    assert (sorted_packets.index([[2]])+1) * (sorted_packets.index([[6]])+1) == 140