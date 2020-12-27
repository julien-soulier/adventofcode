import re
import string

f = open("input.txt", "r")
lines = f.readlines()
f.close()
p = re.compile('^(\w)(\d+)$')

def move_ship(algo):
    if algo==1:
        dx = 1
        dy = 0
    else:
        dx = 10
        dy = 1
    X = 0
    Y = 0
    for l in lines:
        m = p.match(l)
        if m:
            cmd = m.group(1)
            val = int(m.group(2))

            #print("CMD {}{}: {},{} {}x{} ".format(cmd, val, X, Y, dx, dy), end='') 
            if cmd == 'E':
                if (algo == 1):
                    X += val
                else:
                    dx += val
            elif cmd == 'W':
                if (algo == 1):
                    X -= val
                else:
                    dx -= val
            elif cmd == 'S':
                if (algo == 1):
                    Y -= val
                else:
                    dy -= val
            elif cmd == 'N':
                if (algo == 1):
                    Y += val
                else:
                    dy += val
            elif cmd == 'L':
                while val >= 90:
                    tmp = dx
                    dx = -dy
                    dy = tmp
                    val -= 90
                if val != 0:
                    print("Unsupported Left rotation {}".format(val))
            elif cmd == 'R':
                while val >= 90:
                    tmp = -dx
                    dx = dy
                    dy = tmp
                    val -= 90
                if val != 0:
                    print("Unsupported right rotation {}".format(val))
            elif cmd == 'F':
                X += val * dx
                Y += val * dy
            else:
                print("Invalid command {}".format(cmd))
        else:
            print("Invalid line {}".format(l))
        #print("--> {},{} -> {},{}".format(X, Y, dx, dy))
    
    return abs(X)+abs(Y)

res1 = move_ship(1)
print("solution is {}".format(res1))

res2 = move_ship(2)
print("solution is {}".format(res2))

