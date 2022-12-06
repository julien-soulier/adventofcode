#/bin/env python3

from parse import *
import functools

#### CODING STYLE 1 #####
def overlap(line):
    r = parse("{:d}-{:d},{:d}-{:d}\n", line)
    full = 1 if (r[0]>=r[2] and r[1]<=r[3]) or (r[0]<=r[2] and r[1]>=r[3]) else 0
    part = 1 if (r[0]>=r[2] and r[0]<=r[3]) or (r[1]>=r[2] and r[1]<=r[3]) or (r[2]>=r[0] and r[2]<=r[1]) or (r[3]>=r[0] and r[3]<=r[1]) else 0
    return (full, part)

with open("input.txt", "r") as f:
    res = functools.reduce(lambda x,y: (y[0]+x[0], y[1]+x[1]), (overlap(line) for line in f.readlines()))   
    print(f"Soution part1 is {res[0]}")
    print(f"Soution part2 is {res[1]}")


#### CODING STYLE 2 #####
print(f"===========================")

def overlap_full(r):
    return 1 if (r[0]>=r[2] and r[1]<=r[3]) or (r[0]<=r[2] and r[1]>=r[3]) else 0

def overlap_part(r):
    return 1 if (r[0]>=r[2] and r[0]<=r[3]) or (r[1]>=r[2] and r[1]<=r[3]) or (r[2]>=r[0] and r[2]<=r[1]) or (r[3]>=r[0] and r[3]<=r[1]) else 0

with open("input.txt", "r") as f:
    sum_f = sum_p = 0    
    for line in f.readlines():
        pair = parse("{:d}-{:d},{:d}-{:d}\n", line)

        sum_f += overlap_full(pair)
        sum_p += overlap_part(pair)

    print(f"Soution part1 is {sum_f}")
    print(f"Soution part2 is {sum_p}")


#### Coding style Stephane: Iterator to ensure one unique for loop #####
print(f"===========================")

def read_input_lines():
    with open("input.txt", "r") as f:
        for line in f.readlines():
            yield line.strip()

def parse_input(lines):
    for line in lines:
        yield parse("{:d}-{:d},{:d}-{:d}", line)

def overlap(parsed_lines):
    for parsed_line in parsed_lines:
        r = parsed_line
        full = 1 if (r[0]>=r[2] and r[1]<=r[3]) or (r[0]<=r[2] and r[1]>=r[3]) else 0
        part = 1 if (r[0]>=r[2] and r[0]<=r[3]) or (r[1]>=r[2] and r[1]<=r[3]) or (r[2]>=r[0] and r[2]<=r[1]) or (r[3]>=r[0] and r[3]<=r[1]) else 0

        yield full, part

def consume_and_sum(overlap_lines):
    sum_f = 0
    sum_p = 0
    for overlap_line in overlap_lines:
        sum_f += overlap_line[0]
        sum_p += overlap_line[1]

    return sum_f, sum_p

sum_f, sum_p = consume_and_sum(overlap(parse_input(read_input_lines())))

print(f"Soution part1 is {sum_f}")
print(f"Soution part2 is {sum_p}")
