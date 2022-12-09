#/bin/env python3

from parse import *

def sign(v):
    return 1 if v>0 else -1 if v<0 else 0

def update_knot(Hx, Hy, Tx, Ty):
    dx = Hx - Tx
    dy = Hy - Ty
    
    if abs(dx)<2 and abs(dy)<2:
        return Tx, Ty

    return Tx + sign(dx), Ty + sign(dy)

MVT = {'U': (0,1), 'D': (0,-1), 'R': (1,0), 'L': (-1,0)}

def simulate(knots=2):
    visited = {(0,0)}
    Kx = [0] * knots
    Ky = [0] * knots
    with open("input.txt", "r") as f:
        for line in f.readlines():
            r = parse("{cmd} {count:d}", line.strip())
            if not r:
                continue
            
            for _ in range(r['count']):
                Kx[0] += MVT[r['cmd']][0]
                Ky[0] += MVT[r['cmd']][1]
                
                for k in range(1,knots):
                    Kx[k], Ky[k] = update_knot(Kx[k-1], Ky[k-1], Kx[k], Ky[k])
                
                visited.add((Kx[-1], Ky[-1]))
    return visited

print(f"Soution part1 is {len(simulate())}")
print(f"Soution part2 is {len(simulate(10))}")
