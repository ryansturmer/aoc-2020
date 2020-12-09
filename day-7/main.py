import sys
import re

rules = {}
with open(sys.argv[1]) as fp:
    for line in fp.readlines():
        match = re.match(r'([\s\w]+) bags contain ', line)
        bag = match.groups()[0]
        rest = line[match.span()[1]:]
        rules[bag] = {}
        if rest == 'no other bags.\n':
            continue
        for part in rest.strip('.').split(','):
            match = re.match(r'\s*([0-9]+) ([\w\s]+) bags?', part)
            n, b = match.groups()
            rules[bag][b] = int(n)

def find_all_bags(bag):
    contained = set()
    s = [bag]
    while s:
        bag = s.pop()
        contained.add(bag)
        for b in rules[bag]:
            if b not in contained:
                s.append(b)
    return contained-set(bag)

def count_bags(bag):
    return sum([rules[bag][b]*count_bags(b) for b in rules[bag]]) + 1

part1 = 0
contained_bags = {}
for bag in rules:
    contained_bags[bag] = find_all_bags(bag)
    if 'shiny gold' in contained_bags[bag]:
        part1 += 1

print("Part 1: ", part1-1)
print("Part 2: ", count_bags('shiny gold')-1)