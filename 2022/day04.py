import re

parse = re.compile("(\\d+)-(\\d+),(\\d+)-(\\d+)")

with open("day04.in", 'r') as f:
    lines = f.readlines()
    intervals = list(map(lambda line: tuple(map(int, parse.match(line).groups())), lines)) # type: ignore[override]

total = 0
for a, b, c, d in intervals:
    if (a <= c <= d <= b) or (c <= a <= b <= d):
        total += 1

print(total)

total = 0
for a, b, c, d in intervals:
    if (c <= b <= d) or (a <= c <= b) or (c <= a <= d) or (a <= d <= b):
        total += 1

print(total)
