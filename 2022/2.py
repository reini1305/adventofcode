opponent_moves = []
my_moves = []

with open('input2.txt') as f:
    for line in f:
        opponent_moves.append(line[0])
        my_moves.append(line[2])

def play_round(o:str, m:str) -> int:
    score = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2}
    win = {'X': 'C', 'Y': 'A', 'Z': 'B'}
    if score[m] == score[o]:
        return 3 + score[m] + 1
    if win[m] == o:
        return 6 + score[m] + 1
    return score[m] + 1

def what_to_play(opp:str, outcome:str) -> str:
    to_win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    to_lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    if outcome == 'X':
        return to_lose[opp]
    if outcome == 'Y':
        return opp
    return to_win[opp]

part1 = 0
part2 = 0
# opponent_moves = ['A', 'B', 'C']
# my_moves = ['Y', 'X', 'Z' ]
for o,m in zip(opponent_moves, my_moves):
    part1 += play_round(o, m)
    part2 += play_round(o, what_to_play(o, m))

print(f"Day 2, Part 1: {part1}")
print(f"Day 2, Part 2: {part2}")

