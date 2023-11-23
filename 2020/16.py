import pytest
from typing import List, Dict, Set, Tuple
from aoc import day, get_input
from operator import mul
from functools import reduce

def get_scanning_errors(nearby_tickets:List[List[int]], fields:Dict[str,List[int]])->List[int]:
    return [value for ticket in nearby_tickets for value in ticket if not any(value in fields[field] for field in fields)]

def parse_input(input: List[str])->Tuple[Dict[str,List[int]],List[List[int]],List[int]]:
    fields:Dict[str,List[int]] = {}
    nearby_tickets:List[List[int]] = []
    i = 0
    line = input[i]
    # Parse fields
    while line != '':
        field_name, rest = line.split(':')
        fields[field_name] = []
        ranges = rest.split('or')
        for r in ranges:
            start, end = r.split('-')
            fields[field_name].extend(list(range(int(start), int(end)+1)))
        i += 1
        line = input[i]
    # Parse my ticket
    i += 2
    my_ticket = [int(t) for t in input[i].split(',')]
    # Parse nearby tickets
    i += 3
    while i < len(input):
        nearby_tickets.append([int(t) for t in input[i].split(',')])
        i += 1
    return fields, nearby_tickets, my_ticket

def part1(input: List[str])-> None:
    fields, nearby_tickets, _ = parse_input(input)
    result = sum(get_scanning_errors(nearby_tickets, fields))
    print(f'Day {day()}, Part 1: {result}')

def get_fields_order(nearby_tickets:List[List[int]], fields:Dict[str,List[int]])->List[str]:
    invalid_ids = get_scanning_errors(nearby_tickets,fields)
    valid_tickets = [n for n in nearby_tickets if all([v not in invalid_ids for v in n])]
    ordered_fields:List[str] = [""] * len(fields)
    candidates = [set([field for field in fields if all([v[i] in fields[field] for v in valid_tickets])]) for i in range(len(fields))]
    while any([len(c)>0 for c in candidates]):
        # search for field that has only one candidate and remove from all others
        id = [len(c) for c in candidates].index(1)
        ordered_fields[id] = candidates[id].pop()
        for c in candidates:
            try:
                c.remove(ordered_fields[id])
            except KeyError:
                pass
    return ordered_fields

def part2(input: List[str])-> None:
    fields, nearby_tickets, my_ticket = parse_input(input)
    ordered_fields = get_fields_order(nearby_tickets,fields)
    result = reduce(mul,[my_ticket[i] for i,of in enumerate(ordered_fields) if of.startswith('departure')])
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input(f'input{day()}.txt')
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    fields = ['class: 1-3 or 5-7',
            'row: 6-11 or 33-44',
            'seat: 13-40 or 45-50',
            '',
            'your ticket:',
            '7,1,14',
            '',
            'nearby tickets:',
            '7,3,47',
            '40,4,50',
            '55,2,20',
            '38,6,12']

    return fields

def test_day16_part1(puzzle_input):
    input = puzzle_input
    fields, nearby_tickets, _ = parse_input(input)
    assert sum(get_scanning_errors(nearby_tickets, fields)) == 71

def test_day16_part2():
    input = ['class: 0-1 or 4-19',
            'row: 0-5 or 8-19',
            'seat: 0-13 or 16-19',
            '',
            'your ticket:',
            '11,12,13',
            '',
            'nearby tickets:',
            '3,9,18',
            '15,1,5',
            '5,14,9']
    fields, nearby_tickets, my_ticket = parse_input(input)
    assert get_fields_order(nearby_tickets, fields) == ['row', 'class', 'seat']