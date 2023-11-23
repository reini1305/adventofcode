import pytest
from typing import List
from aoc import day, get_input

def get_loop_size(public_key:int)->int:
    value = 1
    loop = 0
    while value != public_key:
        value = (value * 7) % 20201227
        loop+=1
    return loop

def get_encryption_key(public_key:int, rounds:int)->int:
    key = 1
    for _ in range(rounds):
        key = (key * public_key) % 20201227
    return key

def part1(key1:int, key2:int)-> None:
    result = get_encryption_key(key2, get_loop_size(key1))
    print(f'Day {day()}, Part 1: {result}')

if __name__ == "__main__":
    key1 = 18356117
    key2 = 5909654
    part1(key1,key2)

def test_day25_part1():
    assert get_loop_size(5764801) == 8
    assert get_loop_size(17807724) == 11
    assert get_encryption_key(5764801, 11) == get_encryption_key(17807724, 8) == 14897079
