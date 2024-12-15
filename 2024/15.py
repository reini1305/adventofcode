import pytest
from typing import List, Tuple
from aoc import day, get_input, tuple_add


def parseGrid(input: List[str]) -> Tuple[List[List[str]], Tuple[int, int]]:
    grid = []
    robot = (0, 0)
    for y, line in enumerate(input):
        if line.startswith('#'):
            if '@' in line:
                x = line.find('@')
                robot = (x, y)
                line = line.replace('@', '.')
            grid.append([c for c in line])
    return grid, robot


def parseInstructions(input: List[str]) -> List[str]:
    instructions = []
    for line in input:
        if line.startswith('#') or not line:
            continue
        instructions.extend([c for c in line])
    return instructions


def moveRobot(grid: List[List[str]], start: Tuple[int, int], instructions: List[str]):
    directions = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
    position = start
    for i in instructions:
        nx, ny = tuple_add(position, directions[i])
        # if free, just move there
        if grid[ny][nx] == '.':
            position = (nx, ny)
        # if there is a wall, do nothing
        elif grid[ny][nx] == '#':
            pass
        else:
            # if there is a box, there must be some space along the direction to push the boxes
            free_space = position
            fx, fy = nx, ny
            while True:
                fx, fy = tuple_add((fx, fy), directions[i])
                if grid[fy][fx] == '.':
                    free_space = (fx, fy)
                    break
                elif grid[fy][fx] == '#':
                    break
            # no free space, continue
            if free_space == position:
                pass
            else:
                grid[ny][nx] = '.'
                grid[free_space[1]][free_space[0]] = 'O'
                position = (nx, ny)
    return grid


def part1(input: List[str]) -> int:
    result = 0
    instructions = parseInstructions(input)
    grid, robot = parseGrid(input)
    grid = moveRobot(grid, robot, instructions)
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == 'O':
                result += 100 * y + x
    print(f'Day {day()}, Part 1: {result}')
    return result


def parseGrid2(input: List[str]) -> Tuple[List[List[str]], Tuple[int, int]]:
    grid = []
    robot = (0, 0)
    for y, line in enumerate(input):
        if line.startswith('#'):
            line = line.replace('#', '##')
            line = line.replace('O', '[]')
            line = line.replace('.', '..')
            line = line.replace('@', '@.')
            if '@' in line:
                x = line.find('@')
                robot = (x, y)
                line = line.replace('@', '.')
            grid.append([c for c in line])
    return grid, robot


def normalizeBox(grid: List[List[str]], box: Tuple[int, int]) -> Tuple[int, int]:
    if grid[box[1]][box[0]] == ']':
        box = tuple_add(box, (-1, 0))
    return box


def canPush(grid: List[List[str]], box: Tuple[int, int], dir: Tuple[int, int]) -> bool:
    box = normalizeBox(grid, box)
    at = grid[box[1]][box[0]]
    if at == "#":
        return False
    if at == ".":
        return True
    left = box
    right = tuple_add(box, (1, 0))
    if dir == (1, 0):
        return canPush(grid, tuple_add(right, dir), dir)
    elif dir == (-1, 0):
        return canPush(grid, tuple_add(left, dir), dir)
    else:
        return canPush(grid, tuple_add(right, dir), dir) and canPush(grid, tuple_add(left, dir), dir)


def push(grid: List[List[str]], box: Tuple[int, int], dir: Tuple[int, int]):
    box = normalizeBox(grid, box)
    at = grid[box[1]][box[0]]
    if at in "#.":
        return
    left = box
    right = tuple_add(box, (1, 0))
    if dir == (1, 0):
        push(grid, tuple_add(right, dir), dir)
    elif dir == (-1, 0):
        push(grid, tuple_add(left, dir), dir)
    else:
        push(grid, tuple_add(right, dir), dir)
        push(grid, tuple_add(left, dir), dir)
    grid[left[1]][left[0]] = "."
    grid[right[1]][right[0]] = "."
    grid[tuple_add(left, dir)[1]][tuple_add(left, dir)[0]] = "["
    grid[tuple_add(right, dir)[1]][tuple_add(right, dir)[0]] = "]"


def moveRobot2(grid: List[List[str]], start: Tuple[int, int], instructions: List[str]):
    directions = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
    position = start
    for i in instructions:
        nx, ny = tuple_add(position, directions[i])
        # if free, just move there
        if grid[ny][nx] == '.':
            position = (nx, ny)
        # if there is a wall, do nothing
        elif grid[ny][nx] == '#':
            pass
        else:
            if canPush(grid, (nx, ny), directions[i]):
                push(grid, (nx, ny), directions[i])
                position = (nx, ny)
    return grid


def part2(input: List[str]) -> int:
    result = 0
    instructions = parseInstructions(input)
    grid, robot = parseGrid2(input)
    grid = moveRobot2(grid, robot, instructions)
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == '[':
                result += 100 * y + x
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        '##########',
        '#..O..O.O#',
        '#......O.#',
        '#.OO..O.O#',
        '#..O@..O.#',
        '#O#..O...#',
        '#O..O..O.#',
        '#.OO.O.OO#',
        '#....O...#',
        '##########',
        '',
        '<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^',
        'vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v',
        '><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<',
        '<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^',
        '^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><',
        '^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^',
        '>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^',
        '<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>',
        '^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>',
        'v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^',
    ]


def test_day15_part1(puzzle_input):
    assert part1(puzzle_input) == 10092


def test_day15_part2(puzzle_input):
    assert part2(puzzle_input) == 9021
