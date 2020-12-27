import re
import string

f = open("input.txt", "r")
lines = f.readlines()
f.close()

algo = 0

def add_or_mul(match):
    if match.group(2)=='+':
        return str(int(match.group(1)) + int(match.group(3)))
    else:
        return str(int(match.group(1)) * int(match.group(3)))

def add(match):
    return str(int(match.group(1)) + int(match.group(2)))

def mul(match):
    return str(int(match.group(1)) * int(match.group(2)))

def remove_parenthesis(match):
    return match.group(1)

def compute(section):
    sec1 = section
    section = ''
    while sec1 != section:
        section = sec1
        if algo==1:
            sec1 = re.sub(r'(\d+)([+*])(\d+)', add_or_mul, section, count=1)
        else:
            sec1 = re.sub(r'(\d+)\+(\d+)', add, section, count=1)
            if sec1 == section:
                sec1 = re.sub(r'(\d+)\*(\d+)', mul, section, count=1)

    return section

def process_single_parenthesis(match):
    return compute(match.group(1))

def compute_lines():
    total = 0
    for line in lines:
        line1 = line.strip('\n')
        line1 = line1.replace(' ','')
        while line1 != line:
            line = line1
            line1 = re.sub(r'\(([0-9+*]+)\)', process_single_parenthesis, line, count=1)
            if line1 == line:
                line1 = compute(line)
                break

        total += int(line1)
    return total

algo=1
res1 = compute_lines()
print("solution 1 is {}".format(res1))

algo=2
res2 = compute_lines()
print("solution 2 is {}".format(res2))
