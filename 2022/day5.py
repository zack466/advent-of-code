import re

parse = re.compile("move (\\d+) from (\\d+) to (\\d+)")

with open("day5.in", 'r') as f:
    lines = f.readlines()
    instructions = list(map(lambda line: tuple(map(int, parse.match(line).groups())), lines)) # type: ignore[override]

stacks = [
        list("SMRNWJVT"),
        list("BWDJQPCV"),
        list("BJFHDRP"),
        list("FRPBMND"),
        list("HVRPTB"),
        list("CBPT"),
        list("BJRPL"),
        list("NCSLTZBW"),
        list("LSG"),
        ]

for a, b, c in instructions:
    for i in range(a):
        stacks[c-1].append(stacks[b-1].pop())

for i in range(len(stacks)):
    print(stacks[i][-1], end="")
print()

stacks = [
        list("SMRNWJVT"),
        list("BWDJQPCV"),
        list("BJFHDRP"),
        list("FRPBMND"),
        list("HVRPTB"),
        list("CBPT"),
        list("BJRPL"),
        list("NCSLTZBW"),
        list("LSG"),
        ]

for a, b, c in instructions:
    stacks[c-1] += stacks[b-1][-a:]
    stacks[b-1] = stacks[b-1][:-a]

for i in range(len(stacks)):
    print(stacks[i][-1], end="")
print()
