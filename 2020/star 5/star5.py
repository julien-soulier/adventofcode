import re
import string

f = open("input.txt", "r")
max_id = 0
idx = 0
ids = []
for l in f.readlines():
    l = l.replace('B', '1')
    l = l.replace('R', '1')
    l = l.replace('F', '0')
    l = l.replace('L', '0')
    row = int(l[0:7], 2)
    col = int(l[7:10], 2)
    print("{} r:{} c:{}".format(l, row, col))
    id = row * 8 + col
    ids.append(id)
    if id>max_id:
        max_id = id

    idx += 1

for i in range(2,max_id-1):
    p = i-1
    n = i+1
    if (p in ids) and (n in ids) and (i not in ids):
        print(ids.index(p))
        print(ids.index(n))
        print("Found Seat {}".format(i))


print(max_id)
#print(ids)
f.close()
