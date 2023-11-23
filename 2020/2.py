from typing import Callable, List, Tuple
from aoc import day, get_input

def split_policy(policy:str) -> Tuple:
    parts = policy.strip('\n').split(' ')
    positions = [int(x) for x in parts[0].split('-')]
    char = parts[1][0]
    return positions, char, parts[2]

def check_policy(policy: str) -> bool:
    counts, char, password = split_policy(policy)
    return counts[0] <= password.count(char) <= counts[1]

def check_policy2(policy: str) -> bool:
    positions, char, password = split_policy(policy)
    return (password[positions[0]-1] == char) != (password[positions[1]-1] == char)

def part(policies: List[str], part_no: int, check_function: Callable[[str], bool]):
    count = sum([1 for policy in policies if check_function(policy)])
    print(f'Day {day()}, Part {part_no}: {count}')

if __name__ == "__main__":
    policies = get_input(f'input{day()}.txt')
    part(policies, part_no=1, check_function=check_policy)
    part(policies, part_no=2, check_function=check_policy2)

def test_day2_part1():
    assert check_policy('1-3 a: abcde') == True
    assert check_policy('1-3 b: cdefg') == False
    assert check_policy('2-9 c: ccccccccc') == True

def test_day2_part2():
    assert check_policy2('1-3 a: abcde') == True
    assert check_policy2('1-3 b: cdefg') == False
    assert check_policy2('2-9 c: ccccccccc') == False