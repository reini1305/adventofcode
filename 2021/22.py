import re
from collections import namedtuple
from operator import le as less_than_or_equal
from typing import List
from aoc import day, get_input

Instruction = namedtuple("Instruction", "turn cuboid")
Coordinate = namedtuple("Coordinate", "x y z")
Cuboid = namedtuple("Cuboid", "min max")

def parse_instructions(input:List[str])->List[Instruction]:
    input_regex = re.compile(r"(?m)(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)")
    instructions:List[Instruction] = []
    for line in input:
        turn, x1, x2, y1, y2, z1, z2 = input_regex.match(line).groups()
        start = Coordinate(int(x1), int(y1), int(z1))
        end   = Coordinate(int(x2), int(y2), int(z2))
        my_cuboid = Cuboid(start, end)
        instructions.append(
            Instruction(turn, my_cuboid)
        )
    return instructions

def create_cuboids(instructions:List[Instruction])->List[Cuboid]:
    core:List[Cuboid] = []   # List to store the blocks that are on

    # Loop through all instructions
    for turn, new in instructions:
        new_core = []   # List of blocks that will be on after the current instruction

        # Loop through all blocks that are on
        for old in core:

            # Two cuboids intersect when the minimum coordinate of one is smaller
            # than the maximum coordinate of the other, for all 3 axes
            intersect = all(map(less_than_or_equal, new.min, old.max)) and all(map(less_than_or_equal, old.min, new.max))

            # If there is no overlap between the old and new blocks,
            # then the old block will still remain on regardless of the instruction
            if not intersect:
                new_core += [old]
                continue

            # Slice the blocks along the intersection plane formed by the instruction and the block that is on
            # (the parts of the blocks above all the six faces of the instruction will become new blocks,
            # while the intersection area is removed)
            
            # x-axis
            if old.min.x <= new.max.x <= old.max.x:  # Positive direction
                new_core += [Cuboid(
                    Coordinate(new.max.x+1, old.min.y, old.min.z), 
                    Coordinate(old.max.x,   old.max.y, old.max.z)
                )]
                old = Cuboid(
                    Coordinate(old.min.x, old.min.y, old.min.z), 
                    Coordinate(new.max.x, old.max.y, old.max.z)
                )

            if old.min.x <= new.min.x <= old.max.x:  # Negative direction
                new_core += [Cuboid(
                    Coordinate(old.min.x, old.min.y, old.min.z), 
                    Coordinate(new.min.x-1, old.max.y, old.max.z)
                )]
                old = Cuboid(
                    Coordinate(new.min.x, old.min.y, old.min.z), 
                    Coordinate(old.max.x, old.max.y, old.max.z)
                )

            # y-axis
            if old.min.y <= new.max.y <= old.max.y:  # Positive direction
                new_core += [Cuboid(
                    Coordinate(old.min.x, new.max.y+1, old.min.z), 
                    Coordinate(old.max.x, old.max.y, old.max.z)
                )]
                old = Cuboid(
                    Coordinate(old.min.x, old.min.y, old.min.z), 
                    Coordinate(old.max.x, new.max.y, old.max.z)
                )

            if old.min.y <= new.min.y <= old.max.y:  # Negative direction
                new_core += [Cuboid(
                    Coordinate(old.min.x, old.min.y, old.min.z), 
                    Coordinate(old.max.x, new.min.y-1, old.max.z)
                )]
                old = Cuboid(
                    Coordinate(old.min.x, new.min.y, old.min.z), 
                    Coordinate(old.max.x, old.max.y, old.max.z)
                )

            # z-axis
            if old.min.z <= new.max.z <= old.max.z:  # Positive direction
                new_core += [Cuboid(
                    Coordinate(old.min.x, old.min.y, new.max.z+1), 
                    Coordinate(old.max.x, old.max.y, old.max.z)
                )]
                old = Cuboid(
                    Coordinate(old.min.x, old.min.y, old.min.z), 
                    Coordinate(old.max.x, old.max.y, new.max.z)
                )

            if old.min.z <= new.min.z <= old.max.z:  # Negative direction
                new_core += [Cuboid(
                    Coordinate(old.min.x, old.min.y, old.min.z), 
                    Coordinate(old.max.x, old.max.y, new.min.z-1)
                )]
                old = Cuboid(
                    Coordinate(old.min.x, old.min.y, new.min.z), 
                    Coordinate(old.max.x, old.max.y, old.max.z)
                )
        
        # Process the operation
        if turn == "on": new_core += [new]  # If the area is to be turned on, add the region of the instruction
        else: assert turn == "off"          # Ensure that there are no instructions besides "on" and "off"
        core = new_core                     # Replace the old list of "on" blocks by the new one
    return core

def get_volume(cuboids:List[Cuboid], max_val:int=None)->int:
    volume = 0
    for block in cuboids:
        if max_val:
            if block.max.x < -max_val or block.max.y < -max_val or block.max.z < -max_val:
                continue
            if block.min.x > max_val or block.min.y > max_val or block.min.z > max_val:
                continue
            volume += (min(block.max.x,max_val) - max(block.min.x,-max_val) +1) * \
                      (min(block.max.y,max_val) - max(block.min.y,-max_val) +1) * \
                      (min(block.max.z,max_val) - max(block.min.z,-max_val) +1)
        else:
            volume += (block.max.x - block.min.x + 1) * (block.max.y - block.min.y + 1) * (block.max.z - block.min.z + 1)
    return volume

def part1(cuboids:List[Cuboid])-> None:
    result = get_volume(cuboids,50)
    print(f'Day {day()}, Part 1: {result}')

def part2(cuboids:List[Cuboid])-> None:
    result = get_volume(cuboids)
    print(f'Day {day()}, Part 1: {result}')

if __name__ == "__main__":
    input = get_input()
    instructions = parse_instructions(input)
    cuboids = create_cuboids(instructions)
    part1(cuboids)
    part2(cuboids)