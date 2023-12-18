import sys
import os
from typing import List, Tuple


def day() -> str:
    filename = os.path.basename(sys.argv[0])
    return filename.split('.')[0]


def get_input() -> List[str]:
    filename = f"{os.path.dirname(__file__)}/input{day()}.txt"
    with open(filename, 'r') as fp:
        input = [line.strip('\n') for line in fp.readlines()]
    return input


def get_num_input() -> List[int]:
    return [int(i) for i in get_input()]


def tuple_add(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return (a[0] + b[0], a[1] + b[1])


def tuple_mul(a: Tuple[int, int], b: int) -> Tuple[int, int]:
    return (a[0] * b, a[1] * b)
