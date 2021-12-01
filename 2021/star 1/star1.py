f = open("input.txt", "r")
lines = f.read().split('\n')
lines.remove('')
f.close()

depths = list(map(int, lines))

def part1():
    count=0
    prev=depths[0]
    for d in depths:
        if d>prev:
            count += 1
        prev = d
    return count

def part2():
    count = 0

    prev2=depths[0]
    prev1=depths[1]
    prev = prev1 + prev2 + depths[2]
    for d in depths[2:]:
        curt=prev1+prev2+d
        if (curt > prev):
            count += 1
        prev2 = prev1
        prev1 = d
        prev = curt 
    return count

res1 = part1()
print("Soution part1 is {}".format(res1))

res2 = part2()
print("Soution part2 is {}".format(res2))
