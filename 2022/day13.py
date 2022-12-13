with open("day13.in", 'r') as f:
    data = f.read().strip().split("\n\n")

def check(left, right):
    # print(left, right)
    if isinstance(left, int):
        if isinstance(right, int):
            if left == right:
                return None
            return left <= right
        elif isinstance(right, list):
            return check([left], right)
    elif isinstance(left, list):
        if isinstance(right, int):
            return check(left, [right])
        elif isinstance(right, list):
            # print(left, right)
            i = 0
            while i < len(left) and i < len(right):
                res = check(left[i], right[i])
                if res == None:
                    i += 1
                    continue
                else:
                    return res
            if i == len(left) == len(right):
                return None
            if i == len(left) and i < len(right):
                return True
            if i == len(right) and i < len(left):
                return False
            return True
    assert False

# part 1
total = 0
lines = []
for i, d in enumerate(data):
    left, right = map(eval, d.split("\n"))
    lines.append(left) # part 2
    lines.append(right) # part 2
    if check(left, right):
        total += i + 1

lines.append([[2]])
lines.append([[6]])

print(total)


# part 2

# bubble sort lmao
for i in range(len(lines)):
    for j in range(len(lines)):
        if check(lines[i], lines[j]):
            lines[i], lines[j] = lines[j], lines[i]

for i, l in enumerate(lines):
    if l == [[2]] or l == [[6]]:
        print(i + 1) # multiply manually afterwards

