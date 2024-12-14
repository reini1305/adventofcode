import pytest
from typing import List, Tuple
from aoc import day, get_input


def getRobots(input: List[str]) -> Tuple[List[Tuple[int, int, int, int]], int, int]:
    robots = []
    sizex = 0
    sizey = 1
    for line in input:
        p, v = line.split()
        px, py = p[2:].split(',')
        vx, vy = v[2:].split(',')
        robot = (int(px), int(py), int(vx), int(vy))
        sizex = max(sizex, robot[0])
        sizey = max(sizey, robot[1])
        robots.append(robot)
    sizey += 1
    sizex += 1
    return robots, sizex, sizey


def moveRobot(robot: Tuple[int, int, int, int],
              steps: int,
              sizex: int,
              sizey: int) -> Tuple[int, int, int, int]:
    x, y = robot[:2]
    for _ in range(steps):
        x = (x + robot[2]) % sizex
        y = (y + robot[3]) % sizey
    return x, y, *robot[2:]


def part1(input: List[str]) -> int:
    result = 0
    robots, sx, sy = getRobots(input)
    quadrants = [0] * 4
    for robot in robots:
        robot = moveRobot(robot, 100, sx, sy)
        if robot[0] < sx // 2 and robot[1] < sy // 2:
            quadrants[0] += 1
        elif robot[0] < sx // 2 and robot[1] > sy // 2:
            quadrants[1] += 1
        elif robot[0] > sx // 2 and robot[1] < sy // 2:
            quadrants[2] += 1
        elif robot[0] > sx // 2 and robot[1] > sy // 2:
            quadrants[3] += 1
    result = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    robots, sx, sy = getRobots(input)
    for step in range(10_000):
        grid = [[" "] * sx for _ in range(sy)]
        for i in range(len(robots)):
            robots[i] = moveRobot(robots[i], 1, sx, sy)
            grid[robots[i][1]][robots[i][0]] = "."
        for line in grid:
            if "......." in "".join(line):
                result = step + 1
                print(f'Day {day()}, Part 2: {result}')
                return result
    return 0


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        'p=0,4 v=3,-3',
        'p=6,3 v=-1,-3',
        'p=10,3 v=-1,2',
        'p=2,0 v=2,-1',
        'p=0,0 v=1,3',
        'p=3,0 v=-2,-2',
        'p=7,6 v=-1,-3',
        'p=3,0 v=-1,-2',
        'p=9,3 v=2,3',
        'p=7,3 v=-1,2',
        'p=2,4 v=2,-3',
        'p=9,5 v=-3,-3',
    ]


def test_day14_part1(puzzle_input):
    assert part1(puzzle_input) == 12


def test_day14_part2(puzzle_input):
    assert part2(puzzle_input) == 0
