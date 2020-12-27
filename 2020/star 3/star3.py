import re
import string

def count_trees(dx,dy):
    x = 0
    y = 0
    total = 0   
    
    f = open("input.txt", "r")
    for l in f.readlines():
        if (dy==1) or ((dy==2) and (y%2==0)):
            if l[x]=='#':
                print('hit at line {}'.format(y))
                total += 1
            x = (x+dx)%(len(l)-1)
        y += 1
    f.close()
    return total

t0 = count_trees(1,1)
t1 = count_trees(3,1)
t2 = count_trees(5,1)
t3 = count_trees(7,1)
t4 = count_trees(1,2)

print("{} {} {} {} {} {}".format(t0,t1,t2,t3,t4,t0*t1*t2*t3*t4))