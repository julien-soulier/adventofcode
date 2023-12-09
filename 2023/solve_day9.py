#!/bin/env python3

import re

def last(vals):
    last = 0
    for v in vals[::-1]:
        last += v[-1]

    return last

def first(vals):
    first = 0
    for v in vals[::-1]:
        first = v[0]-first
    
    return first

def estimation(line, part):
    vals = []
    vals.append([int(x) for x in re.findall('-?\d+', line)])
    while not all(x==0 for x in vals[-1]):
        vals.append([y-x for x,y in zip(vals[-1], vals[-1][1:])])

    return last(vals) if part==1 else first(vals)


def process_input(fname, part):
    with open(fname, "r") as f:
        for l in f:
            yield estimation(l, part)

print(f"The solution for part1 is {sum(process_input(fname='input_9.txt', part=1))}")
print(f"The solution for part2 is {sum(process_input(fname='input_9.txt', part=2))}")
    