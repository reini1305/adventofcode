import pytest
from typing import Dict, List
from aoc import day, get_input

def get_allergens(input:List[str])->Dict[str,List[str]]:
    candidates = {}
    for line in input:
        fi, fa = line[:-1].split(' (contains ')
        food_allergens = fa.split(', ')
        food_ingredients = set(fi.split(' '))
        for a in food_allergens:
            if a in candidates:
                candidates[a] &= food_ingredients
            else:
                candidates[a] = food_ingredients.copy()
    allergens=dict()
    while any([len(candidates[a])>0 for a in candidates]):
        # search for field that has only one candidate and remove from all others
        for a in candidates:
            if len(candidates[a]) == 1:
                allergens[a] = candidates[a].pop()
                for other in candidates:
                    try:
                        candidates[other].remove(allergens[a])
                    except KeyError:
                        pass
                break
    return allergens

def count_no_allergens(input, allergens):
    count = 0
    for line in input:
        fi, _ = line[:-1].split(' (contains ')
        for food_ingredients in fi.split(' '):
            if food_ingredients not in allergens.values():
                count += 1
    return count

def part1(input: List[str])-> None:
    allergens = get_allergens(input)
    result = count_no_allergens(input,allergens)
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    allergens = get_allergens(input)
    result = ','.join(allergens[a] for a in sorted(allergens))
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input(f'input{day()}.txt')
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    input = ['mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
            'trh fvjkl sbzzf mxmxvkd (contains dairy)',
            'sqjhc fvjkl (contains soy)',
            'sqjhc mxmxvkd sbzzf (contains fish)']
    return input

def test_day21_part1(puzzle_input):
    input = puzzle_input
    allergens = get_allergens(input)
    assert count_no_allergens(input,allergens) == 5

def test_day21_part2(puzzle_input):
    input = puzzle_input
    allergens = get_allergens(input)
    assert ','.join(allergens[a] for a in sorted(allergens)) == 'mxmxvkd,sqjhc,fvjkl'