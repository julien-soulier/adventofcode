#/bin/env python3

def priority(c):
    base = 27 if c.isupper() else 1
    return ord(c) - ord('A' if c.isupper() else 'a') + base

def get_sum(items):
    return sum(priority(x.pop()) for x in items)

with open("input.txt", "r") as f:
    L = f.read().splitlines()
    
    items = [set(l[0:len(l)//2]).intersection(set(l[len(l)//2:])) for l in L]
    print(f"Soution part1 is {get_sum(items)}")

    items = [set(L[i]).intersection(set(L[i+1]), L[i+2]) for i in range(0, len(L), 3)]
    print(f"Soution part2 is {get_sum(items)}")
