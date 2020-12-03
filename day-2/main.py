import re

regex = re.compile(r'([0-9]+)\-([0-9]+)\s*([a-zA-z])\:\s*([a-zA-Z]+)\n')
with open('input.txt') as fp:
    n = list(map(lambda x : list(regex.match(x).groups()), fp.readlines()))

    part1 = 0
    part2 = 0
    for a,b,c,p in n:
        count = list(p).count(c)
        a = int(a)
        b = int(b)
        if a <= count <= b:
            part1+=1
        if (p[a-1] == c) ^ (p[b-1] == c):
            part2+=1

    print('Part 1: ', part1 )
    print('Part 2: ', part2 )
