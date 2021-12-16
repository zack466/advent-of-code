from heapq import heappop, heappush

with open("day15.in", "r") as f:
    lines = map(lambda x: x.strip(), f.readlines())
    risks = [list(map(int, list(line))) for line in lines]
    N = len(risks)

# actually wrong because I assumed you could only move right and down (but worked for part A)
def dp(coords, memo):
    x, y = coords
    if (x, y) == (0, 0):
        return 0
    if x < 0 or y < 0:
        return 9e12
    if coords in memo.keys():
        return memo[coords]
    a = dp((x-1, y), memo)
    b = dp((x, y-1), memo)
    ret = min(a, b) + risks[x][y]
    memo[coords] = ret
    return ret

def solA():
    memo = dict()
    print(dp((N-1, N-1), memo))

def addWrap(x, y):
    ret = x + y
    while ret >= 10:
        ret -= 9
    return ret

def hcat(a, b):
    assert len(a) == len(b)
    return [a[i] + b[i] for i in range(len(a))]

def vcat(a, b):
    assert len(a[0]) == len(b[0])
    return a + b

def map2d(x, f):
    return [list(map(f, x[i])) for i in range(len(x))]

def solB(risks):
    for k in range(1, 5):
        right = map2d([risks[x][:N] for x in range(N)], lambda y: addWrap(y, k))
        risks = hcat(risks, right)
    for k in range(1, 5):
        bottom = map2d(risks[:N], lambda y: addWrap(y, k))
        risks = vcat(risks, bottom)
    # dijkstra's w/ priority queue
    Q = [(0, (0, 0))]
    seen = set()
    while len(Q) != 0:
        score, coords = heappop(Q)
        if coords in seen:
            continue
        seen.add(coords)
        if coords == (len(risks) - 1, len(risks) - 1):
            print(score + risks[len(risks) - 1][len(risks) - 1] - risks[0][0], coords)
            break
        x, y = coords
        if x < len(risks) - 1:
            new_coords = (x+1, y)
            heappush(Q, (score + risks[x][y], new_coords))
        if y < len(risks) - 1:
            new_coords = (x, y+1)
            heappush(Q, (score + risks[x][y], new_coords))
        if x > 1:
            new_coords = (x-1, y)
            heappush(Q, (score + risks[x][y], new_coords))
        if y > 1:
            new_coords = (x, y-1)
            heappush(Q, (score + risks[x][y], new_coords))

# solA()
solB(risks)
