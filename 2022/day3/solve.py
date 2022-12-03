f = open("input.txt", "r")
lines = f.read().split('\n')
lines.remove('')
f.close()

def priority(c):
    base = 26 if c.isupper() else 0
    return ord(c) - ord('A' if c.isupper() else 'a') + 1 + base

def part1():
    items = [set(L[0:len(L)//2]).intersection(set(L[len(L)//2:])) for L in lines]
    return sum(map(lambda x: priority(x.pop()), items))

def part2():
    L=lines
    items = [set(L[i]).intersection(set(L[i+1]), L[i+2]) for i in range(0, len(L), 3)]
    return sum(map(lambda x: priority(x.pop()), items))

print("Soution part1 is {}".format(part1()))
print("Soution part2 is {}".format(part2()))
