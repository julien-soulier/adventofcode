#/bin/env python3

# !!! must remove the last empty line in input.txt !!!
with open("input.txt", "r") as f:
    E=f.read().split('\n\n')
    C=[sum(map(int, x.split('\n'))) for x in E]
    C.sort(reverse=True)
    print(f"Soution part1 is {C[0]}")
    print(f"Soution part2 is {sum(C[0:3])}")
