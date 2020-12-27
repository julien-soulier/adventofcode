f = open("input.txt", "r")
a_str = f.readlines()
a_nbr = []
for s in a_str:
    a_nbr.append(int(s))

for n in a_nbr:
    for m in a_nbr:
        try:
            i = a_nbr.index(2020-n-m)
        except:
            pass
        else:
            l=a_nbr[i]
            print("{}+{}+{}={} and {}*{}*{}={}".format(n,m,l,n+m+l,n,m,l,n*m*l))
            break

f.close()