#/bin/env python3

import functools

def compare(left, right):
    #print(f"Comparing {left} vs {right}")
    if type(left) is int and type(right) is int:
        return left - right

    if type(left) is int:
        left = [left]

    if type(right) is int:
        right = [right]

    pairs = list(zip(left, right))
    for pair in pairs:
        #print(f"Compare {pair} in {left} {right}")
        cmp = compare(pair[0],pair[1])
        if cmp != 0:
            return cmp

    return 1 if len(left) > len(pairs) else -1 if len(right) > len(pairs) else 0

def get_right_order_pairs(input="input.txt"):
    idx = 1
    right_order_list = []

    with open(input, "r") as f:
        for pair in f.read().strip().split("\n\n"):
            left, right = pair.split("\n")

            cmp = compare(eval(left), eval(right))
            if cmp <= 0:
                right_order_list.append(idx)
    
            idx += 1
    
    return right_order_list

def sort_packets(input="input.txt"):
    with open(input, "r") as f:
        packets = f.read().split('\n')

    packets = [eval(p) for p in packets if p!='']
    packets.extend([[[2]], [[6]]])
    packets.sort(key=functools.cmp_to_key(compare))
    return packets

pairs = get_right_order_pairs()
print(f"Soution part1 is {sum(pairs)}")

packets = sort_packets()
key1 = packets.index([[2]]) + 1
key2 = packets.index([[6]]) + 1
print(f"Soution part2 is {key1 * key2}")



