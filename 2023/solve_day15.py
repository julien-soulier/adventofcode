#!/bin/env python3

import re

def get_steps(fname):
    with open(fname, "r") as f:
        steps = f.readline().strip().split(',')

    for s in steps:
        yield s 

def hash(str):
    val = 0
    for c in str:
        val += ord(c)
        val *= 17
        val %= 256
    return val

def process_input_part1(fname):
    for step in get_steps(fname):
        yield hash(step)


def process_input_part2(fname):
    boxes = {}
    for box in range(256):
        boxes[box] = []

    for step in get_steps(fname):
        m0 = re.fullmatch(r'(\w+)=(\d+)', step)
        m1 = re.fullmatch(r'(\w+)-', step)
        if m0:
            label = m0.group(1)
            focal = int(m0.group(2))
        elif m1:
            label = m1.group(1)
            focal = 0
        else:
            raise RuntimeError(f"Bad step: {step}")
        
        box = hash(label)
        try:
            idx = [x['label'] for x in boxes[box]].index(label)
        except:
            idx = -1

        if focal == 0:
            if idx >=0:
                boxes[box].pop(idx)
        else:
            if idx >=0:
                boxes[box][idx]['focal'] = focal
            else:
                boxes[box].append({'label': label, 'focal': focal})

    for box in range(256):
        for i, lense in enumerate(boxes[box], start=1):
            yield (box+1) * i * lense['focal']

print(f"The solution for part1 is {sum(process_input_part1(fname='input_15.txt'))}")
print(f"The solution for part2 is {sum(process_input_part2(fname='input_15.txt'))}")
    