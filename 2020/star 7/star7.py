import re
import string

#p = re.compile("^([\w\s]+) bags contain ((?:no other bags)|(?:\s*(\d+) ([\w\s]+) bags?,?))+\.$")
p = re.compile("^([\w\s]+) bags contain ((?:no other bags)|(?:[\s\w,]*))\.$")
q = re.compile("\s*(\d+) ([\w\s]+) bag")

def count_bags(color):
    print("COUNT bags for {}".format(color))
    count = 0
    for c in rule_set[color].keys():
        count += count_bags(c)*int(rule_set[color][c])

    # the inner bags plus the current bag
    return count+1

f = open("input.txt", "r")
total = 0
idx = 0
rule_set = {}
for l in f.readlines():
    l = l.rstrip('\n')
    m = p.match(l)
    if not m:
        print("error: line '{}' does not match".format(l))
    else:
        bag = m.group(1)
        rule = m.group(2)
        sub_rule = {}

        if (rule != "no other bags"):
            for r in rule.split(','):
                n = q.match(r)
                if n:
                    sub_rule[n.group(2)] = n.group(1)
                else:
                    print("error: rule '{}' does not match".format(r))
        
        rule_set[bag] = sub_rule
         
    idx += 1

f.close()

bags = ['shiny gold']
curt_len = 0
while curt_len < len(bags):
    curt_len = len(bags)
    for color in bags:
        for rule in rule_set:
            if (color in rule_set[rule].keys()):
                if rule not in bags:
                    bags.append(rule)
                print("bag {} is OK".format(rule))
    
#remove 1 because 'shiny gold' bag must not be taken into account
print("Solution #1 is {}".format(curt_len - 1))


#remove 1 because 'shiny gold' bag must not be taken into account
print("Solution #2 is {}".format(count_bags('shiny gold')-1))
