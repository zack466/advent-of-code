from typing import Dict

with open("day7.in", 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

root = {}
root[".."] = root
pwd = root

i = 0
while i < len(lines):
    toks = lines[i].split(" ")
    if toks[0] == "$":
        # parse command
        if toks[1] == "cd":
            dir = toks[2]
            if dir == "/":
                pwd = root
            else:
                pwd = pwd[dir]
        elif toks[1] == "ls":
            while i+1 < len(lines) and lines[i+1][0] != "$":
                i += 1
                toks = lines[i].split(" ")
                if toks[0] == "dir":
                    name = toks[1]
                    new_dir = {}
                    pwd[name] = new_dir
                    new_dir[".."] = pwd
                else:
                    name = toks[1]
                    pwd[name] = int(toks[0])
    i += 1

total_total = 0
best_size = 1e10
root_size = None

def size(dir: Dict):
    total = 0
    for k in dir.keys():
        if k == "..":
            continue
        if isinstance(dir[k], int):
            total += dir[k]
        else:
            total += size(dir[k])
    if total <= 100000:
        global total_total;
        total_total += total
    global root_size
    global best_size
    if root_size is not None:
        if total + 28390426 >= 30000000:
            if total < best_size:
                best_size = total
    return total

root_size = size(root)
print(root_size)
print(total_total)

size(root)
print(best_size)
