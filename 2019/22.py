from copy import deepcopy

def deal_cards(num_cards, instructions):
    cards = list(range(num_cards))
    for i in instructions:
        if i.startswith('deal with'):
            number = int(i.split(' ')[-1])
            old_cards = deepcopy(cards)
            new_pos = 0
            for n in range(num_cards):
                cards[new_pos] = old_cards[n]
                new_pos = (new_pos + number) % num_cards
        elif i.startswith('cut'):
            number = int(i.split(' ')[-1])
            cards = cards[number:] + cards[:number]
        elif i.startswith('deal into'):
            cards.reverse()
    return cards

def part1(instructions):
    cards = deal_cards(10007,instructions)
    return cards.index(2019)

if __name__ == "__main__":
    with open('input22.txt','r') as f:
        instructions = f.readlines()
    assert deal_cards(10,["cut -4"]) == [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
    assert deal_cards(10,["cut 3"]) == [3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
    assert deal_cards(10,["deal into new deck"]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert deal_cards(10,["deal with increment 3"]) == [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]
    
    print('Day 22, Part 1: {}'.format(part1(instructions)))