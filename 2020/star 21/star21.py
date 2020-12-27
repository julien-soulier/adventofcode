import re
import string
import math

f = open("input.txt", "r")
lines = f.read().split('\n')
f.close()

food_list = []
alg_set = set()
ing_set = set()

for line in lines:
    if len(line)==0:
        continue
    m = re.match(r'^(.+) \(contains (.*)\)$', line)
    if m:
        f = {}
        ing = m.group(1)
        alg = m.group(2).replace(' ','')
        f['ing'] = set(ing.split(' '))
        f['alg'] = set(alg.split(','))
        alg_set.update(f['alg'])
        ing_set.update(f['ing'])
        food_list.append(f)
    else:
        print("Bad food -{}-".format(line))

alg_list = {}
alg_ing_set = set()
while len(alg_set)>0:
    for alg in alg_set:
        ings = ing_set.copy()
        for food in food_list:
            if alg in food['alg']:
                ings.intersection_update(food['ing'])
        
        if len(ings)==1:
            ing = ings.pop()
            print("Processed {} {}".format(alg, ing))
            alg_list[alg]=ing
            alg_ing_set.add(ing)
            for f in food_list:
                f['alg'].discard(alg)
                f['ing'].discard(ing)

    for alg in alg_list.keys():
        alg_set.discard(alg)

#print(alg_ing_set)

total=0
for food in food_list:
    total += len(food['ing'].difference(alg_ing_set))

print("solution part 1: {}".format(total))

res=''
for alg in sorted(alg_list.keys()):
    res+=alg_list[alg]+','
    
print("solution part 2: {}".format(res[0:-1]))