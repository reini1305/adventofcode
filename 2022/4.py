from typing import Set, Tuple

def check_contains(pair:Tuple[Set[int],Set[int]]) -> bool:
    return pair[0].issubset(pair[1]) or pair[1].issubset(pair[0])

def check_overlaps(pair:Tuple[Set[int],Set[int]]) -> bool:
    return not (pair[0].isdisjoint(pair[1]) or pair[1].isdisjoint(pair[0]))

region_pairs = []

with open('input4.txt') as f:
    for line in f:
        one, two = line.strip().split(',')
        one_start, one_stop = one.split('-')
        two_start, two_stop = two.split('-')
        region_pairs.append((
            set(range(int(one_start), int(one_stop) + 1)),
            set(range(int(two_start), int(two_stop) + 1))
        ))

part1 = 0
part2 = 0
for pair in region_pairs:
    part1 += check_contains(pair)
    part2 += check_overlaps(pair)

print(f"Day 4, Part 1: {part1}")
print(f"Day 4, Part 2: {part2}")
