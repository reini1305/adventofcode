import pytest
from typing import Dict, List
from aoc import day, get_input

class File:
    def __init__(self, name, filesize) -> None:
        self.name = name
        self.filesize = filesize

class Dir:
    def __init__(self, name:str, parent) -> None:
        self.dirs:Dict[str,Dir] = {}
        self.files:Dict[str,File] = {}
        self.name = name
        self.parent = parent
        self.total_size = 0

    def add_dir(self, name):
        self.dirs[name] = Dir(name, self)

    def add_file(self, name, size):
        self.files[name] = File(name, size)
        self.add_size(size)

    def add_size(self, size):
        self.total_size += size
        if self.parent:
            self.parent.add_size(size)

def parse_input(input: List[str]):
    fs = Dir('/', None)
    cd = fs
    for line in input:
        if line.startswith('$'):
            command = line.strip().split(' ')
            if command[1] == 'cd':
                if command[2] == '..':
                    cd = cd.parent
                elif command[2] != '/':
                    cd = cd.dirs[command[2]]
            # we can ignore ls command
        else:
            # we see the ls output and need to update the current dir
            ls_output = line.strip().split(' ')
            if ls_output[0] == 'dir':
                cd.add_dir(ls_output[1])
            else:
                cd.add_file(ls_output[1], int(ls_output[0]))
    return fs

def get_dirs_smaller_than(fs:Dir, max_size:int, result:List[int]) -> None:
    if fs.total_size < max_size:
        result.append(fs.total_size)
    for dir in fs.dirs:
        get_dirs_smaller_than(fs.dirs[dir], max_size, result)

def get_dirs_bigger_than(fs:Dir, max_size:int, result:List[int]) -> None:
    if fs.total_size >= max_size:
        result.append(fs.total_size)
    for dir in fs.dirs:
        get_dirs_bigger_than(fs.dirs[dir], max_size, result)

def part1(input: List[str])-> None:
    fs = parse_input(input)
    result = []
    get_dirs_smaller_than(fs, 100000, result)
    print(f'Day {day()}, Part 1: {sum(result)}')

def part2(input: List[str])-> None:
    fs = parse_input(input)
    free_space = 70000000 - fs.total_size
    needed_space = 30000000 - free_space
    result = []
    get_dirs_bigger_than(fs, needed_space, result)
    print(f'Day {day()}, Part 2: {min(result)}')

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k"
    ]

def test_dayx_part1(puzzle_input):
    fs = parse_input(puzzle_input)
    assert fs.total_size == 48381165
    assert fs.dirs['d'].total_size == 24933642
    result = []
    get_dirs_smaller_than(fs, 100000, result)
    assert sum(result) == 95437

def test_dayx_part2(puzzle_input):
    fs = parse_input(puzzle_input)
    free_space = 70000000 - fs.total_size
    needed_space = 30000000 - free_space
    result = []
    get_dirs_bigger_than(fs, needed_space, result)
    assert len(result) == 2
    assert min(result) == 24933642