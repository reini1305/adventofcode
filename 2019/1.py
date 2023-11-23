def calcFuel(mass):
    return max(mass // 3 - 2, 0)
def part1(components):
    fuel = sum(map(calcFuel, components))
    return fuel

def calcFuelWithFuel(mass):
        total = 0 
        fuel = calcFuel(mass)
        if fuel == 0:
            return 0
        else:
            return total + fuel + calcFuelWithFuel(fuel)

def part2(components):
    fuel = sum(map(calcFuelWithFuel, components)) 
    return fuel 

if __name__ == "__main__":
    with open('input1.txt','r') as f:
        components = [int(l) for l in f]
    assert part1([12]) == 2
    assert part1([14]) == 2
    assert part1([1969]) == 654
    assert part1([100756]) == 33583
    assert part2([14]) == 2
    assert part2([1969]) == 966
    assert part2([100756]) == 50346
    print("Day 1, Part 1: {}".format(part1(components)))
    print("Day 1, Part 2: {}".format(part2(components)))