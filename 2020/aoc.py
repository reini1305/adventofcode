import sys
import os 
from typing import Callable, List, Tuple

def day() -> str:
    filename = os.path.basename(sys.argv[0])
    return filename.split('.')[0]

def get_input(filename: str) -> List[str]:
    with open(filename,'r') as fp:
        input = [line.strip('\n') for line in fp.readlines()]
    return input

def get_num_input(filename: str) -> List[int]:
    return [int(i) for i in get_input(filename)]

class Assembler:
    def __init__(self) -> None:
        self.accumulator = 0
        self.ip = 0
        self.code:List[Tuple[Callable[[VarArg(int)],None],List[int]]] = []
        self.operatormap = {
            'acc':self.acc,
            'jmp':self.jmp,
            'nop':self.nop}

    def decode(self, input:List[str])->None:
        self.code = []
        self.accumulator = 0
        self.ip = 0
        for line in input:
            op, *vals = line.strip().split()
            self.code.append((self.operatormap[op],list(map(int,vals))))

    # operators
    def acc(self, *vals:int)->None:
        self.accumulator += vals[0]
        self.ip += 1

    def jmp(self, *vals:int)->None:
        self.ip += vals[0]

    def nop(self, *vals:int)->None:
        self.ip += 1