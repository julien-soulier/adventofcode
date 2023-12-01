#!/bin/env python3

import re

PATTERN1 = r'\d'
PATTERN2 = r'(one|two|three|four|five|six|seven|eight|nine|\d)'
CONV = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def get_calibration_re(line, pattern=r'\d'):
    digits = re.findall(pattern, line)
    return CONV[digits[0]]*10 + CONV[digits[-1]]

def process_input(fname="input_1.txt", pattern=r'\d'):
    with open(fname, "r") as f:
        for l in f:
            yield get_calibration_re(l.strip(), pattern)

print(f"The total calibration part1 is {sum(process_input(pattern=PATTERN1))}")
print(f"The total calibration part2 is {sum(process_input(pattern=PATTERN2))}")
    