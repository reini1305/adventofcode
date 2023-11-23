import pytest
from typing import DefaultDict, Dict, List
from collections import defaultdict
from aoc import day, get_input

def part1(input: List[str])-> int:
    result = 0
    for line in input:
        line = line[58:]
        result += sum([1 for word in line.split() if len(word) in [2, 4, 3, 7]])

    print(f'Day {day()}, Part 1: {result}')
    return result

def decode(input:str)->int:
    number_to_segment = {
        "abcefg":0,
        "cf":1,
        "acdeg":2,
        "acdfg":3,
        "bcdf":4,
        "abdfg":5,
        "abdefg":6,
        "acf":7,
        "abcdefg":8,
        "abcdfg":9
    }
    train, test = input.split('|')
    map = get_map(train.split())
    output = ''
    for number in test.split():
        output += str(number_to_segment["".join(sorted([map[c] for c in number]))])
    return int(output)


def get_map(input:List[str])->Dict[str,str]:
    one =   list(filter(lambda x: len(x)==2, input))[0]
    seven = list(filter(lambda x: len(x)==3, input))[0]
    four =  list(filter(lambda x: len(x)==4, input))[0]
    lights:DefaultDict[str,int] = defaultdict(int)
    for number in input:
        for segment in number:
            lights[segment] += 1
    map = {}
    for k, v in lights.items():
        if v == 9:
            map[k] = 'f'
        elif v == 4:
            map[k] = 'e'
        elif v == 6:
            map[k] = 'b'
        elif v == 8:
            if k in seven and k in one:
                map[k] = 'c'
            else:
                map[k] = 'a'
        elif v == 7:
            if k in four:
                map[k] = 'd'
            else:
                map[k] = 'g'

    return map

def part2(input: List[str])-> None:
    result = sum([decode(i) for i in input])
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
        "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
        "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
        "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
        "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
        "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
        "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
        "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
        "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
        "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"]

def test_day8_part1(puzzle_input):
    assert part1(puzzle_input) == 26

def test_day8_part2(puzzle_input):
    assert decode(puzzle_input[0]) == 8394