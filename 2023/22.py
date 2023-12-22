from collections import defaultdict
from copy import deepcopy
import pytest
from typing import DefaultDict, Dict, List, Tuple
from aoc import day, get_input


class Brick:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self._update_occupied()

    def supported_by(self, brick) -> bool:
        return self.create_move_down().intersects(brick.occupied)

    def intersects(self, grid) -> bool:
        return len(grid.intersection(self.occupied)) > 0

    def on_ground(self) -> bool:
        return any(z == 1 for _, _, z in self.occupied)

    def _update_occupied(self):
        self.occupied = {self.start}
        self.occupied.update([(i, self.start[1], self.start[2]) for i in range(self.start[0], self.end[0] + 1)])
        self.occupied.update([(self.start[0], i, self.start[2]) for i in range(self.start[1], self.end[1] + 1)])
        self.occupied.update([(self.start[0], self.start[1], i) for i in range(self.start[2], self.end[2] + 1)])

    def create_move_down(self):
        start = *self.start[:-1], self.start[-1] - 1
        end = *self.end[:-1], self.end[-1] - 1
        return Brick(start, end)


def get_bricks(input: List[str]) -> List[Brick]:
    bricks = []
    for line in input:
        start_str, end_str = line.split('~')
        s_x, s_y, s_z = [int(i) for i in start_str.split(',')]
        e_x, e_y, e_z = [int(i) for i in end_str.split(',')]
        bricks.append(Brick((s_x, s_y, s_z), (e_x, e_y, e_z)))
    return bricks


def settle_bricks(bricks):
    grid = set()
    for brick in bricks:
        for x, y, z in brick.occupied:
            grid.add((x, y, z))
    brick_moved = True
    while brick_moved:
        brick_moved = False
        for id in range(len(bricks)):
            new_brick = deepcopy(bricks[id])
            movable = True
            while movable:
                # try moving it down by 1
                if new_brick.on_ground():
                    movable = False
                    continue
                new_brick = new_brick.create_move_down()
                if new_brick.intersects(grid - bricks[id].occupied):
                    movable = False
                    break
                if movable:
                    for x, y, z in bricks[id].occupied:
                        grid.remove((x, y, z))
                    bricks[id] = new_brick
                    for x, y, z in bricks[id].occupied:
                        grid.add((x, y, z))
                    brick_moved = True


def part1(bricks) -> int:
    result = 0
    supports: DefaultDict[int, List[int]] = defaultdict(list)
    supported_by: DefaultDict[int, List[int]] = defaultdict(list)
    for id, brick in enumerate(bricks):
        for other_id, other_brick in enumerate(bricks):
            if id == other_id:
                continue
            if brick.supported_by(other_brick):
                supports[other_id].append(id)
                supported_by[id].append(other_id)
    # A brick can be removed if all of the bricks it supports are supported by another brick
    for id in range(len(bricks)):
        if not supports[id]:
            result += 1
            continue
        if all(len(supported_by[s]) != 1 for s in supports[id]):
            result += 1
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(bricks) -> int:
    result = 0
    supports: DefaultDict[int, List[int]] = defaultdict(list)
    supported_by: DefaultDict[int, List[int]] = defaultdict(list)
    for id, brick in enumerate(bricks):
        for other_id, other_brick in enumerate(bricks):
            if id == other_id:
                continue
            if brick.supported_by(other_brick):
                supports[other_id].append(id)
                supported_by[id].append(other_id)
    for t in range(len(bricks)):
        collapsed = {t}
        collapsing = True
        while collapsing:
            collapsing = False
            for s in range(len(bricks)):
                if s in collapsed:
                    continue
                if len(supported_by[s]) == 0:
                    continue
                to_check = set(supported_by[s]) - collapsed
                if len(to_check) == 0:
                    collapsed.add(s)
                    collapsing = True
        result += len(collapsed) - 1

    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    bricks = get_bricks(input)
    settle_bricks(bricks)
    part1(bricks)
    part2(bricks)


@pytest.fixture
def puzzle_input():
    return [
        '1,0,1~1,2,1',
        '0,0,2~2,0,2',
        '0,2,3~2,2,3',
        '0,0,4~0,2,4',
        '2,0,5~2,2,5',
        '0,1,6~2,1,6',
        '1,1,8~1,1,9',
    ]


def test_day22_part1(puzzle_input):
    bricks = get_bricks(puzzle_input)
    settle_bricks(bricks)
    assert part1(bricks) == 5


def test_day22_part2(puzzle_input):
    bricks = get_bricks(puzzle_input)
    settle_bricks(bricks)
    assert part2(bricks) == 7
