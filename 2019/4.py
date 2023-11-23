def check_number(number):
    num_array = [c for c in str(number)]
    adjacent = 1
    adjacents = []
    for x, y in zip(num_array[0::], num_array[1::]): 
        if x == y:
            adjacent +=1
        else:
            adjacents.append(adjacent)
            adjacent = 1
    adjacents.append(adjacent)
    issorted = num_array == sorted(num_array)
    if issorted:
        return (max(adjacents) > 1, 2 in adjacents)
    else:
        return (False, False)

if __name__ == "__main__":
    # Tests
    assert check_number(111111)[0] == True
    assert check_number(223450)[0] == False
    assert check_number(123789)[0] == False

    assert check_number(112233)[1] == True
    assert check_number(123444)[1] == False
    assert check_number(111122)[1] == True

    num_correct_1 = 0
    num_correct_2 = 0
    for num in range(271973, 785961 + 1):
        (p1, p2) = check_number(num)
        if p1:
            num_correct_1 += 1
        if p2:
            num_correct_2 += 1
    print("Day 4, Part 1: {}".format(num_correct_1))
    print("Day 4, Part 2: {}".format(num_correct_2))