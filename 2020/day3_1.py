fin = open('day3_input', 'r')
idx = 0
count = 0
# part 1
# for line in fin.readlines():
#     line = line.rstrip()
#     print(line)
#     if line[idx % len(line)] == '#':
#         count += 1
#     idx += 3
# 
# print(count)

# part 2
t = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]
right = [0 for _ in t]
down = [0 for _ in t]
counts = [0 for _ in t]
for i, line in enumerate(fin.readlines()):
    line = line.rstrip()
    for j, tup in enumerate(t):
        if down[j] == i:
            if line[right[j] % len(line)] == '#':
                counts[j] += 1
            right[j] += tup[0]
            down[j] += tup[1]

import numpy as np
print(np.prod(counts))
fin.close()
