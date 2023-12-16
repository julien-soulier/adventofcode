#!/bin/env python3

import re

def add_tuple(tupx, tupy):
    return tuple([(x+y) for x,y in zip(tupx, tupy)])

def get_platform(fname):
    platform = {}
    platform['cubes'] = set()
    platform['rounds'] = set()
    with open(fname, "r") as f:
        for y, l in enumerate(f):
            for x, c in enumerate(l):
                if c == '#':
                    platform['cubes'].add((x, y))
                elif c == 'O':
                    platform['rounds'].add((x, y))
        platform['height'] = y+1
        platform['width'] = x
    return platform

def display_platform(P):
    for y in range(P['height']):
        for x in range(P['width']):
            if (x,y) in P['cubes']:
                print('#', end='')
            elif (x,y) in P['rounds']:
                print('O', end='')
            else:
                print('.', end='')
        print()

def valid_position(P, position):
    if position[0] < 0 or position[1] < 0:
        return False
    
    if position[0] >= P['width'] or position[1] >= P['height']:
        return False
    
    return True

def count_space(P, position, direction):
    cnt = (0,0)
    pos = position
    while True:
        pos = add_tuple(pos, direction)
        if not valid_position(P, pos) or pos in P['cubes']:
            break
        if pos in P['rounds']:
            continue
        cnt = add_tuple(cnt, direction)
    
    return cnt

def get_weight(platform):
    return sum(platform['height']-p[1] for p in platform['rounds'])

def tilt_platform(platform, direction):
    new_rounds = set()
    for pos in platform['rounds']:
        new_rounds.add(add_tuple(pos, count_space(platform, pos, direction)))
    platform['rounds'] = new_rounds

def do_cyle(platform):
    for direction in [(0,-1), (-1,0), (0,1), (1,0)]:
        #display_platform(platform)
        tilt_platform(platform, direction)
        #print("---")

def process_input_part1(fname):
    P = get_platform(fname)
    tilt_platform(P, (0,-1))
    return get_weight(P)

def process_input_part2(fname):
    P = get_platform(fname)
    history = []
    history.append(P.copy())
    while True:
        do_cyle(P)
        if P in history:
            loop_start = history.index(P)
            loop_length = len(history) - loop_start
            break
        history.append(P.copy())
        print(get_weight(P))

    print(f"Found {loop_length} loop starting at {loop_start}")
    index = (1000000000 - loop_start) % loop_length + loop_start
    return get_weight(history[index])


print(f"The solution for part1 is {process_input_part1(fname='input_14.txt')}")
print(f"The solution for part2 is {process_input_part2(fname='input_14.txt')}")
    