with open("day01.in", 'r') as f:
    lines = f.readlines()

totals = []

total = 0
for i, line in enumerate(lines):
    line = line.strip()
    if line == "":
        totals.append(total)
        total = 0
        continue
    total += int(line)

totals.sort(reverse=True)
print(sum(totals[:3]))
