# I saw someone doing AoC problems with numpy, so I'm gonna try to do the same
import numpy as np
from collections import deque

with open("day9.in", "r") as f:
    lines = map(lambda x: x.strip(), f.readlines())
    heights = np.array([list(map(int, list(line))) for line in lines])

def findLowPoints():
    padded = np.pad(heights, 1, mode='maximum')
    left = padded[1:-1, 1:-1] < padded[1:-1, 2:]
    right = padded[1:-1, 1:-1] < padded[1:-1, :-2]
    up = padded[1:-1, 1:-1] < padded[:-2, 1:-1]
    down = padded[1:-1, 1:-1] < padded[2:, 1:-1]
    mask = np.logical_and(left, np.logical_and(right, np.logical_and(up, down)))
    vals = heights[mask]
    return mask, vals

def neighbors(arr, idx):
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x, y = idx
        if 0 <= x + dx and x + dx < arr.shape[0]:
            if 0 <= y + dy and y + dy < arr.shape[1]:
                yield arr[(x + dx), (y + dy)], (x + dx, y + dy)

def solA():
    mask, vals = findLowPoints()
    ret = np.sum(vals) + len(vals)
    print(ret)

def basin(low_point):
    # flood fill bfs
    searched = np.full_like(heights, False)
    Q = deque()
    Q.append(low_point)
    size = 1
    searched[low_point] = True
    while not len(Q) == 0:
        idx = Q.pop()
        for n, n_idx in neighbors(heights, idx):
            if not searched[n_idx] and n != 9 and n > heights[idx]:
                Q.appendleft(n_idx)
                searched[n_idx] = True
                size += 1
    return size

def solB():
    mask, vals = findLowPoints()
    sizes = []
    for idx in np.argwhere(mask):
        point = (idx[0], idx[1])
        sizes.append(basin(point))
    sizes.sort(reverse=True)
    print(sizes[0] * sizes[1] * sizes[2])

solB()
