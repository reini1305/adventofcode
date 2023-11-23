import pytest
from typing import List
from operator import mul
from functools import reduce
from aoc import day, get_input

def hex_to_bin(hex:str)->str:
    hex_size = len(hex) * 4
    return bin(int(hex,16))[2:].zfill(hex_size)

def parse_packet(binary:str):
    packet = {}
    # first three bits are version number
    packet['version'] = int(binary[:3],2)
    packet['id'] = int(binary[3:6],2)
    packet['packets'] = []
    curr = 6
    if packet['id'] == 4:
        #literal number
        number = ''
        while binary[curr] == '1':
            number += binary[curr+1:curr+5]
            curr += 5
        number += binary[curr+1:curr+5]
        curr += 5
        packet['value'] = int(number,2)
    else:
        #operator packet
        if binary[curr] == '0':
            curr += 1
            total_length = int(binary[curr:curr+15],2)
            curr += 15
            # until we reach the total_length parsed, parse the sub packages
            total_parsed = 0
            while total_parsed < total_length:
                subpackets, parsed = parse_packet(binary[curr:curr+total_length-total_parsed])
                packet['packets'].append(subpackets)
                total_parsed += parsed
                curr += parsed
        else:
            curr += 1
            num_subpackets = int(binary[curr:curr+11],2)
            curr += 11
            while len(packet['packets']) < num_subpackets:
                subpackets, parsed = parse_packet(binary[curr:])
                curr += parsed
                packet['packets'].append(subpackets)
    return packet, curr

def get_version_sum(packet):
    version_sum = packet['version']
    for p in packet['packets']:
        version_sum += get_version_sum(p)
    return version_sum

def calculate(packet):
    id = packet['id']
    if id == 4:
        return packet['value']
    if id == 0:
        return sum([calculate(p) for p in packet['packets']])
    if id == 1:
        return reduce(mul, [calculate(p) for p in packet['packets']])
    if id == 2:
        return min([calculate(p) for p in packet['packets']])
    if id == 3:
        return max([calculate(p) for p in packet['packets']])
    if id == 5:
        return calculate(packet['packets'][0]) > calculate(packet['packets'][1])
    if id == 6:
        return calculate(packet['packets'][0]) < calculate(packet['packets'][1])
    if id == 7:
        return calculate(packet['packets'][0]) == calculate(packet['packets'][1])

def part1(input: List[str])-> None:
    p,_ = parse_packet(hex_to_bin(input[0]))
    result = get_version_sum(p)
    print(f'Day {day()}, Part 1: {result}')

def part2(input: List[str])-> None:
    p,_ = parse_packet(hex_to_bin(input[0]))
    result = calculate(p)
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    part1(input)
    part2(input)

@pytest.fixture
def puzzle_input():
    return [
        'D2FE28',
        '38006F45291200',
        'EE00D40C823060',
        '8A004A801A8002F478',
        '620080001611562C8802118E34',
        'C0015000016115A2E0802F182340',
        'A0016C880162017C3686B18A3D4780'
    ]

def test_day16_part1(puzzle_input):
    packet = hex_to_bin(puzzle_input[0]) 
    assert packet == '110100101111111000101000'
    p,_ = parse_packet(packet)
    assert p['value'] == 2021
    p,_ = parse_packet(hex_to_bin(puzzle_input[2]))
    assert get_version_sum(p) == 14
    p,_ = parse_packet(hex_to_bin(puzzle_input[3]))
    assert get_version_sum(p) == 16
    p,_ = parse_packet(hex_to_bin(puzzle_input[4]))
    assert get_version_sum(p) == 12
    p,_ = parse_packet(hex_to_bin(puzzle_input[5]))
    assert get_version_sum(p) == 23
    p,_ = parse_packet(hex_to_bin(puzzle_input[6]))
    assert get_version_sum(p) == 31

def test_day16_part2(puzzle_input):
    p, _ = parse_packet(hex_to_bin('C200B40A82'))
    assert calculate(p) == 3
    p, _ = parse_packet(hex_to_bin('9C0141080250320F1802104A08'))
    assert calculate(p) == 1