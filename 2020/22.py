import pytest
from typing import Deque, List, Set
from aoc import day, get_input
from collections import deque
from copy import deepcopy

def parse_input(input):
    deck_1 = deque()
    deck_2 = deque()
    player_1 = True
    for line in input:
        try:
            card = int(line)
            if player_1:
                deck_1.append(card)
            else:
                deck_2.append(card)
        except:
            if line == 'Player 2:':
                player_1 = False
    return (deck_1, deck_2)

def play_until_win(deck_1:Deque[int], deck_2:Deque[int]):
    while len(deck_1) > 0 and len(deck_2) > 0:
        c1 = deck_1.popleft()
        c2 = deck_2.popleft()
        if c1 > c2:
            deck_1.append(c1)
            deck_1.append(c2)
        if c2 > c1:
            deck_2.append(c2)
            deck_2.append(c1)

def play_recursive_until_win(deck_1:Deque[int], deck_2:Deque[int]):
    prev_1:Set = set()
    prev_2:Set = set()
    while len(deck_1) > 0 and len(deck_2) > 0:
        if tuple(deck_1) in prev_1 or tuple(deck_2) in prev_2:
            return True
        prev_1.add(tuple(deck_1))
        prev_2.add(tuple(deck_2))
        c1 = deck_1.popleft()
        c2 = deck_2.popleft()
        if len(deck_1) >= c1 and len(deck_2) >= c2:
            #play recursive game
            new_deck_1 = deepcopy(deck_1)
            while len(new_deck_1)>c1:
                new_deck_1.pop()
            new_deck_2 = deepcopy(deck_2)
            while len(new_deck_2)>c2:
                new_deck_2.pop()
            if play_recursive_until_win(new_deck_1, new_deck_2):
                deck_1.append(c1)
                deck_1.append(c2)
            else:
                deck_2.append(c2)
                deck_2.append(c1)
        else:
            if c1 > c2:
                deck_1.append(c1)
                deck_1.append(c2)
            if c2 > c1:
                deck_2.append(c2)
                deck_2.append(c1)
    return len(deck_2) == 0

def part1(input: List[str])-> None:
    decks = parse_input(input)
    play_until_win(*decks)
    d = decks[0] if len(decks[0])>0 else decks[1]
    result = sum([c*i for c,i in zip(d,range(len(d),0,-1))])
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    decks = parse_input(input)
    play_recursive_until_win(*decks)
    d = decks[0] if len(decks[0])>0 else decks[1]
    result = sum([c*i for c,i in zip(d,range(len(d),0,-1))])
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input(f'input{day()}.txt')
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    input = ['Player 1:',
                '9',
                '2',
                '6',
                '3',
                '1',
                '',
                'Player 2:',
                '5',
                '8',
                '4',
                '7',
                '10']
    return input

def test_day22_part1(puzzle_input):
    input = puzzle_input
    decks = parse_input(input)
    play_until_win(*decks)
    assert len(decks[1]) == 10
    d = decks[0] if len(decks[0])>0 else decks[1]
    result = sum([c*i for c,i in zip(d,range(len(d),0,-1))])
    assert result == 306

def test_day22_part2(puzzle_input):
    input = puzzle_input
    decks = parse_input(input)
    play_recursive_until_win(*decks)
    assert len(decks[1]) == 10
    d = decks[0] if len(decks[0])>0 else decks[1]
    result = sum([c*i for c,i in zip(d,range(len(d),0,-1))])
    assert result == 291