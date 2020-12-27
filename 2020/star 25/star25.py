import re
import string
import operator

f = open("input.txt", "r")
lines = f.read().split('\n')
f.close()

def get_loop(key):
    v = 1
    loop = 0
    while v!= key:
        v *= 7
        v %= 20201227
        loop += 1
    return loop

def compute_key(loop, number):
    v = 1
    for l in range(loop):
        v *= number
        v %= 20201227
    return v

pub_keys = tuple(map(int, lines))
loops = tuple(map(get_loop, pub_keys))
pk0 = compute_key(loops[0], pub_keys[1])
pk1 = compute_key(loops[1], pub_keys[0])
priv_keys = (pk0, pk1)

print(loops)
print(pub_keys)
print(priv_keys)

res1 = 0
print("solution part 1: {}".format(res1))

res2 = 0
print("solution part 2: {}".format(res2))