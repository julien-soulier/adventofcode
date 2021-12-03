import re

f = open("input.txt", "r")
lines = f.read().split('\n')
lines.remove('')
f.close()

def part1():
    pos=0
    depth=0
    for l in lines:
        m = re.match(r'^(forward|down|up) +(\d+)$', l)
        if m:
            action=m.group(1)
            value=int(m.group(2))
        else:
            print("Invalid line {}".format(l))
            exit(1)

        if action=="forward":
            pos+=value
        elif action=="down":
            depth += value
        else:
            depth -= value

    return pos*depth

def part2():
    pos=0
    depth=0
    aim=0
    for l in lines:
        m = re.match(r'^(forward|down|up) +(\d+)$', l)
        if m:
            action=m.group(1)
            value=int(m.group(2))
        else:
            print("Invalid line {}".format(l))
            exit(1)

        if action=="forward":
            pos+=value
            depth += aim * value
        elif action=="down":
            aim += value
        else:
            aim -= value

    return pos*depth

res1 = part1()
print("Soution part1 is {}".format(res1))

res2 = part2()
print("Soution part2 is {}".format(res2))
