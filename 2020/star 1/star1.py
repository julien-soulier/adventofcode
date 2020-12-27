f = open("input.txt", "r")
lines = f.read().split('\n')
lines.remove('')
f.close()

a_nbr = list(map(int, lines))

def part1():
    for n in a_nbr:
        try:
            i = a_nbr.index(2020-n)
        except:
            pass
        else:
            l=a_nbr[i]
            print("{}+{}={} and {}*{}={}".format(n,l,n+l,n,l,n*l))
            return n*l

def part2():
    for n in a_nbr:
        for m in a_nbr:
            try:
                i = a_nbr.index(2020-n-m)
            except:
                pass
            else:
                l=a_nbr[i]
                print("{}+{}+{}={} and {}*{}*{}={}".format(n,m,l,n+m+l,n,m,l,n*m*l))
                return n*m*l


res1 = part1()
print("Soution part1 is {}".format(res1))

res2 = part2()
print("Soution part2 is {}".format(res2))
