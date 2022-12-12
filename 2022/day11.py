from tqdm import tqdm
from functools import reduce

with open("day11.in", 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

class Monkey:
    def __init__(self, items, op, test, if_true, if_false):
        self.items = items
        self.op = op
        self.test = test
        self.if_true = if_true
        self.if_false = if_false

monkeys = [
        Monkey([71, 56, 50, 73], lambda x: x * 11, 13, 1, 7),
        Monkey([70, 89, 82], lambda x: x + 1, 7, 3, 6),
        Monkey([52, 95], lambda x: x * x, 3, 5, 4),
        Monkey([94, 64, 69, 87, 70], lambda x: x + 2, 19, 2, 6),
        Monkey([98, 72, 98, 53, 97, 51], lambda x: x + 6, 5, 0, 5),
        Monkey([79], lambda x: x + 7, 2, 7, 0),
        Monkey([77, 55, 63, 93, 66, 90, 88, 71], lambda x: x * 7, 11, 2, 4),
        Monkey([54, 97, 87, 70, 59, 82, 59], lambda x: x + 8, 17, 1, 3),
        ]

# monkeys = [
#         Monkey([79, 98], lambda x: x * 19, 23, 2, 3),
#         Monkey([54, 65, 75, 74], lambda x: x + 6, 19, 2, 0),
#         Monkey([79, 60, 97], lambda x: x * x, 13, 1, 3),
#         Monkey([74], lambda x: x + 3, 17, 0, 1),
#         ]

MOD = reduce(lambda a, b: a * b, map(lambda x: x.test, monkeys))

tracker = [0 for _ in range(len(monkeys))]

for round in tqdm(range(10000)): # part 2
# for round in range(20): # part 1
    for i, m in enumerate(monkeys):
        for item in m.items:
            tracker[i] += 1
            item %= MOD # part 2
            item = m.op(item)
            # item //= 3 # part 1
            if item % m.test == 0:
                monkeys[m.if_true].items.append(item)
            else:
                monkeys[m.if_false].items.append(item)
        m.items = []

answer = sorted(tracker, reverse=True)
print(answer[0] * answer[1])
