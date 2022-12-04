#/bin/env python3

from parse import *

#### CODING STYLE 1 #####
def overlap(pair):
    r = parse("{:d}-{:d},{:d}-{:d}", pair)
    full = 1 if (r[0]>=r[2] and r[1]<=r[3]) or (r[0]<=r[2] and r[1]>=r[3]) else 0
    part = 1 if (r[0]>=r[2] and r[0]<=r[3]) or (r[1]>=r[2] and r[1]<=r[3]) or (r[2]>=r[0] and r[2]<=r[1]) or (r[3]>=r[0] and r[3]<=r[1]) else 0
    return (full, part)


with open("input.txt", "r") as f:
    res = [overlap(pair) for pair in f.read().splitlines()]
    print(f"Soution part1 is {sum(x[0] for x in res)}")
    print(f"Soution part2 is {sum(x[1] for x in res)}")


#### CODING STYLE 2 #####
print(f"===========================")

def overlap_full(r):
    return 1 if (r[0]>=r[2] and r[1]<=r[3]) or (r[0]<=r[2] and r[1]>=r[3]) else 0

def overlap_part(r):
    return 1 if (r[0]>=r[2] and r[0]<=r[3]) or (r[1]>=r[2] and r[1]<=r[3]) or (r[2]>=r[0] and r[2]<=r[1]) or (r[3]>=r[0] and r[3]<=r[1]) else 0

with open("input.txt", "r") as f:
    sum_f = sum_p = 0    
    for line in f.read().splitlines():
        pair = parse("{:d}-{:d},{:d}-{:d}", line)

        sum_f += overlap_full(pair)
        sum_p += overlap_part(pair)

    print(f"Soution part1 is {sum_f}")
    print(f"Soution part2 is {sum_p}")
    

