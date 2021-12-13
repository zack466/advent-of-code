import numpy as np
from itertools import product

def neighbors(arr, idx):
    for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
        if dx == 0 and dy == 0:
            continue
        x, y = idx
        if 0 <= x + dx and x + dx < arr.shape[0]:
            if 0 <= y + dy and y + dy < arr.shape[1]:
                yield arr[(x + dx), (y + dy)], (x + dx, y + dy)

with open("day11.in", "r") as f:
    lines = map(lambda x: x.strip(), f.readlines())
    octopi = np.array([list(map(int, list(line))) for line in lines])

# does not mutate input array
def step(arr):
    arr = np.copy(arr)
    arr += 1
    flashed = np.full_like(arr, False)
    to_flash = arr > 9
    while to_flash.any(): 
        # print(to_flash)
        new_flash = np.full_like(to_flash, False)
        for idx in np.argwhere(to_flash):
            for n, n_idx in neighbors(arr, (idx[0], idx[1])):
                arr[n_idx] += 1
                if arr[n_idx] > 9:
                    new_flash[n_idx] = True
            flashed[(idx[0], idx[1])] = True
        to_flash = np.logical_and(new_flash, np.logical_not(flashed))
    for idx in np.argwhere(flashed):
        arr[(idx[0], idx[1])] = 0
    return arr

def solA():
    arr = octopi
    total = 0
    for _ in range(100):
        arr = step(arr)
        # print(arr)
        total += np.count_nonzero(arr == 0)
    print(total)

def solB():
    arr = octopi
    i = 1
    while True:
        arr = step(arr)
        if np.all(arr == 0):
            print(i)
            break
        else:
            i += 1

solB()
