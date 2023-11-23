from itertools import chain

with open('input3.txt') as f:
    rucksacks = [line.strip() for line in f]

costs = {chr(key): value for key,value in zip(chain(range(97, 123), range(65, 91)), range(1,53))}

part1 = 0
for rucksack in rucksacks:
    compartment_1 = set(rucksack[:len(rucksack)//2])
    compartment_2 = set(rucksack[len(rucksack)//2:])
    part1 += costs[compartment_1.intersection(compartment_2).pop()]

part2 = 0
for group in zip(*[iter(rucksacks)]*3):
    part2 += costs[set(group[0]).intersection(set(group[1])).intersection(set(group[2])).pop()]

print(f"Day 3, Part 1: {part1}")
print(f"Day 3, Part 2: {part2}")