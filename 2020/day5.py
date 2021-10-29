with open("input", 'r') as f:
    lines = f.readlines()
m = set()
min_ = 1024
max_ = 0
for line in lines:
    line = line.rstrip()
    row = 0
    for i,FB in enumerate(line[:7]):
        x = 0 if FB == 'F' else 1
        row += 2**(6-i) * x
    col = 0
    for i,FB in enumerate(line[7:]):
        x = 0 if FB == 'L' else 1
        col += 2**(2-i) * x
    # print(line, row, col)
    seatid = row * 8 + col
    m.add(seatid)
    if seatid > max_:
        max_ = seatid
    if seatid < min_:
        min_ = seatid
for i in range(min_, max_):
    if i not in m:
        print(i)