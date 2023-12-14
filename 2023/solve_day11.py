#!/bin/env python3

import re

def add_tuple(tupx, tupy):
    return tuple([(x+y) for x,y in zip(tupx, tupy)])

def read_galaxies(fname):
    with open(fname, "r") as f:
        for y,l in enumerate(f):
            for x,c in enumerate(l):
                if c == '#':
                    yield (x,y)

def expend_galaxies(G, empty_cols, empty_rows, scale=2):
    for g in G:
        x = g[0] + sum(scale-1 for e in empty_cols if e < g[0]) 
        y = g[1] + sum(scale-1 for e in empty_rows if e < g[1])
        yield (x,y)

def process_input(fname, part):
    G = list(read_galaxies(fname))
    
    width = max(g[0] for g in G)+1
    height = max(g[1] for g in G)+1

    empty_cols = set(range(width)) - set([g[0] for g in G])
    empty_rows = set(range(height)) - set([g[1] for g in G])

    print(f"Width: {width}, height: {height}")
    print(f"Empty columns: {empty_cols}")
    print(f"Empty rows: {empty_rows}")

    GE = list(expend_galaxies(G, empty_cols, empty_rows, scale=2 if part==1 else 1000000))
    for i, g in enumerate(GE):
        for h in GE[i:]:
            yield abs(g[0]-h[0]) + abs(g[1]-h[1])

print(f"The solution for part1 is {sum(process_input(fname='input_11.txt', part=1))}")
print(f"The solution for part2 is {sum(process_input(fname='input_11.txt', part=2))}")
    