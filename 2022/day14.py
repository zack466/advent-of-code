import re

COORD = re.compile("(\\d+),(\\d+)")

with open("day14.in", 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

N = 750
cave = [["." for _ in range(N)] for _ in range(N)]

max_y = 0 # part 2

for line in lines:
    coords = list(map(lambda x: (int(x[0]), int(x[1])), COORD.findall(line)))
    for i in range(len(coords) - 1):
        x1, y1 = coords[i]
        x2, y2 = coords[i+1]
        x1, x2 = min((x1, x2)), max((x1, x2))
        y1, y2 = min((y1, y2)), max((y1, y2))
        if y2 > max_y: # part 2
            max_y = y2 # part 2
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                cave[y][x] = "#"

def filled(x, y):
    # return cave[y][x] == "#" or cave[y][x] == "o" # part 1
    return y == max_y+2 or cave[y][x] == "#" or cave[y][x] == "o" # part 2

def sand():
    x, y = 500, 0
    total = 0
    while True:
        if y == N - 1:
            break
        if not filled(x, y+1):
            y += 1
        elif not filled(x-1, y+1):
            x -= 1
            y += 1
        elif not filled(x+1, y+1):
            x += 1
            y += 1
        else:
            cave[y][x] = "o"
            total += 1
            if (x, y) == (500, 0): break # part 2
            x, y = 500, 0
    return total

# for i in range(10):
#     print([cave[i][x] for x in range(494, 504)])
print(sand())
