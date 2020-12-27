import re
import string

f = open("input.txt", "r")
lines = f.readlines()
f.close()

S={}
B={}

def set_state(C,x,y,z,w,state):
    k='{},{},{},{}'.format(x,y,z,w)
    C[k]=state

def is_active(C,x,y,z,w):
    k='{},{},{},{}'.format(x,y,z,w)
    if k in C.keys() and C[k]:
        return True
    else:
        return False

def init_space(algo):
    B['xmin']=-1
    B['xmax']=len(lines[0])
    B['ymin']=-1
    B['ymax']=len(lines[0])
    B['zmin']=-1
    B['zmax']=2
    if algo == 1:
        B['wmin']=0
        B['wmax']=1
    else:
        B['wmin']=-1
        B['wmax']=2
    for x in range(len(lines)):
        l = lines[x].rstrip('\n')
        for y in range(len(l)):
            if l[y]=='#':
                set_state(S,x,y,0,0, True)

def count_active(C):
    count = 0
    for k in C.keys():
        if C[k]:
            count += 1
    return count

def count_active_neighbours(C,x,y,z,w):
    count = 0
        
    for xi in range(x-1,x+2):
        for yi in range(y-1,y+2):
            for zi in range(z-1,z+2):
                for wi in range(w-1,w+2):
                    if is_active(C,xi,yi,zi,wi):
                        count += 1

    if is_active(C,x,y,z,w):
        count -= 1
    
    return count

def do_one_turn(S):
    D = S.copy()
    for x in range(B['xmin'],B['xmax']):
        for y in range(B['ymin'],B['ymax']):
            for z in range(B['zmin'],B['zmax']):
                for w in range(B['wmin'],B['wmax']):
                    c = count_active_neighbours(D,x,y,z,w)
                    if is_active(D,x,y,z,w):
                        if c!=2 and c!=3:
                            set_state(S,x,y,z,w,False)
                    else:
                        if c==3:
                            set_state(S,x,y,z,w,True)
    

def do_boot(loop, algo):
    for i in range(loop):
        do_one_turn(S)
        B['xmin'] -= 1
        B['ymin'] -= 1
        B['zmin'] -= 1
        B['xmax'] += 1
        B['ymax'] += 1
        B['zmax'] += 1
        if algo==2:
            B['wmin'] -=1
            B['wmax'] +=1

init_space(2)
do_boot(6,2)
res1 = count_active(S)

print("solution is {}".format(res1))
