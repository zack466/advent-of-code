with open("day3.in", 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

score = lambda c:(lambda d:[d+58,d][d>0])(ord(c)-96)

total = sum(map(lambda l:(lambda a,b:score(set(a).intersection(set(b)).pop()))(l[:len(l)//2],l[len(l)//2:]),lines))

total = 0
for i in range(0, len(lines), 3):
    items = list(map(set, lines[i: i+3]))
    j = items[0].intersection(items[1]).intersection(items[2]).pop()
    total += score(j)

print(total)
