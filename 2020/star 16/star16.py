import re
import string

f = open("input.txt", "r")
lines = f.readlines()
f.close()
p = re.compile('^(.+): (\d+)-(\d+) or (\d+)-(\d+)$')
q = re.compile('^departure')

def parse_lines():
    rules = {}
    full_range = set()
    all_fields = []
    field_table = []
    state = 0
    idx = 0
    res = 0
    for l in lines:
        l = l.rstrip('\n')

        if len(l) == 0:
            state += 1
            idx = 0
            continue
        
        if state == 0:
            m = p.match(l)
            if not m:
                print("error parsing line {} in state 0".format(l))
                break
            k=m.group(1)
            all_fields.append(k)
            r00 = int(m.group(2))
            r01 = int(m.group(3))
            r10 = int(m.group(4))
            r11 = int(m.group(5))
            rules[k] = set(range(r00, r01))
            rules[k].add(r01)
            rules[k].update(range(r10, r11))
            rules[k].add(r11)
            full_range.update(rules[k])
        
        if state == 1:
            idx += 1
            if idx == 2:
                my_ticket = l

        if state == 2:
            idx += 1
            if (idx == 1):
                for i in range(len(all_fields)):
                    field_table.append(all_fields.copy())

            if (idx >= 2):
                valid = True
                items = l.split(',')
                for item in items:
                    v = int(item)
                    if v not in full_range:
                        res += int(v)
                        valid = False
                        print("{} is invalid".format(v))
               
                if not valid:
                    continue

                for i in range(len(items)):
                    v = int(items[i])
                    for k,r in rules.items():
                        if v not in r:
                            field_table[i].remove(k)

    complete = False
    while not complete:
        complete = True
        for f in field_table:
            if len(f) == 1:
                for g in field_table:
                    if len(g) > 1:
                        if f[0] in g:
                            g.remove(f[0])
            else:
                complete = False

    my_fields = my_ticket.split(',')
    res2 = 1
    i = 0
    for f in field_table:
        m = q.match(f[0])
        if m:
            print('use field {}'.format(i))
            res2 *= int(my_fields[i])
        i += 1
    
    return res, res2

res1, res2 = parse_lines()
print("solution 1 is {}".format(res1))
print("solution 2 is {}".format(res2))

