import re
import string

def get_Nth(start_list, idx):
    N = [0]*idx

    i=1
    for n in start_list[0:-1]:
        N[n] = i
        i+=1

    last = start_list[-1]
    while i<idx:
        if N[last]==0:
            next = 0
        else:
            next = i-N[last]
        N[last]=i
        last = next
        i += 1

    return last

I = [16, 11, 15, 0, 1, 7]
res1 = get_Nth(I, 2020)
print("solution is {}".format(res1))
res2 = get_Nth(I, 30000000)
print("solution is {}".format(res2))

