#/bin/env python3

from parse import *

def tuple_sign(a):
    return tuple(1 if v>0 else -1 if v<0 else 0 for v in a)

def tuple_add(a, b):
    return tuple(i + j for i, j in zip(a,b))

def tuple_neg(a):
    return tuple(-i for i in a)

def update_knot(H, T):
    D = tuple_add(H, tuple_neg(T))
    
    if all(abs(i)<2 for i in D):
        return T

    return tuple_add(T, tuple_sign(D))

MVT = {'U': (0,1), 'D': (0,-1), 'R': (1,0), 'L': (-1,0)}

def simulate(knots=2):
    visited = {(0,0)}
    K = [(0,0)] * knots
    with open("input.txt", "r") as f:
        for line in f.readlines():
            r = parse("{cmd} {count:d}", line.strip())
            if not r:
                continue
            
            for _ in range(r['count']):
                K[0] = tuple_add(K[0], MVT[r['cmd']])
                
                for k in range(1,knots):
                    K[k] = update_knot(K[k-1], K[k])
                
                visited.add(K[-1])
    return len(visited)

print(f"Soution part1 is {simulate(2)}")
print(f"Soution part2 is {simulate(10)}")
