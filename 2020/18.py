import pytest
from typing import List, Tuple
from aoc import day, get_input
from operator import add, mul

def solvelines(input: List[str])->int:
    total: int = 0
    for line in input:
        total += int(solve(line))

    return total
        
def evaluate(s):
	equation = s.split(' ')
	total = int(equation[0])
	i = 0
	while i < len(equation) - 2:
		if equation[i + 1] == '+':
			total += int(equation[i + 2])
		elif equation[i + 1] == '*':
			total *= int(equation[i + 2])
		i += 2
	return total

def get_parentheses(eqn):
	if '(' in eqn:
		i = eqn.index('(') + 1
		num_open = 1
		while i < len(eqn):
			if eqn[i] == '(':
				num_open += 1
			elif eqn[i] == ')':
				num_open -= 1
			if num_open == 0:
				return [eqn[eqn.index('(') + 1 : i], eqn.index('('), i]
			i += 1
	else:
		return [eqn, -1, -1]

def solve(eqn:str)->str:
	if '(' not in eqn:
		return str(evaluate(eqn))
	else:
		inner, start_id, end_id = get_parentheses(eqn)
		return str(solve(eqn[0:start_id] + solve(inner) + eqn[end_id + 1:]))

def part1(input: List[str])-> None:
    result = solvelines(input)
    print(f'Day {day()}, Part 1: {result}')

def add_parentheses(eqn:str)->str:
    tokens = eqn.split(' ')
    for i in range(1,len(tokens)-1):
        if tokens[i] == '+':
            if tokens[i-1].endswith(')'):
                #search for corresponding '('
                j = i-2
                num_open = tokens[i-1].count(')')
                while j>=0:
                    num_open += tokens[j].count(')')
                    num_open -= tokens[j].count('(')
                    if num_open <= 0:
                        tokens[j] = '(' + tokens[j]
                        break
                    j -= 1
            else:
                tokens[i-1] = '(' + tokens[i-1]
            if tokens[i+1].startswith('('):
                #search for corresponding ')'
                j = i+2
                num_open = tokens[i+1].count('(')
                while j<len(tokens):
                    num_open += tokens[j].count('(')
                    num_open -= tokens[j].count(')')
                    if num_open <= 0:
                        tokens[j] = tokens[j] + ')'
                        break
                    j += 1
            else:
                tokens[i+1] = tokens[i+1] + ')'
    return ' '.join(tokens)

def solvelines2(input: List[str])->int:
    total: int = 0
    for line in input:
        total += int(solve(add_parentheses(line)))

    return total

def part2(input: List[str])-> None:
    result = solvelines2(input)
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input(f'input{day()}.txt')
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    input = ['2 * 3 + (4 * 5)',
             '2 * (2 * 3 + (4 * 5)) * 2',
            '5 + (8 * 3 + 9 + 3 * 4 * 3)',
            '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
            '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']
    return input

def test_day18_part1(puzzle_input):
    input = puzzle_input
    assert solve(input[0]) == '26'
    assert solve(input[1]) == '104'
    assert solve(input[2]) == '437'
    assert solve(input[3]) == '12240'
    assert solve(input[4]) == '13632'

def test_day18_part2(puzzle_input):
    input = puzzle_input
    assert solve(add_parentheses(input[0])) == '46'
    assert solve(add_parentheses('1 + (2 * 3) + (4 * (5 + 6))')) == '51'
    assert solve(add_parentheses(input[2])) == '1445'
    assert solve(add_parentheses(input[3])) == '669060'
    assert solve(add_parentheses(input[4])) == '23340'