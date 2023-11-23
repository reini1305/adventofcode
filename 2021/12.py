import pytest
from typing import Dict, List
from aoc import day, get_input

def parse_input(input: List[str])->Dict[str,List[str]]:
    graph:Dict[str,List[str]] = {}
    for line in input:
        f, t = line.split('-')
        if f in graph:
            graph[f].append(t)
        else:
            graph[f] = [t]
        if t in graph:
            graph[t].append(f)
        else:
            graph[t] = [f]
    return graph

def find_all_routes(graph:Dict[str,List[str]], p2:bool=False)->int:
    routes = set()
    def find_routes(current:str, path:List[str], p2:bool=False)->int:
        if current == 'end':
            routes.add(tuple(path))
            return 0
        for child in graph[current]:
            if (child == 'start' or (child.islower() and child in path) and not p2) \
            or (child == 'start' or (child.islower() and child in path and any(path.count(y) > 1 for y in path if y.islower())) and p2):
                continue
            find_routes(child, path + [child], p2)
        return len(routes)
    
    return find_routes('start',['start'],p2)

def part1(input: List[str])-> None:
    graph = parse_input(input)
    result = find_all_routes(graph)
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    graph = parse_input(input)
    result = find_all_routes(graph, True)
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        "start-A",
        "start-b",
        "A-c",
        "A-b",
        "b-d",
        "A-end",
        "b-end",
    ]

def test_day12_part1(puzzle_input):
    graph = parse_input(puzzle_input)
    assert graph['start'] == ['A', 'b']
    assert find_all_routes(graph) == 10

def test_day12_part2(puzzle_input):
    graph = parse_input(puzzle_input)
    assert find_all_routes(graph,True) == 36