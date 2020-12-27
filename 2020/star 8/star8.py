import re
import string

p = re.compile('^(nop|acc|jmp)\s+([+-])(\d+)\s*$')
f = open("input.txt", "r")

# reasd lines and add one extra line to process last group in loop
lines = f.readlines()
max_len = len(lines)

mod = {}
for l in range(max_len):
    mod[l] = False

def compute_acc(do_change):
    idx = 0
    acc = 0
    hit = {}
    for l in range(max_len):
        hit[l] = False

    while idx < max_len and not hit[idx]:
        hit[idx] = True
        m = p.match(lines[idx])
        if m:
            inst = m.group(1)
            sign = m.group(2)
            offset = int(m.group(3))
            if sign == '-':
                offset = -offset

            if inst == 'jmp':
                if do_change and not mod[idx]:
                    print("convert jmp to nop @{}".format(idx))
                    mod[idx] = True
                    do_change = False
                    idx += 1
                else:
                    idx += offset
            elif inst == 'acc':
                acc += offset
                idx += 1
            elif inst == 'nop':
                if do_change and not mod[idx]:
                    print("convert nop to jmp @{}".format(idx))
                    mod[idx] = True
                    do_change = False
                    idx += offset
                else:
                    idx += 1
            else:
                print('invalid instruction {}'.format(inst))
        else:
            print('invalid line {} at {}'.format(lines[idx], idx))

    if idx == max_len:
        return True, acc
    else:
        return False, acc

res, acc = compute_acc(False)
print("Part1 {}".format(acc))

res, acc = compute_acc(True)
while not res:
    res, acc = compute_acc(True)

print("Part2 {}".format(acc))


f.close()
