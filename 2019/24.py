from copy import deepcopy
from operator import itemgetter

def part1(input):
    input = [ c for c in ''.join(input)]
    rel_adjacent_ids = [-5,5,-1,1]
    adjacent_ids = [[i + j for j in rel_adjacent_ids if (i+j)>=0 and (i+j)<25 and not(i%5==0 and j==-1) and not (i%5==4 and j==1)] 
             for i in range(25)]
    seen = set()
    while ''.join(input) not in seen:
        seen.add(''.join(input))
        old_input = deepcopy(input)
        for i,c in enumerate(old_input):
            adjacent_list = list(itemgetter(*adjacent_ids[i])(old_input))
            num_bugs_adjacent = sum([1 for i in adjacent_list if i == '#'])
            if  old_input[i] == '#' and not num_bugs_adjacent == 1:
                input[i] = '.'
            elif old_input[i] == '.' and (num_bugs_adjacent == 1 or num_bugs_adjacent == 2):
                input[i] = '#'
    # Get bioderversity
    return sum([2**i for i in range(25) if input[i] == '#'])
        

if __name__ == "__main__":
    input = ['.###.',
            '##...',
            '...##',
            '.#.#.',
            '#.#.#']
    # input = ['....##..#.#..##..#..#....']
    print('Day 24, Part 1: {}'.format(part1(input)))