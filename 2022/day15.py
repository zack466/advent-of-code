import re

DATA = re.compile("Sensor at x=(-?\\d+), y=(-?\\d+): closest beacon is at x=(-?\\d+), y=(-?\\d+)")

with open("day15.in", 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

data = [list(map(int, DATA.match(line).groups())) for line in lines]

def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# part 1
# s = set()
# exclude = [(d[2], d[3]) for d in data]

# for x1, y1, x2, y2 in data:
#     d = distance(x1, y1, x2, y2)
#     ydist = abs(y1 - 2000000)
#     if ydist <= d:
#         print(x1, y1, x2, y2, x1 - (d - ydist), x1 - (d - ydist) + 1)
#         for x in range(x1 - (d - ydist), x1 + (d - ydist) + 1):
#             s.add(x)

# for x, y in exclude:
#     if y == 2000000:
#         if x in s:
#             s.remove(x)

# print(len(s))

# part 2
def at_dist(x, y, d):
    s = set()
    for dx, dy in zip(range(d+1), range(d, -1, -1)):
        s.add((x+dx, y+dy))
        s.add((x-dx, y+dy))
        s.add((x+dx, y-dy))
        s.add((x-dx, y-dy))
    return s

def search():
    for x1, y1, x2, y2 in data:
        print(x1, y1)
        d = distance(x1, y1, x2, y2) + 1
        for xdx, ydy in at_dist(x1, y1, d):
            if not ((0 <= xdx <= 4000000) and (0 <= ydy <= 4000000)):
                continue
            good = True
            for x11, y11, x22, y22 in data:
                if (x11, y11) == (x1, y1):
                    continue
                if distance(x11, y11, xdx, ydy) >  distance(x11, y11, x22, y22):
                    pass
                else:
                    good = False
                    break
            if good:
                print(xdx, ydy, xdx*4000000 + ydy)
                return

# running with pypy recommended lmao
search()
