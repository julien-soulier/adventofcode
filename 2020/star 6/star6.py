import re
import string

def count_answers_part1(s, group_len):
    return len(list(dict.fromkeys(list(s))))

def count_answers_part2(s, group_len):
    res = 0
    for c in list(string.ascii_lowercase):
        if s.count(c) == group_len:
            res += 1
    return res

f = open("input.txt", "r")

# reasd lines and add one extra line to process last group in loop
lines = f.readlines()
lines.append("\n")

total = 0
group_idx = 0
group_len = 0
s=""

for l in lines:
    l = l.rstrip('\n')

    if len(l)==0:
        group_idx += 1
        c = count_answers_part2(s, group_len)
        print("new group {} of length {}: answers {} - {}".format(group_idx, group_len, s, c))
        total += c
        s=""
        group_len = 0
    else:
        s +=  l
        group_len += 1

print(total)
f.close()
