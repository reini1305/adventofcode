from copy import deepcopy
import pytest
from typing import List, Tuple
from aoc import day, get_input


class Brick:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self._update_occupied()

    def supports(self, brick) -> bool:
        return False

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


def part1(input: List[str]) -> int:
    result = 0
    bricks = get_bricks(input)
    settle_bricks(bricks)
    print(f'Day {day()}, Part 1: {result}')
    return result


def part2(input: List[str]) -> int:
    result = 0
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


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
    print(bricks)


def test_day22_part2(puzzle_input):
    assert 1
