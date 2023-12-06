#!/bin/env python3

import re,math

def get_races(fname):
    with open(fname, "r") as f:
        times = re.findall(r'\d+', f.readline())
        distances = re.findall(r'\d+', f.readline())

    for t,d in zip(times, distances):
        race = {}
        race['time'] = int(t)
        race['distance'] = int(d)
        yield race

# we solve the equation x*(T-x)-d = 0 <=> -(x^2) + T.x - d = 0
def solve_race(race):
    t = race['time']
    d = race['distance']
    delta = t**2 - 4*d
    if delta < 0:
        raise RuntimeError(f"Invalid equation {race} -> delta = {delta}")

    x1 = (t-delta**0.5) / 2
    x1 = int(x1+1) if x1.is_integer() else math.ceil(x1)
    x2 = (t+delta**0.5) / 2
    x2 = int(x2-1) if x2.is_integer() else math.floor(x2)
    print(f"{race} -> x1 = {x1}, x2 = {x2}")
    return x2-x1+1

def process_input_part1(fname="input_6.txt"):
    for r in get_races(fname):
        c = solve_race(r)
        print(c)
        yield c

def get_single_race(fname):
    with open(fname, "r") as f:
        race = {}
        race['time'] = int(f.readline().replace(" ", "").split(':')[1])
        race['distance'] = int(f.readline().replace(" ", "").split(':')[1])
        return race

def process_input_part2(fname="input_6.txt"):
    race = get_single_race(fname)
    return solve_race(race)

print(f"The answer for part1 is {math.prod(process_input_part1(fname='input_6.txt'))}")
print(f"The answer for part2 is {process_input_part2(fname='input_6.txt')}")
    