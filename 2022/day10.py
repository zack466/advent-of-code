with open("day10.in", 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

def close(cycle, X):
    return any(((cycle-1 + i)%40 == X%40 for i in [-1, 0, 1]))

cycle = 0
X = 1
total = 0
crt = []
for l in lines:
    if l[:4] == "noop":
        cycle += 1
        if cycle % 40 == 20:
            total += cycle * X
        if close(cycle, X):
            crt.append('#')
        else:
            crt.append('.')
    else:
        arg = int(l[5:])
        cycle += 1
        if cycle % 40 == 20:
            total += cycle * X
        if close(cycle, X):
            crt.append('#')
        else:
            crt.append('.')

        cycle += 1
        if cycle % 40 == 20:
            total += cycle * X
        if close(cycle, X):
            crt.append('#')
        else:
            crt.append('.')
        X += arg

print(total)
for i in range(6):
    print("".join(crt[i * 40:(i+1)*40]))
