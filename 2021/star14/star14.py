import re
from collections import Counter

f = open("input.txt", "r")
lines = f.read().split('\n')
f.close()

polymere = lines.pop(0)

def part1():
    tranform = {}
    for line in lines:
        m = re.match(r'^(\w\w) -> (\w)$', line)
        if m:
            k = m.group(1)
            tranform[k] = k[0] + m.group(2)

    poly = polymere
    for step in range(10):
        pairs = re.findall(r'(?=(\w\w))', poly)
        pairs = list(map(lambda x: tranform[x], pairs))
        pairs.append(poly[-1])
        poly = ''.join(pairs)

    counts = Counter(poly)
    return max(counts.values()) - min(counts.values())
    
def part2():
    tranform = {}
    for line in lines:
        m = re.match(r'^(\w\w) -> (\w)$', line)
        if m:
            k = m.group(1)
            tranform[k] = [k[0] + m.group(2), m.group(2) + k[1]]

    poly_out = {}
    for p in re.findall(r'(?=(\w\w))', polymere):
        poly_out.setdefault(p, 0)
        poly_out[p] += 1

    for step in range(40):
        poly_in = poly_out
        poly_out = {}
        for k,v in poly_in.items():
            for i in range(2):
                p = tranform[k][i]
                poly_out.setdefault(p, 0)
                poly_out[p] += v
            
    counts = {}
    for k,v in poly_out.items():
        for i in range(2):
            c = k[i]
            counts.setdefault(c,0)
            counts[c] += v

    # each element is counted twice because they are grouped in overlapping pairs
    for k,v in counts.items():
        counts[k] = counts[k] // 2
    
    # except the first one and last one which are present only once. Need Compensate
    counts[polymere[0]] += 1
    counts[polymere[-1]] += 1

    return max(counts.values()) - min(counts.values()) 

print("Solution part1 is {}".format(part1()))
print("Solution part2 is {}".format(part2()))
