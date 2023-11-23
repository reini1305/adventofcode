import pytest
from typing import List
from itertools import permutations
from collections import defaultdict
from aoc import day, get_input

def orientation():
    """Yields each of 8 possible orientations"""
    for i in range(8):
        yield (-1) ** (i % 2), (-1) ** ((i // 2) % 2), (-1) ** ((i // 4) % 2)


class Scanner:
    def __init__(self, num, pos=None):
        self.beacons = defaultdict(set)
        self.num = num
        self.pos = pos
        self.orient = None
        self.perm = None


    def add_beacon(self, beacon):
        # precalculate all orientations
        for orient in orientation():
            for perm in permutations((0,1,2)):
                self.beacons[orient, perm].add(tuple(o*beacon[dp] for o, dp in zip(orient, perm)))

    def compare(self, other):
        # Possible positions from self
        # For each orientation and permutation (?? 48 possible orientations ??)
        for orient in orientation():
            for perm in permutations((0, 1, 2)):
                c = defaultdict(int)

                # Compare each beacon from each scanner
                for a in self.get_beacons():
                    for b in other.beacons[orient, perm]:
                        # Assume a is absolute, find other.pos
                        c[tuple([da+db for da,db in zip(a,b)])] += 1

                # If 12 beacons have the same comparison, k is the absolute position of the other scanner
                for k, v in c.items():
                    if v >= 12:
                        other.pos = k

                        # Reorient all beacons based on absolute position

                        other.reorient(orient, perm)
                        return True

    def get_beacons(self):
        return self.beacons[self.orient, self.perm]

    def reorient(self, orient, perm):
        self.orient = orient
        self.perm = perm
        new_s = set()
        for b in self.beacons[self.orient, self.perm]:
            new_b = tuple(self.pos[order] - b[order] for order in (0, 1, 2))
            new_s.add(new_b)

        self.beacons[self.orient, self.perm] = new_s

def parse(input: List[str]):
    scanners = []
    current = 0
    for line in input:
        if line =='':
            continue
        if line.startswith('---'):
            scanners.append(Scanner(current))
            current += 1
            continue
        scanners[-1].add_beacon(tuple(int(x) for x in line.split(',')))
    return scanners

def align_scanners(scanners):
    known = set([0])
    scanners[0].pos = (0,0,0)
    scanners[0].orient = (1,1,1)
    scanners[0].perm = (0,1,2)
    while len(known) < len(scanners):
        new = set()
        for k in known:
            for i in range(len(scanners)):
                if i in known:
                    continue
                if scanners[k].compare(scanners[i]):
                    new.add(i)
        known |= new
        print(f'Mapped {len(known)} ...')

def manhattan_distance(p1,p2):
    return sum(abs(pp1-pp2) for pp1,pp2 in zip(p1,p2))

def part1(scanners)-> None:
    points = set()
    for s in scanners:
        points |= s.get_beacons()

    print(f'Day {day()}, Part 1: {len(points)}')

def part2(scanners)-> None:
    result = 0
    for s1 in scanners:
        for s2 in scanners:
            result = max(result, manhattan_distance(s1.pos, s2.pos))
    print(f'Day {day()}, Part 2: {result}')

if __name__ == "__main__":
    input = get_input()
    scanners = parse(input)
    align_scanners(scanners)
    part1(scanners)
    part2(scanners)

@pytest.fixture
def puzzle_input():
    return [
        '--- scanner 0 ---',
        '404,-588,-901',
        '528,-643,409',
        '-838,591,734',
        '390,-675,-793',
        '-537,-823,-458',
        '-485,-357,347',
        '-345,-311,381',
        '-661,-816,-575',
        '-876,649,763',
        '-618,-824,-621',
        '553,345,-567',
        '474,580,667',
        '-447,-329,318',
        '-584,868,-557',
        '544,-627,-890',
        '564,392,-477',
        '455,729,728',
        '-892,524,684',
        '-689,845,-530',
        '423,-701,434',
        '7,-33,-71',
        '630,319,-379',
        '443,580,662',
        '-789,900,-551',
        '459,-707,401',
        '',
        '--- scanner 1 ---',
        '686,422,578',
        '605,423,415',
        '515,917,-361',
        '-336,658,858',
        '95,138,22',
        '-476,619,847',
        '-340,-569,-846',
        '567,-361,727',
        '-460,603,-452',
        '669,-402,600',
        '729,430,532',
        '-500,-761,534',
        '-322,571,750',
        '-466,-666,-811',
        '-429,-592,574',
        '-355,545,-477',
        '703,-491,-529',
        '-328,-685,520',
        '413,935,-424',
        '-391,539,-444',
        '586,-435,557',
        '-364,-763,-893',
        '807,-499,-711',
        '755,-354,-619',
        '553,889,-390',
        '',
        '--- scanner 2 ---',
        '649,640,665',
        '682,-795,504',
        '-784,533,-524',
        '-644,584,-595',
        '-588,-843,648',
        '-30,6,44',
        '-674,560,763',
        '500,723,-460',
        '609,671,-379',
        '-555,-800,653',
        '-675,-892,-343',
        '697,-426,-610',
        '578,704,681',
        '493,664,-388',
        '-671,-858,530',
        '-667,343,800',
        '571,-461,-707',
        '-138,-166,112',
        '-889,563,-600',
        '646,-828,498',
        '640,759,510',
        '-630,509,768',
        '-681,-892,-333',
        '673,-379,-804',
        '-742,-814,-386',
        '577,-820,562',
        '',
        '--- scanner 3 ---',
        '-589,542,597',
        '605,-692,669',
        '-500,565,-823',
        '-660,373,557',
        '-458,-679,-417',
        '-488,449,543',
        '-626,468,-788',
        '338,-750,-386',
        '528,-832,-391',
        '562,-778,733',
        '-938,-730,414',
        '543,643,-506',
        '-524,371,-870',
        '407,773,750',
        '-104,29,83',
        '378,-903,-323',
        '-778,-728,485',
        '426,699,580',
        '-438,-605,-362',
        '-469,-447,-387',
        '509,732,623',
        '647,635,-688',
        '-868,-804,481',
        '614,-800,639',
        '595,780,-596',
        '',
        '--- scanner 4 ---',
        '727,592,562',
        '-293,-554,779',
        '441,611,-461',
        '-714,465,-776',
        '-743,427,-804',
        '-660,-479,-426',
        '832,-632,460',
        '927,-485,-438',
        '408,393,-506',
        '466,436,-512',
        '110,16,151',
        '-258,-428,682',
        '-393,719,612',
        '-211,-452,876',
        '808,-476,-593',
        '-575,615,604',
        '-485,667,467',
        '-680,325,-822',
        '-627,-443,-432',
        '872,-547,-609',
        '833,512,582',
        '807,604,487',
        '839,-516,451',
        '891,-625,532',
        '-652,-548,-490',
        '30,-46,-14'
    ]

def test_day19_part1(puzzle_input):
    scanners = parse(puzzle_input)
    assert len(scanners) == 5
    align_scanners(scanners)
    points = set()
    for s in scanners:
        points |= s.get_beacons()
    assert len(points) == 79

def test_day19_part2(puzzle_input):
    assert manhattan_distance((1105,-1205,1229),(-92,-2380,-20)) == 3621