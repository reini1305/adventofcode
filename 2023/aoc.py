import sys
import os
from typing import List


def day() -> str:
    filename = os.path.basename(sys.argv[0])
    return filename.split('.')[0]


def get_input() -> List[str]:
    filename = f"input{day()}.txt"
    with open(filename, 'r') as fp:
        input = [line.strip('\n') for line in fp.readlines()]
    return input


def get_num_input() -> List[int]:
    return [int(i) for i in get_input()]
