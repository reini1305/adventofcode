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


def pad_array(array: List[str], value: str, amount: int):
    array_out: List[str] = []
    for line in array:
        array_out.append(value * amount + line + value * amount)
    for _ in range(amount):
        array_out.append(value * len(array_out[0]))
        array_out.insert(0, value * len(array_out[0]))
    return array_out
