#!/bin/env python3

import re

def get_seeds(fname):
    with open(fname, "r") as f:
        values = [int(x) for x in re.findall(r'\d+', f.readline())]
        for x in values:
            yield x
        
def get_seed_ranges(fname):
    with open(fname, "r") as f:
        values = [int(x) for x in re.findall(r'\d+', f.readline())]
        it = iter(values)
        for x in it:
            length = next(it)
            seed_range = {}
            seed_range['start'] = x
            seed_range['end'] = x + length - 1
            yield seed_range

def get_map_blocks(fname):
    with open(fname, "r") as f:
        block = []
        for l in f.readlines()[2:]:
            l = l.strip()
            if len(l) == 0:
                yield block
                block = []
            else:
                block.append(l)
        yield block

def get_transformers(fname):
    for block in get_map_blocks(fname):
        transform = {}
        m = re.match(r'(\w+)-to-(\w+)', block[0])
        if not m:
            raise RuntimeError(f"Bad block {block[0]}")
        transform['src'] = m.group(1)
        transform['dest'] = m.group(2)
        transform['mapping'] =  []
        for l in block[1:]:
            transform['mapping'].append([int(x) for x in re.findall(r'\d+', l)])
        yield transform

def apply_transform(x, transform):
    y = x
    for m in transform['mapping']:
        if m[1] <= x < m[1]+m[2]:
            y = m[0] + (x - m[1])
            break
    return y

def process_input_part1(fname="input_5.txt"):
    transforms={}
    for t in get_transformers(fname):
        transforms[t['src']] = t

    for s in get_seeds(fname):
        src='seed'
        while src != 'location':
            t = transforms[src]
            s = apply_transform(s, t)
            src = t['dest']

        yield s

class Region:
    def __init__(self):
        self.unmapped=[]
        self.mapped = []

    def add_unmapped(self, start, end):
        x = {}
        x['start'] = start
        x['end'] = end
        self.unmapped.append(x)

    def apply_transform(self, transform):
        for mapping in transform['mapping']:
            unmapped = []
            for r_in in self.unmapped:

                #print(f"Transforming {r_in} with {mapping}")

                # left side
                if r_in['start'] < mapping[1]:
                    new_range = {}
                    new_range['start'] = r_in['start']
                    new_range['end'] = min(mapping[1], r_in['end'])
                    unmapped.append(new_range)

                # middle side
                start = max(r_in['start'], mapping[1])
                end = min(r_in['end'], mapping[1] + mapping[2] - 1)
                if end > start:
                    new_range = {}
                    new_range['start'] = mapping[0] + start - mapping[1]
                    new_range['end'] = mapping[0] + end - mapping[1]
                    self.mapped.append(new_range)

                # right side
                if r_in['end'] > mapping[1] + mapping[2]:
                    new_range = {}
                    new_range['start'] = max(mapping[1] + mapping[2], r_in['start'])
                    new_range['end'] = r_in['end']
                    unmapped.append(new_range)

            self.unmapped = unmapped
        self.unmapped.extend(self.mapped)
        self.mapped = []

    def min_value(self):
        return min([x['start'] for x in self.unmapped])

def process_input_part2(fname="input_5.txt"):
    transforms={}
    for t in get_transformers(fname):
        transforms[t['src']] = t

    region = Region()
    for seed_range in get_seed_ranges(fname):
        region.add_unmapped(seed_range['start'], seed_range['end'])

    src='seed'
    while src != 'location':
        t = transforms[src]
        region.apply_transform(t)
        src = t['dest']

    return region.min_value()

print(f"The solution for part1 is {min(process_input_part1())}")
print(f"The solution for part2 is {process_input_part2()}")
    