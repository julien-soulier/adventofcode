f = open("input.txt", "r")
input = f.read()
f.close()

# !!! must remove the last empty line in input.txt !!!
E=input.split('\n\n')
C=[sum(map(int, x.split('\n'))) for x in E]
C.sort(reverse=True)

def part1():
    return C[0]

def part2():
    return sum(C[0:3])

print("Soution part1 is {}".format(part1()))
print("Soution part2 is {}".format(part2()))
