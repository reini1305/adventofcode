import pytest
from typing import List
from aoc import day, get_input

def die():
    current = 0
    while True:
        current += 1
        if current > 100:
            current = 1
        yield current

def play(start):
    scores = [0, 0]
    current = start
    roll = 0
    d = die()
    while not any(s >= 1000 for s in scores):
        for player in range(2):
            current[player] += sum([next(d), next(d), next(d)])
            roll += 3
            current[player] = mod10(current[player])
            scores[player] += current[player]
            if scores[player] >= 1000:
                break

    return roll, scores

def mod10(val):
    while val > 10: val -= 10
    return val

def part1(input: List[int])-> None:
    roll, scores = play(input)
    result = roll * min(scores)
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[int])-> None:
    moveset = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    update_tuple = lambda t, i, n: ([n, t[0]][i], [t[1],n][i])

    total_wins = [0, 0]
    universes = {((0, 0), (input[0], input[1]), 0): 1}

    while universes:
        for (score, pos, turn), old_count in sorted(universes.items()):
            del universes[(score, pos, turn)]
            for move, count in moveset.items():
                updated_pos = mod10(pos[turn] + move)
                updated_score = score[turn] + updated_pos
                updated_count = old_count * count
                if updated_score >= 21:
                    total_wins[turn] += updated_count
                    continue
                new_pos = update_tuple(pos, turn, updated_pos)
                new_score = update_tuple(score, turn, updated_score)
                new_key = (new_score, new_pos, (turn+1)%2)
                universes[new_key] = universes.get(new_key, 0) + updated_count

    result = max(total_wins)
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = [10, 8]
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [4,8]

def test_day21_part1(puzzle_input):
    rolls, scores = play(puzzle_input)
    assert rolls == 993
    assert scores == [1000, 745]

def test_day21_part2(puzzle_input):
    assert 1