from collections import deque

with open("day12.in", 'r') as f:
    lines = list(map(lambda x: list(x.strip()), f.readlines()))

def height(ch):
    if ch == "S":
        return ord("a")
    elif ch == "E":
        return ord("z")
    else:
        return ord(ch)


visited = [[False for _ in range(len(lines[0]))] for _ in range(len(lines))]
depth = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]

def neighbor(x, y):
    for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= x+dx < len(lines[0]):
            if 0 <= y+dy < len(lines):
                yield x+dx, y+dy

def search(x, y):
    Q = deque()
    Q.append((x, y))
    visited[y][x] = True
    while len(Q) > 0:
        (x, y) = Q.pop()
        for nx, ny in neighbor(x, y):
            if not visited[ny][nx]:
                # if height(lines[y][x]) + 1 >= height(lines[ny][nx]): # part 1
                if height(lines[ny][nx]) + 1 >= height(lines[y][x]): # part 2
                    depth[ny][nx] = depth[y][x] + 1
                    visited[ny][nx] = True
                    Q.appendleft((nx, ny))

# part 1
# search(0, 20)
# print(depth[20][149])

# part 2
search(149, 20)
best = 1e9
bestcoords = None
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == "a" and visited[y][x] and depth[y][x] < best:
            best = depth[y][x]
            bestcoords = (x, y)
print(best)
print(bestcoords)
