import re

POINT = re.compile("(\\d+),(\\d+)")
FOLD = re.compile("fold along (x|y)=(\\d+)")

def parse_point(x):
    match = POINT.match(x)
    return (int(match.group(1)), int(match.group(2)))

def parse_fold(x):
    match = FOLD.match(x)
    return (match.group(1), int(match.group(2)))

with open("day13.in", 'r') as f:
    lines = f.readlines()
    i = lines.index("\n")
    points, folds = lines[:i], lines[i+1:]
    all_points = list(map(parse_point, points))
    all_folds = list(map(parse_fold, folds))

def fold_point(point, folds):
    x, y = point
    for p, q in folds:
        if p == 'x':
            if x > q:
                x = 2 * q - x
        elif p == 'y':
            if y > q:
                y = 2 * q - y
    return (x, y)

def solA():
    final_points = set()
    for p in all_points:
        final_points.add(fold_point(p, all_folds[:1]))
    print(len(final_points))

def solB():
    final_points = set()
    for p in all_points:
        final_points.add(fold_point(p, all_folds))
    # checked size of smallest x and y folds
    for y in range(13):
        for x in range(81):
            if (x, y) in final_points:
                print("#", end="")
            else:
                print(".", end="")
        print()

solB()
