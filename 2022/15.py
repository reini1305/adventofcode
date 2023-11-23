import pytest
from typing import List
from aoc import day, get_input
from tqdm import tqdm

def parse_input(input: List[str]):
    sensors = []
    for line in input:
        sensor_string, beacon_string = line.strip().split(':')
        sensor_xy = sensor_string.split('=')
        becon_xy = beacon_string.split('=')
        sensors.append(
            (
                (int(sensor_xy[1].split(',')[0]),int(sensor_xy[2])),
                (int(becon_xy[1].split(',')[0]),int(becon_xy[2]))
            )
        )
    return sensors

def get_range_of_sensor(sensor, y):
    dist = abs(sensor[0][0] - sensor[1][0]) + abs(sensor[0][1] - sensor[1][1])
    dist_y = abs(sensor[0][1] - y)
    if dist_y > dist:
        return []
    start = sensor[0][0] - (dist - dist_y)
    end = sensor[0][0] + (dist - dist_y)
    return [start, end]

def merge_ranges(ranges):
    # sort by begin
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged = [sorted_ranges[0]]
    for current in sorted_ranges:
        previous = merged[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)
    return merged

def get_range_for_line(sensors, y):
    ranges = []
    for sensor in sensors:
        range = get_range_of_sensor(sensor, y)
        if range:
            ranges.append(range)
    return merge_ranges(ranges)

def part1(input: List[str])-> None:
    sensors = parse_input(input)
    occupied = get_range_for_line(sensors, 2000000)
    result = 0
    for o in occupied:
        result += o[1] - o[0]
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    sensors = parse_input(input)
    for y in range(4000000):
        ranges = get_range_for_line(sensors, y)
        if len(ranges) > 1:
            result = y + (ranges[0][1] + 1) * 4000000
            print(f'Day {day()}, Part 2: {result}')
            break

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        "Sensor at x=2, y=18: closest beacon is at x=-2, y=15",
        "Sensor at x=9, y=16: closest beacon is at x=10, y=16",
        "Sensor at x=13, y=2: closest beacon is at x=15, y=3",
        "Sensor at x=12, y=14: closest beacon is at x=10, y=16",
        "Sensor at x=10, y=20: closest beacon is at x=10, y=16",
        "Sensor at x=14, y=17: closest beacon is at x=10, y=16",
        "Sensor at x=8, y=7: closest beacon is at x=2, y=10",
        "Sensor at x=2, y=0: closest beacon is at x=2, y=10",
        "Sensor at x=0, y=11: closest beacon is at x=2, y=10",
        "Sensor at x=20, y=14: closest beacon is at x=25, y=17",
        "Sensor at x=17, y=20: closest beacon is at x=21, y=22",
        "Sensor at x=16, y=7: closest beacon is at x=15, y=3",
        "Sensor at x=14, y=3: closest beacon is at x=15, y=3",
        "Sensor at x=20, y=1: closest beacon is at x=15, y=3"
    ]

def test_day15_part1(puzzle_input):
    sensors = parse_input(puzzle_input)
    occupied = get_range_for_line(sensors, 10)
    count = 0
    for o in occupied:
        count += o[1] - o[0]
    assert count == 26

def test_day15_part2(puzzle_input):
    assert 1