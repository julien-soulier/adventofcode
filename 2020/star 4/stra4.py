import re
import string

def check_valid(ppt, idx, do_match):
    fields = { 
        'byr': '^19[2-9][0-9]|200[0-2]$',
        'iyr': '^201[0-9]|2020$',
        'eyr': '^202[0-9]|2030$', 
        'hgt': '^1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in$', 
        'hcl': '^#[0-9a-f]{6}$',
        'ecl': '^amb|blu|brn|gry|grn|hzl|oth$',
        'pid': '^\d{9}$',
    }

    for k in fields.keys():
        if k in ppt.keys():
            if do_match:
                p = re.compile(fields[k])
                m = p.match(ppt[k])
                if not m:
                    print("invalid field at index {}, {}:{}".format(idx, k, ppt[k]))
                    return False
        else:
            print("missing field {} at index {}".format(k, idx))
            return False

    print("passport {} is valid".format(idx))
    return True

f = open("input.txt", "r")
ppt = {}
total = 0
idx = 0
for l in f.readlines():
    items = l.split()
    for i in items:
        tokens = i.split(':')
        tok=tokens[0]
        val=tokens[1]
        ppt[tok] = val

    if len(l)==1:
        idx += 1
        if check_valid(ppt, idx, True):
            total += 1

        ppt = {}

idx += 1
if check_valid(ppt, idx, True):
    total += 1

print(total)
f.close()
