import re

PARSE = re.compile("target area: x=(-?\\d+)\\.\\.(-?\\d+), y=(-?\\d+)\\.\\.(-?\\d+)")
with open("day17.in") as f:
    match = PARSE.match(f.readline())
    minx, maxx, miny, maxy = map(int, match.groups())

def done(vx0, x, y):
    if vx0 > 0:
        return x > maxx or y < miny
    else:
        return x < minx or y < miny

def success(x, y):
    return x >= minx and x <= maxx and y >= miny and y <= maxy

def sim(vx, vy):
    vx0 = vx
    x, y = 0, 0
    while not done(vx0, x, y) and not success(x, y):
        x += vx
        y += vy
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
        yield x, y, vx, vy

def getLast(iter):
    a = None
    b = iter
    while True:
        try:
            a = next(b)
        except:
            return a

# turns out brute force works fine for both A and B
def solA():
    for vy in range(250, 0, -1):
        for vx in range(1, 500):
            last = getLast(sim(vx, vy))
            if last != None:
                x, y, _, _ = last
                if success(x, y):
                    print(vx, vy)
                    return

def solB():
    count = 0
    for vy in range(500, -500, -1):
        for vx in range(500, -500, -1):
            last = getLast(sim(vx, vy))
            if last != None:
                x, y, _, _ = last
                if success(x, y):
                    count += 1
    print(count)

solB()
