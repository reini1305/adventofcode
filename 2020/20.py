from collections import deque
import pytest
from typing import Deque, Dict, List, Tuple
from aoc import day, get_input
from functools import reduce
from operator import mul
import numpy as np
import math

def parse_tiles(input: List[str]):
    tiles = {}
    id = 0
    for line in input:
        if line.startswith('Tile'):
            id = int(line.split(' ')[1][:-1])
            tiles[id]={'borders':[], 'all':[]}
        else:
            if line != '':
                tiles[id]['all'].append(line)
    # pre-calculate borders
    for tile in tiles: # up, right, down, left
        tiles[tile]['borders'].append(tiles[tile]['all'][0])
        tiles[tile]['borders'].append(''.join([tiles[tile]['all'][i][-1] for i in range(len(tiles[tile]['all']))]))
        tiles[tile]['borders'].append(tiles[tile]['all'][-1][::-1])
        tiles[tile]['borders'].append(''.join([tiles[tile]['all'][len(tiles[tile]['all'])-1-i][0] for i in range(len(tiles[tile]['all']))]))
    return tiles

def match_border_to_tile(border:str, tile:Dict)->bool:
    return border in tile['borders'] or border[::-1] in tile['borders']

def find_corner_pieces(tiles:Dict)->List[int]:
    corner_ids = []
    for tile in tiles:
        sum_matched = 0
        for border in tiles[tile]['borders']:
            if any([match_border_to_tile(border, tiles[t]) for t in tiles if t != tile]):
                sum_matched+=1
        if sum_matched == 2:
            corner_ids.append(tile)
    return corner_ids

def part1(input: List[str])-> None:
    tiles = parse_tiles(input)
    result = reduce(mul,find_corner_pieces(tiles))
    print(f'Day {day()}, Part 1: {result}')

def render_tile(tile, coordinate, image):
    tile_size = len(tile['all'][0]) - 2
    tile_img = np.zeros((tile_size,tile_size))
    for row,line in enumerate(tile['all'][1:-1]):
        for col,c in enumerate(line[1:-1]):
            if c == '#':
                tile_img[row][col] = 1
    # properly rotate and flip
    tile_img = np.rot90(tile_img, tile['rot']//90)
    if tile['fliplr']:
        tile_img = np.fliplr(tile_img)
    if tile['flipud']:
        tile_img = np.flipud(tile_img)
    try:
        image[coordinate[0]*tile_size:(coordinate[0]+1)*tile_size,
            coordinate[1]*tile_size:(coordinate[1]+1)*tile_size] = tile_img
    except:
        print(f'Could not render {coordinate}')

def get_matching_border(border:str, tile:Dict)->Tuple[int,bool]:
    if border in tile['borders']:
        return (tile['borders'].index(border),False)
    if border[::-1] in tile['borders']:
        return (tile['borders'].index(border[::-1]),True)
    return (-1,False)

def assemble_tiles(tiles):
    orientations = ['U','R','D','L']
    corners = find_corner_pieces(tiles)
    img_size = int(math.sqrt(len(tiles)) * (len(tiles[next(iter(tiles))]['all'])-2))
    img = np.zeros((img_size,img_size))
    active_tiles = deque()
    # take corner piece, rotate such that it is in upper left corner
    active_tile = corners[0]
    tiles[active_tile]['rot']=0
    tiles[active_tile]['fliplr']=False
    tiles[active_tile]['flipud']=False
    matching_borders = [any([match_border_to_tile(border, tiles[t]) for t in tiles if t != active_tile]) for border in tiles[active_tile]['borders']]
    while matching_borders != [False,True,True,False]:
        matching_borders = [*matching_borders[1:],matching_borders[0]]
        tiles[active_tile]['borders'] = [*tiles[active_tile]['borders'][1:],tiles[active_tile]['borders'][0]]
        tiles[active_tile]['rot']+=90
    coordinate = (0,0)
    active_tiles.append((corners[0],coordinate))
    while active_tiles:
        active_tile, coordinate = active_tiles.popleft()
        render_tile(tiles[active_tile], coordinate, img)
        # match right border
        border = tiles[active_tile]['borders'][orientations.index('R')]
        try:
            right_tile = [t for t in tiles if t != active_tile and match_border_to_tile(border,tiles[t])][0]
            if (right_tile,(coordinate[0],coordinate[1]+1)) not in active_tiles:
                tiles[right_tile]['rot']=0
                tiles[right_tile]['fliplr']=False
                tiles[right_tile]['flipud']=False
                # make sure it matches the left border of that tile
                match_id, flipped = get_matching_border(border,tiles[right_tile])
                while match_id != orientations.index('L'):
                    tiles[right_tile]['borders'] = [*tiles[right_tile]['borders'][1:],tiles[right_tile]['borders'][0]]
                    tiles[right_tile]['rot']+=90
                    match_id, flipped = get_matching_border(border,tiles[right_tile])
                if not flipped: # if match wasn't flipped we need to flipud
                    tiles[right_tile]['flipud'] = True
                    b0 = tiles[right_tile]['borders'][orientations.index('U')]
                    tiles[right_tile]['borders'][orientations.index('U')] = tiles[right_tile]['borders'][orientations.index('D')][::-1]
                    tiles[right_tile]['borders'][orientations.index('D')] = b0[::-1]
                    tiles[right_tile]['borders'][orientations.index('L')] = tiles[right_tile]['borders'][orientations.index('L')][::-1]
                    tiles[right_tile]['borders'][orientations.index('R')] = tiles[right_tile]['borders'][orientations.index('R')][::-1]
                active_tiles.append((right_tile,(coordinate[0],coordinate[1]+1)))
        except:
            pass
        # match down border
        border = tiles[active_tile]['borders'][orientations.index('D')]
        try:
            down_tile = [t for t in tiles if t != active_tile and match_border_to_tile(border,tiles[t])][0]
            if (down_tile,(coordinate[0]+1,coordinate[1])) in active_tiles:
                continue
            tiles[down_tile]['rot']=0
            tiles[down_tile]['fliplr']=False
            tiles[down_tile]['flipud']=False
            # make sure it matches the up border of that tile
            match_id, flipped = get_matching_border(border,tiles[down_tile])
            while match_id != orientations.index('U'):
                tiles[down_tile]['borders'] = [*tiles[down_tile]['borders'][1:],tiles[down_tile]['borders'][0]]
                tiles[down_tile]['rot']+=90
                match_id, flipped = get_matching_border(border,tiles[down_tile])
            if not flipped: # if match wasn't flipped we need to fliplr
                tiles[down_tile]['fliplr'] = True
                b0 = tiles[down_tile]['borders'][orientations.index('L')]
                tiles[down_tile]['borders'][orientations.index('L')] = tiles[down_tile]['borders'][orientations.index('R')][::-1]
                tiles[down_tile]['borders'][orientations.index('R')] = b0[::-1]
                tiles[down_tile]['borders'][orientations.index('U')] = tiles[down_tile]['borders'][orientations.index('U')][::-1]
                tiles[down_tile]['borders'][orientations.index('D')] = tiles[down_tile]['borders'][orientations.index('D')][::-1]
            active_tiles.append((down_tile,(coordinate[0]+1,coordinate[1])))
        except:
            pass
    return img

def match_template(img):
    template = ['                  # ',
                '#    ##    ##    ###',
                ' #  #  #  #  #  #   ']
    t = np.zeros((len(template),len(template[0])))
    for row,line in enumerate(template):
        for col,c in enumerate(line):
            if c == '#':
                t[row][col] = 1
    # flipping and rotating the template is easier
    sum_template = np.sum(t)
    for rot in range(1,5):
        for fliplr in [False,True]:
            for flipud in [True,False]:
                if np.sum(img>1)>sum_template:
                    return img
                tr = np.rot90(t,rot)
                if fliplr:
                    tr = np.fliplr(tr)
                if flipud:
                    tr = np.flipud(tr)
                # sliding window matching
                for starty in range(img.shape[0]-tr.shape[0]):
                    for startx in range(img.shape[1]-tr.shape[1]):
                        sum_matching = 0
                        for x in range(tr.shape[1]):
                            for y in range(tr.shape[0]):
                                if tr[y][x] == 1:
                                    if img[starty+y][startx+x] >= 1:
                                        sum_matching += 1
                        if sum_matching == sum_template:
                            for y in range(tr.shape[0]):
                                for x in range(tr.shape[1]):
                                    if tr[y][x] == 1:
                                        img[starty+y][startx+x] += 1 
    return img

def part2(input: List[str])-> None:
    tiles = parse_tiles(input)
    result = assemble_tiles(tiles)
    img = match_template(result)
    print(f'Day {day()}, Part 2: {np.sum(img==1)}')

if __name__ == "__main__":
    input = get_input(f'input{day()}.txt')
    part1(input)
    part2(input)
