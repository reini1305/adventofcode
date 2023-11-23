from re import split
from typing import Dict, List
import pytest
import re

from aoc import day, get_input

def split_passports(input: List[str]) -> List[Dict[str,str]]:
    passports = []
    passport: Dict[str,str] = {}
    for line in input:
        if line == '':
            passports.append(passport)
            passport = {}
        for pair in line.split(' '):
            if pair == '':
                continue
            key_value = pair.split(':')
            passport[key_value[0]] = key_value[1]
    passports.append(passport)
    return passports

def is_valid(passport:Dict[str,str])->bool:
    must_haves = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all([m in passport for m in must_haves])

def part1(input: List[Dict[str,str]])->None:
    print(f'Day {day()}, Part 1: {sum([1 for p in input if is_valid(p)])}')

def is_valid2(passport:Dict[str,str])->bool:
    if not is_valid(passport):
        return False
    if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        return False
    if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        return False
    if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        return False
    height = int(passport['hgt'][:-2])
    if passport['hgt'].endswith('cm'):
        if height < 150 or height > 193:
            return False
    else:
        if height < 59 or height > 76:
            return False
    eye_colors=['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if passport['ecl'] not in eye_colors:
        return False
    try:
        pid = int( passport['pid'])
        if len(passport['pid']) != 9:
            return False
    except:
        return False
    if not re.search(r'^#(?:[0-9a-f]{3}){1,2}$', passport['hcl']):
        return False
    return True
    
def part2(input: List[Dict])->None:
    print(f'Day {day()}, Part 2: {sum([1 for p in passports if is_valid2(p)])}')

if __name__ == "__main__":
    input = get_input(f'input{day()}.txt')
    passports = split_passports(input)
    part1(passports)
    part2(passports)

def test_day4_part1():
    passports= split_passports( ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
            'byr:1937 iyr:2017 cid:147 hgt:183cm',
            '',
            'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
            'hcl:#cfa07d byr:1929',
            '',
            'hcl:#ae17e1 iyr:2013',
            'eyr:2024',
            'ecl:brn pid:760753108 byr:1931',
            'hgt:179cm',
            '',
            'hcl:#cfa07d eyr:2025 pid:166559648',
            'iyr:2011 ecl:brn hgt:59in'])
    len(passports) == 4
    assert is_valid(passports[0]) == True
    assert is_valid(passports[1]) == False
    assert is_valid(passports[2]) == True
    assert is_valid(passports[3]) == False

def test_day4_part2():
    invalid_passports = split_passports(['eyr:1972 cid:100',
            'hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926',
            '',
            'iyr:2019',
            'hcl:#602927 eyr:1967 hgt:170cm',
            'ecl:grn pid:012533040 byr:1946',
            '',
            'hcl:dab227 iyr:2012',
            'ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277',
            '',
            'hgt:59cm ecl:zzz',
            'eyr:2038 hcl:74454a iyr:2023',
            'pid:3556412378 byr:2007'])

    assert all([not is_valid2(p) for p in invalid_passports]) == True

    valid_passports = split_passports(['pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980',
            'hcl:#623a2f',
            '',
            'eyr:2029 ecl:blu cid:129 byr:1989',
            'iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm',
            '',
            'hcl:#888785',
            'hgt:164cm byr:2001 iyr:2015 cid:88',
            'pid:545766238 ecl:hzl',
            'eyr:2022',
            '',
            'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'])
    
    assert all([is_valid2(p) for p in valid_passports]) == True