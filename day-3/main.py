import re
import sys
with open(sys.argv[1]) as fp:
    rows = list(map(lambda line : list(line.strip()), fp.readlines()))
    X = len(rows[0])
    Y = len(rows)
    part2 = 1
    for sx,sy in (1,1),(3,1),(5,1),(7,1),(1,2):
        x = y = 0
        trees = 0
        while y < Y:
            trees += 1 if rows[y][x] == '#' else 0
            x = (x+sx)%X
            y = y+sy

        if (sx,sy) == (3,1):
            print("Part 1: ",trees)

        part2*=trees

    print("Part 2: ",part2)
