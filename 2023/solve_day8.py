#!/bin/env python3

import re
from collections import Counter
import math

def get_moves(fname):
    with open(fname, "r") as f:
        instructions =  f.readline().strip()

    while True:
        for i in instructions:
            yield i

def get_move_cnt(fname):
    with open(fname, "r") as f:
        return len(f.readline().strip())

def read_nodes(fname):
    nodes = {}
    with open(fname, "r") as f:
        for i, l in enumerate(f):
            if i < 2:
                continue
            m = re.match(r'(\w{3}) = \((\w{3}), (\w{3})\)', l.strip())
            if not m:
                raise RuntimeError(f"Bad line {l}")

            nodes[m.group(1)] = {}
            nodes[m.group(1)]['L'] = m.group(2)
            nodes[m.group(1)]['R'] = m.group(3)
    
    return nodes                        

def process_input_part1(fname):

    nodes = read_nodes(fname)
    name = 'AAA'

    for cnt, mov in enumerate(get_moves(fname), start=1):
        name = nodes[name][mov]
        if name == 'ZZZ':
            return cnt
        
def get_node_period(fname, nodes, n):
    path = {}
    move_cnt = get_move_cnt(fname)
    for cnt, mov in enumerate(get_moves(fname), start=1):
        n = nodes[n][mov]
        if n[2]=='Z':
            print(f"Found node {n} after {cnt} moves")
        elt = (n, cnt % move_cnt)
        if elt in path.keys():
            loop_cnt = cnt - path[elt]
            print(f"Find a {loop_cnt} loop for {n} after {cnt} moves")
            break
        path[elt] = cnt

    return loop_cnt

def process_input_part2(fname):

    nodes = read_nodes(fname)
    curt_nodes = [k for k in nodes.keys() if k[2]=='A']    

    return math.lcm(*[get_node_period(fname, nodes, n) for n in curt_nodes])

print(f"The answer for part1 is {process_input_part1(fname='input_8.txt')}")
print(f"The answer for part2 is {process_input_part2(fname='input_8.txt')}")
    