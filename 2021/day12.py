import re
from copy import deepcopy
from collections import defaultdict

adj = re.compile("([a-zA-Z]+)-([a-zA-Z]+)")

G = dict()

with open("day12.in", 'r') as f:
    lines = f.readlines()
    for line in lines:
        match = adj.match(line)
        a, b = match.groups()
        if a not in G.keys():
            G[a] = set()
        if b not in G.keys():
            G[b] = set()
        G[a].add(b)
        G[b].add(a)

def isLarge(x):
    return x.isupper()

def isSmall(x):
    return x.islower()

# assumes that a large cave is never adjacent to another large cave
def dfs(node, searched, curr_path, ret):
    neighbors = G[node]
    for n in neighbors:
        if n == "end":
            ret.append(deepcopy(curr_path))
            continue
        if n == "start":
            continue
        if isSmall(n) and searched[n]:
            continue
        else:
            if isSmall(n):
                searched[n] = True
            curr_path.append(n)
            dfs(n, searched, curr_path, ret)
            curr_path.pop()
            if isSmall(n):
                searched[n] = False
    return ret

def solA():
    ret = []
    searched = defaultdict(lambda: False)
    dfs('start', searched, [], ret)
    print(len(ret))

def dfsB(node, searched, curr_path, ret, special):
    neighbors = G[node]
    for n in neighbors:
        if n == "end":
            ret.add("".join(curr_path))
            continue
        if n == "start":
            continue
        if n != special and isSmall(n) and searched[n] == 1:
            continue
        if n == special and searched[n] == 2:
            continue
        else:
            if isSmall(n):
                searched[n] += 1
            curr_path.append(n)
            dfsB(n, searched, curr_path, ret, special)
            curr_path.pop()
            if isSmall(n):
                searched[n] -= 1
    return ret

def solB():
    ret = set()
    searched = defaultdict(lambda: False)
    for k in G.keys():
        if k == "start" or k == "end":
            continue
        if not isSmall(k):
            continue
        dfsB('start', searched, [], ret, k)
    print(len(ret))

solB()
