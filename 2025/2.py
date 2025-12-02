import pytest
from typing import List
from aoc import day, get_input


def findDuplicates(start: int, end: int) -> List[int]:
    duplicates: List[int] = []
    for num in range(start, end + 1):
        string_num = str(num)
        if string_num[:len(string_num)//2] == string_num[len(string_num)//2:]:
            duplicates.append(num)
    return duplicates


def findNplicates(start: int, end: int) -> List[int]:
    nplicates: List[int] = []
    for num in range(start, end + 1):
        string_num = str(num)
        string_len = len(string_num)
        for split in range(1, string_len // 2 + 1):
            if string_len % split:
                continue
            num_chunks = string_len // split
            chunks = [string_num[i * split:(i+1)*split] for i in range(num_chunks)]
            if len(set(chunks)) == 1:
                nplicates.append(num)
                break
    return nplicates


def part1(input: List[str]) -> int:
    result = 0
    for range_to_check in input[0].split(","):
        start, end = range_to_check.split("-")
        result += sum(findDuplicates(int(start), int(end)))
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    for range_to_check in input[0].split(","):
        start, end = range_to_check.split("-")
        result += sum(findNplicates(int(start), int(end)))
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return ["11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
            "1698522-1698528,446443-446449,38593856-38593862,565653-565659,"
            "824824821-824824827,2121212118-2121212124"]


def test_day2_part1(puzzle_input):
    assert findDuplicates(11, 22) == [11, 22]
    assert part1(puzzle_input) == 1227775554


def test_day2_part2(puzzle_input):
    assert findNplicates(11, 22) == [11, 22]
    assert findNplicates(222220, 222224) == [222222]
    assert findNplicates(824824821, 824824827) == [824824824]
    assert findNplicates(95, 115) == [99, 111]
    assert findNplicates(998, 1012) == [999, 1010]
    assert findNplicates(1188511880, 1188511890) == [1188511885]
    assert findNplicates(1698522, 1698528) == []
    assert findNplicates(446443, 446449) == [446446]
    assert findNplicates(38593856, 38593862) == [38593859]
    assert findNplicates(565653, 565659) == [565656]
    assert findNplicates(824824821, 824824827) == [824824824]
    assert findNplicates(2121212118, 2121212124) == [2121212121]
    assert part2(puzzle_input) == 4174379265
