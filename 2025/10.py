import pytest
import numpy as np
from collections import deque
from heapq import heappop, heappush
from typing import Deque, List, Tuple
from aoc import day, get_input
from scipy.optimize import linprog  # type: ignore


def getMachines(input: List[str]) -> List[Tuple[List[bool], List[List[int]], List[int]]]:
    machines: List[Tuple[List[bool], List[List[int]], List[int]]] = []

    for line in input:
        lights = [c == "#" for c in line[1:line.find("]")]]
        buttons = []
        for b in line[line.find("]") + 3:line.find("{")-2].split(") ("):
            buttons.append([int(c) for c in b.split(",")])
        joltages = [int(c) for c in line[line.find("{")+1:-1].split(",")]
        machines.append((lights, buttons, joltages))

    return machines


def getState(state: List[bool], button: List[int]) -> List[bool]:
    new_state = state.copy()
    for b in button:
        new_state[b] = not new_state[b]
    return new_state


def getMinButtonPresses(machine: Tuple[List[bool], List[List[int]], List[int]]) -> int:
    presses = 0
    goal, buttons, _ = machine
    candidates: List[Tuple[int, List[bool]]] = [(0, [False] * len(goal))]
    visited = set()
    while candidates:
        cur_presses, state = heappop(candidates)
        if state == goal:
            return cur_presses
        # Try mashing all buttons
        for b in buttons:
            next_state = getState(state, b)
            if tuple(next_state) not in visited:
                visited.add(tuple(next_state))
                heappush(candidates, (cur_presses + 1, getState(state, b)))

    return presses


def part1(input: List[str]) -> int:
    result = 0
    machines = getMachines(input)
    for m in machines:
        result += getMinButtonPresses(m)
    print(f'Day {day()}, Part 1: {result}')
    return result


def getJoltage(state: List[int], button: List[int]) -> List[int]:
    new_state = state.copy()
    for b in button:
        new_state[b] += 1
    return new_state


def getMinButtonPresses2(machine: Tuple[List[bool], List[List[int]], List[int]]) -> int:
    presses = 0
    _, buttons, goal = machine
    num_buttons = len(buttons)
    num_goals = len(goal)
    c = [1] * num_buttons
    button_masks = []
    for b in buttons:
        mask = 0
        if isinstance(b, int):
            mask |= 1 << b
        else:
            for bit in b:
                mask |= 1 << bit
        button_masks.append(mask)

    shifts = np.arange(num_goals)
    constraint_matrix = ((np.array(button_masks)[:, None] >> shifts) & 1).T.astype(
        float
    )

    target_vector = np.array(goal, dtype=float)

    # Fast Path: Use Least Squares for Deterministic/Overdetermined systems
    if num_buttons <= num_goals:
        try:
            x, _, rank, _ = np.linalg.lstsq(
                constraint_matrix, target_vector, rcond=None
            )
            x_rounded = np.round(x).astype(int)

            # Verify validity: Non-negative, Integer-close, Exact match
            # CRITICAL: Must be Full Rank (rank == num_buttons) to ensure uniqueness.
            if (
                rank == num_buttons
                and np.all(x_rounded >= 0)
                and np.allclose(x, x_rounded, atol=1e-5)
                and np.allclose(constraint_matrix @ x_rounded, target_vector)
            ):
                return int(np.sum(x_rounded))
        except np.linalg.LinAlgError:
            pass  # Fallback to linprog

    res = linprog(
        c,
        A_eq=constraint_matrix,
        b_eq=target_vector,
        bounds=(0, None),
        method="highs",
        integrality=True,
    )

    return round(res.fun)


def part2(input: List[str]) -> int:
    result = 0
    machines = getMachines(input)
    for m in machines:
        result += getMinButtonPresses2(m)
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
    ]


def test_day10_part1(puzzle_input: List[str]):
    assert part1(puzzle_input) == 7


def test_day10_part2(puzzle_input: List[str]):
    assert part2(puzzle_input) == 33
