#!/bin/env python3

import re

def get_map_width(fname):
    with open(fname, "r") as f:
        width = len(f.readline().strip())
    return width

def get_lines(fname):
    width = get_map_width(fname)
    yield '.' * (width+2)

    with open(fname, "r") as f:
        for l in f:
            yield '.'+l.strip()+'.'
    
    yield '.' * (width+2)

def is_symbol(c):
    return False if c.isdigit() else False if c == '.' else True

def is_part_number(slice, start, end):
    for l in [0,2]:
        for i in range(start-1, end+1):
            if is_symbol(slice[l][i]):
                return True
        
    if is_symbol(slice[1][start-1]) or is_symbol(slice[1][end]):
            return True
    
    return False

def process_input_part1(fname="input_3.txt"):
    slice = []
    for line in get_lines(fname):
        slice.append(line)
        if len(slice)<3:
            continue

        for m in re.finditer(r'\d+', slice[1]):
            if is_part_number(slice, m.start(0), m.end(0)):
                #print(f"Found part number {m.group(0)}")
                yield int(m.group(0))

        slice.pop(0)

def get_number_left(line, pos):
    n = 0
    base = 1
    for i in range(pos, 0, -1):
        if line[i].isdigit():
            n += int(line[i]) * base
            base *= 10
        else:
            break
    return n

def get_number_right(line, pos, n_left=0):
    n = n_left
    for i in range(pos, len(line)):
        if line[i].isdigit():
            n = n*10 + int(line[i])
        else:
            break
    return n

def get_number_center(line, pos):
    n_left = get_number_left(line, pos-1)
    n = get_number_right(line, pos, n_left)
    return n

def get_numbers_around(slice, pos):
    numbers = []
    for l in [0,2]:
        if slice[l][pos].isdigit():
            numbers.append(get_number_center(slice[l], pos))
        else:
            n = get_number_left(slice[l], pos-1)
            if n>0:
                numbers.append(n)
            n = get_number_right(slice[l], pos+1)
            if n>0:
                numbers.append(n)

    if slice[1][pos-1].isdigit():
        numbers.append(get_number_left(slice[1], pos-1))
    if slice[1][pos+1].isdigit():
        numbers.append(get_number_right(slice[1], pos+1))

    return numbers

def process_input_part2(fname="input_3.txt"):
    slice = []
    line_idx = 0
    for line in get_lines(fname):
        line_idx += 1
        slice.append(line)
        if len(slice)<3:
            continue

        for m in re.finditer(r'\*', slice[1]):
            numbers = get_numbers_around(slice, m.start(0))
            if len(numbers) == 2:
                yield numbers[0]*numbers[1]

        slice.pop(0)

print(f"The answer for part1 is {sum(process_input_part1(fname='input_3.txt'))}")
print(f"The answer for part2 is {sum(process_input_part2(fname='input_3.txt'))}")
    