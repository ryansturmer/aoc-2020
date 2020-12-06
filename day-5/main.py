import sys

with open(sys.argv[1]) as fp:
    passes = list(map(lambda x : x.strip(), fp.readlines()))

    part1 = 0

    all_seats = set()
    for row in range(128):
        for col in range(8):
            all_seats.add(row*8 + col)

    booked_seats = set()

    for p in passes:
        rows,cols = list(range(128)),list(range(8))

        fb,lr = p[:7], p[7:]
        for x in fb:
            rows = rows[:int(len(rows)/2)] if x == 'F' else rows[int(len(rows)/2):]
        for y in lr:
            cols = cols[:int(len(cols)/2)] if y == 'L' else cols[int(len(cols)/2):]

        row,col = rows[0],cols[0]
        seat_id = row*8 + col
        part1 = max(part1, seat_id)
        booked_seats.add(seat_id)

    candidate_seats = all_seats-booked_seats

    for seat in candidate_seats:
        if seat-1 in booked_seats and seat+1 in booked_seats:
            print(seat)


    print("Part 1: ", part1)