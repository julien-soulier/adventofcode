import re
import string

f = open("input.txt", "r")
lines = f.readlines()
f.close()

rules = {}

def get_matching_rule(rule):
    m = re.match(r'\s*"(.)"', rule)
    if m:
        return m.group(1)
    
    m = re.match(r'(.+)\|(.+)', rule)
    if m:
        return '('+ get_matching_rule(m.group(1)) + '|' + get_matching_rule(m.group(2)) + ')'

    s=''
    for e in rule.split(' '):
        if len(e)>0:
            s += get_matching_rule(rules[e])
    return s

while True:
    line = lines.pop(0)
    line = line.rstrip('\n')
    if len(line)==0:
        break

    elts = line.split(':')
    k = elts[0]
    rules[k] = elts[1]

regexp = get_matching_rule(rules['0'])
p = re.compile('^'+regexp+'$')
count = 0
for line in lines:
    m = p.match(line)
    if m:
        count += 1

res1 = count
print("solution 1 is {}".format(res1))

r1 = get_matching_rule(rules['42'])
r2 = get_matching_rule(rules['31'])

count = 0
for line in lines:
    for i in range(1,10):
        done = False
        for j in range(1,10):
            regexp = '^('+r1+'){'+str(i)+'}('+r1+'){'+str(j)+'}('+r2+'){'+str(j)+'}$'
            p = re.compile(regexp)
            m = p.match(line)
            if m:
                done = True
                count += 1
                break
        if done:
            break

res2 = count
print("solution 2 is {}".format(res2))
