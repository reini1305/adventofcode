import pytest
from typing import Dict, List, Tuple
from aoc import day, get_input


def getInputs(input: List[str]) -> Dict[str, int]:
    inputs = {}
    for line in input:
        if line == '':
            break
        name, val = line.split(': ')
        inputs[name] = int(val)
    return inputs


def getOperations(input: List[str]) -> Dict[str, Tuple[str, str, str]]:
    operations = {}
    for line in input:
        if '->' not in line:
            continue
        ops, name = line.split(' -> ')
        op1, op, op2 = ops.split(' ')
        operations[name] = (op1, op2, op)
    return operations


def getOutput(name: str,
              operations: Dict[str, Tuple[str, str, str]],
              inputs: Dict[str, int],
              outputs: Dict[str, int]):
    if name in outputs:
        return outputs[name]
    op1, op2, op = operations[name]
    val1 = inputs[op1] if op1 in inputs else getOutput(op1, operations, inputs, outputs)
    val2 = inputs[op2] if op2 in inputs else getOutput(op2, operations, inputs, outputs)
    result = 0
    if op == 'OR':
        result = val1 | val2
    elif op == 'XOR':
        result = val1 ^ val2
    elif op == 'AND':
        result = val1 & val2
    outputs[name] = result
    return result


def part1(input: List[str]) -> int:
    result = 0
    inputs = getInputs(input)
    operations = getOperations(input)
    outputs: Dict[str, int] = {}
    all_outputs = sorted([n for n in operations if n.startswith('z')])
    for i, out in enumerate(all_outputs):
        result += (2 ** i) * getOutput(out, operations, inputs, outputs)
    print(f'Day {day()}, Part 1: {result}')
    return result


def findGate(x: str, y: str, op: str, operations: Dict[str, Tuple[str, str, str]]) -> str:
    if (x, y, op) in operations.values():
        return list(operations.keys())[list(operations.values()).index((x, y, op))]
    if (y, x, op) in operations.values():
        return list(operations.keys())[list(operations.values()).index((y, x, op))]
    return ""


def swapOutputWires(gate1: str, gate2: str, operations: Dict[str, Tuple[str, str, str]]):
    temp = operations[gate1]
    operations[gate1] = operations[gate2]
    operations[gate2] = temp


def checkParallelAdders(operations: Dict[str, Tuple[str, str, str]], inputs: Dict[str, int]):
    current_carry_wire = ""
    swaps = []
    bit = 0

    while True:
        x_wire = f'x{bit:02d}'
        y_wire = f'y{bit:02d}'
        z_wire = f'z{bit:02d}'
        if x_wire not in inputs or y_wire not in inputs:
            break

        if bit == 0:
            current_carry_wire = findGate(x_wire, y_wire, 'AND', operations)
        else:
            ab_xor_gate = findGate(x_wire, y_wire, 'XOR', operations)
            ab_and_gate = findGate(x_wire, y_wire, 'AND', operations)

            cin_ab_xor_gate = findGate(ab_xor_gate, current_carry_wire, 'XOR', operations)
            if cin_ab_xor_gate == "":
                swaps.append(ab_xor_gate)
                swaps.append(ab_and_gate)
                swapOutputWires(ab_xor_gate, ab_and_gate, operations)
                bit = 0
                continue
            elif cin_ab_xor_gate != z_wire:
                swaps.append(cin_ab_xor_gate)
                swaps.append(z_wire)
                swapOutputWires(cin_ab_xor_gate, z_wire, operations)
                bit = 0
                continue

            cin_ab_and_gate = findGate(ab_xor_gate, current_carry_wire, 'AND', operations)

            carry_wire = findGate(ab_and_gate, cin_ab_and_gate, 'OR', operations)
            current_carry_wire = carry_wire

        bit += 1

    return swaps


def part2(input: List[str]) -> str:
    result = ''
    inputs = getInputs(input)
    operations = getOperations(input)
    swaps = checkParallelAdders(operations, inputs)
    result = ",".join(sorted(swaps))
    print(f'Day {day()}, Part 2: {result}')
    return result


if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)


@pytest.fixture
def puzzle_input():
    return [
        'x00: 1',
        'x01: 0',
        'x02: 1',
        'x03: 1',
        'x04: 0',
        'y00: 1',
        'y01: 1',
        'y02: 1',
        'y03: 1',
        'y04: 1',
        '',
        'ntg XOR fgs -> mjb',
        'y02 OR x01 -> tnw',
        'kwq OR kpj -> z05',
        'x00 OR x03 -> fst',
        'tgd XOR rvg -> z01',
        'vdt OR tnw -> bfw',
        'bfw AND frj -> z10',
        'ffh OR nrd -> bqk',
        'y00 AND y03 -> djm',
        'y03 OR y00 -> psh',
        'bqk OR frj -> z08',
        'tnw OR fst -> frj',
        'gnj AND tgd -> z11',
        'bfw XOR mjb -> z00',
        'x03 OR x00 -> vdt',
        'gnj AND wpb -> z02',
        'x04 AND y00 -> kjc',
        'djm OR pbm -> qhw',
        'nrd AND vdt -> hwm',
        'kjc AND fst -> rvg',
        'y04 OR y02 -> fgs',
        'y01 AND x02 -> pbm',
        'ntg OR kjc -> kwq',
        'psh XOR fgs -> tgd',
        'qhw XOR tgd -> z09',
        'pbm OR djm -> kpj',
        'x03 XOR y03 -> ffh',
        'x00 XOR y04 -> ntg',
        'bfw OR bqk -> z06',
        'nrd XOR fgs -> wpb',
        'frj XOR qhw -> z04',
        'bqk OR frj -> z07',
        'y03 OR x01 -> nrd',
        'hwm AND bqk -> z03',
        'tgd XOR rvg -> z12',
        'tnw OR pbm -> gnj',
    ]


def test_day24_part1(puzzle_input):
    assert part1(puzzle_input) == 2024
