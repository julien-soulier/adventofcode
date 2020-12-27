import re
import string

f = open("input.txt", "r")
lines = f.readlines()
f.close()
p = re.compile('^mask = ([10X]+)$')
q = re.compile('^mem\[(\d+)\] = (\d+)$')
mask1 = 2**36 - 1

def part1():
    OR_mask = 0
    AND_mask = mask1
    MEM = {}
    for l in lines:
        m = p.match(l) 
        if m:
            s = m.group(1)
            AND_mask = int(s.replace('X', '1'), 2)
            OR_mask = int(s.replace('X', '0'), 2)
    
        m = q.match(l)
        if m:
            addr = int(m.group(1))
            val = int(m.group(2))
            val = val & AND_mask
            val = val | OR_mask
            MEM[addr] = val

    return sum(MEM.values())

def store_value(MEM, mask, idx, addr, val):
    do_store = True
    for i in range(idx, len(mask)):
        if mask[i] == '0':
            pass
        elif mask[i] == '1':
            addr = addr | 2**(35-i)
        elif mask[i] == 'X':
            addr1 = addr & (mask1 ^ 2**(35-i))
            addr0 = addr | 2**(35-i)
            #print('X@{} {} -> {} {}'.format(i, addr, addr0, addr1))
            store_value(MEM, mask, i+1, addr1, val)
            store_value(MEM, mask, i+1, addr0, val)
            do_store = False

    if do_store:
        #print("store value mem[{}] = {}".format(addr, val))
        MEM[addr] = val


def part2():
    MEM = {}

    for l in lines:
        m = p.match(l) 
        if m:
            mask = m.group(1)
    
        m = q.match(l)
        if m:
            addr = int(m.group(1))
            val = int(m.group(2))
            store_value(MEM, mask, 0, addr, val)

    return sum(MEM.values())

res1 = part1()
print("solution is {}".format(res1))

res2 = part2()
print("solution is {}".format(res2))

