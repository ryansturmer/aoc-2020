import sys

with open(sys.argv[1]) as fp:
    groups = [[]]
    yesses = [set()]
    for line in fp.readlines():
        questions = line.strip()
        if not questions:
            groups.append([])
            yesses.append(set())
        else:
            if not groups[-1]:
                yesses[-1] = set(questions)
            else:
                yesses[-1] &= set(questions)
            
            groups[-1].append(questions)
            

    print("Part 1:", sum(map(len, yesses)))

