import re
import string

p = re.compile('^(\d+)-(\d+)\s+(\w):\s+(\w+)$')
f = open("input.txt", "r")

total = 0
for l in f.readlines():
    m=p.match(l)
    print(l)
    pwd = m.group(4)
    letter = m.group(3)
    mi = int(m.group(1))
    ma = int(m.group(2))
    if (pwd[mi-1]==letter) and (pwd[ma-1]!=letter):
        total +=1
    elif (pwd[mi-1]!=letter) and (pwd[ma-1]==letter):
        total += 1
    
print(total)

f.close()