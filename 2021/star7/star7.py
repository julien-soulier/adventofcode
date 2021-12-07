f = open("input.txt", "r")
nums = list(map(int, f.read().split(',')))
f.close()

import statistics

def fuel_cost(pos, algo):
    if algo==1:
        return sum(map(lambda x: abs(x-pos), nums))
    else:
        return sum(map(lambda x: (abs(x-pos)*(abs(x-pos)+1))//2, nums))

def resolve(algo):
    m = round(statistics.mean(nums))
    b = fuel_cost(m, algo)
    a = fuel_cost(m-1, algo)
    c = fuel_cost(m+1, algo)

    if min(a,b,c)==b:
        return b
    else:
        step = 1 if c<b else -1
        m+=step
        a = b
        b = fuel_cost(m, algo)
        while (b<a):
            m += step
            a = b
            b = fuel_cost(m, algo)
        
        return a

def part1():
    return resolve(1)

def part2():
    return resolve(2)

res1 = part1()
print("Soution part1 is {}".format(res1))

res2 = part2()
print("Soution part2 is {}".format(res2))