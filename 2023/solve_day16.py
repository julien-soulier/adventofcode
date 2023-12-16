#!/bin/env python3

import re

def add_tuple(tupx, tupy):
    return tuple([(x+y) for x,y in zip(tupx, tupy)])

TURN_SLASH = {
    (0,1): (-1,0),
    (0,-1): (1,0),
    (1,0): (0,-1),
    (-1,0): (0, 1),
}

TURN_ANTI_SLASH = {
    (0,1): (1,0),
    (0,-1): (-1,0),
    (1,0): (0,1),
    (-1,0): (0,-1),
}
def get_contraption(fname):
    contraption = {}
    with open(fname, "r") as f:
        for y, l in enumerate(f):
            for x, c in enumerate(l.strip()):
                contraption[(x,y)] = {'tiles': c, 'beams': []}

    return contraption

def get_energy(C, start_position, start_direction):
    beams = []
    beams.append({'position': start_position, 'direction': start_direction})
    while len(beams)>0:
        beam = beams.pop()
        pos = beam['position']
        direction = beam['direction']
        while True:
            #print(f"Now at {pos} with direction {direction}")
            if not pos in C.keys():
                #print(f"Out of bounds: {pos}")
                break

            if direction in C[pos]['beams']:
                #print(f"Duplicate beam: {pos}, {direction}")
                break

            C[pos]['beams'].append(direction)

            if (C[pos]['tiles'] == '-' and direction[0] == 0) or (C[pos]['tiles'] == '|' and direction[1] == 0):
                #print(f"Split beam at {pos} direction {direction} becomes {TURN_SLASH[direction]} and {TURN_ANTI_SLASH[direction]}")
                new_pos = add_tuple(pos, TURN_SLASH[direction])
                if new_pos in C:
                    beams.append({'position': new_pos, 'direction': TURN_SLASH[direction]})

                new_pos = add_tuple(pos, TURN_ANTI_SLASH[direction])
                if new_pos in C:
                    beams.append({'position': new_pos, 'direction': TURN_ANTI_SLASH[direction]})
                break

            if C[pos]['tiles'] == '/':
                #print(f"Turn left at {pos} direction {direction} becomes {TURN_SLASH[direction]}")
                direction = TURN_SLASH[direction]

            if C[pos]['tiles'] == '\\':
                #print(f"Turn right at {pos} direction {direction} becomes {TURN_ANTI_SLASH[direction]}")
                direction = TURN_ANTI_SLASH[direction]

            pos = add_tuple(pos, direction)

    energy = sum(1 for tile in C.values() if len(tile['beams']) > 0)

    # clear beams
    for tile in C.values():
        tile['beams'] = []

    return energy

def process_input_part1(fname):
    C = get_contraption(fname)
    return get_energy(C, (0,0), (1,0))

def process_input_part2(fname):
    C = get_contraption(fname)
    width = max(x for x,y in C.keys())+1
    height = max(y for x,y in C.keys())+1
    print(f"Width is {width}, height is {height}")
    for x in range(width):
        yield get_energy(C, (x,0), (0,1))
        yield get_energy(C, (x,height-1), (0,-1))

    for y in range(height):
        yield get_energy(C, (0,y), (1,0))
        yield get_energy(C, (width-1,y), (-1,0))

    return 0

print(f"The solution for part1 is {process_input_part1(fname='input_16.txt')}")
print(f"The solution for part2 is {max(process_input_part2(fname='input_16.txt'))}")
