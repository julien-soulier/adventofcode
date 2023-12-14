#!/bin/env python3

import re

def get_patterns(fname):
    pattern = []
    with open(fname, "r") as f:
        for l in f:
            if l.strip() == "": 
                yield pattern
                pattern=[]
            else:
                pattern.append(list(l.strip()))
    yield pattern

def get_axis(pattern, forbidden=0):
    axes = list(range(1, len(pattern[0])))
    if forbidden > 0:
        axes.remove(forbidden)
    for l in pattern:
        new_axes = []            
        for a in axes:
            w = min(a, len(l)-a)
            left = l[a-w:a]
            right = l[a:a+w]
            if left[::-1] == right:
                new_axes.append(a)

        axes = new_axes
        if len(axes) == 0:
            break

    if len(axes)==1:
        return axes[0]
    
    return 0

def get_axis_with_smudge(pattern, prev_axis):
    for y in range(len(pattern)):
        for x in range(len(pattern[0])):
            pattern[y][x] = "." if pattern[y][x] == "#" else "#"
            axis = get_axis(pattern, prev_axis)
            pattern[y][x] = "#" if pattern[y][x] == "." else "."

            if axis>0:
                return axis

    return 0

def rotate(pattern):
    p = []
    for x in range(len(pattern[0])):
        l = []
        for y in range(len(pattern)):
            l.append(pattern[y][x])
        p.append(l)

    return p

def process_input_part1(fname):
    for p in get_patterns(fname):
        x_axis = 0
        y_axis = get_axis(p)
        if y_axis == 0:
            p = rotate(p)
            x_axis = get_axis(p)

        yield (x_axis, y_axis)


def process_input_part2(fname, prev_axes):
    for i, p in enumerate(get_patterns(fname)):
        x_axis = 0
        y_axis = get_axis_with_smudge(p, prev_axes[i][1])
        if y_axis == 0:
            p = rotate(p)
            x_axis = get_axis_with_smudge(p, prev_axes[i][0])

        yield (x_axis,y_axis)

axes = [x for x in process_input_part1(fname='input_13.txt')]
print(f"The solution for part1 is {sum([x[0]*100+x[1] for x in axes])}")
print(f"The solution for part2 is {sum([x[0]*100+x[1] for x in process_input_part2(fname='input_13.txt', prev_axes=axes)])}")
