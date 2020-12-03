with open('input.txt') as fp:
    n = list(map(int, fp.readlines()))

for a in n:
    for b in n:
        if a + b == 2020:
            print("2 Numbers: %d" % (a*b))
        for c in n:
            if a + b + c == 2020:
                print("3 Numbers: %d" % (a*b*c))
