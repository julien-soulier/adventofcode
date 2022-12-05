#/bin/env python3

from parse import *
import copy

# GET it by observing input file
STACK_COUNT = 9

STACK = [[] for _ in range(STACK_COUNT)]

with open("input.txt", "r") as f:
    L = f.readlines()

i = 0
while L[i] != "\n":
    pos = [j for j, c in enumerate(L[i]) if c=='[']

    for k in pos:
        STACK[k//4].insert(0,L[i][k+1])

    i += 1

def move_crates(mode):
    S = copy.deepcopy(STACK)

    for line in L[i+1:]:
        r = parse("move {count:d} from {orig:d} to {dest:d}\n", line)

        p = []
        for _ in range(r['count']):
            s = S[r['orig']-1].pop()
            p.append(s)
        
        if mode == 2:
            p.reverse()

        S[r['dest']-1].extend(p)

    return ''.join([s[-1] for s in S])

print(f"Soution part1 is {move_crates(1)}")
print(f"Soution part2 is {move_crates(2)}")



