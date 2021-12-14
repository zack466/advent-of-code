import re
from collections import defaultdict

RULE = re.compile("([A-Z])([A-Z]) -> ([A-Z])")

def parse_rule(x):
    match = RULE.match(x)
    return (match.group(1), match.group(2), match.group(3))

with open("day14.in", 'r') as f:
    start, _, *end = f.readlines()
    start = start.strip()
    rules = list(map(parse_rule, end))

def step(p):
    new_p = []
    for i in range(len(p) - 1):
        new_p.append(p[i])
        for a, b, c in rules:
            if p[i] == a and p[i+1] == b:
                new_p.append(c)
    new_p.append(p[-1])
    return new_p

def minmax_count(p):
    minval, minkey = 9e15, ""
    maxval, maxkey = -1, ""
    for k in p.keys():
        if p[k] > maxval:
            maxval = p[k]
            maxkey = k
        if p[k] < minval:
            minval = p[k]
            minkey = k
    return minkey, minval, maxkey, maxval

def solA():
    curr = start
    for _ in range(10):
        curr = step(curr)

    chars = defaultdict(lambda: 0)
    for l in curr:
        chars[l] += 1

    minkey, minval, maxkey, maxval = minmax_count(chars)
    print(maxval - minval)

def smartstep(state):
    new_state = defaultdict(lambda: 0)
    for a, b, c in rules:
        if (a + b) in state.keys():
            n = state[a+b]
            new_state[a+c] += n
            new_state[c+b] += n
    return new_state

def solB():
    curr = defaultdict(lambda: 0)
    for i in range(len(start) - 1):
        curr[start[i:i+2]] += 1

    for _ in range(40):
        curr =  smartstep(curr)

    chars = defaultdict(lambda: 0)
    for k in curr.keys():
        # don't overcount!
        chars[k[0]] += curr[k]
    chars[start[-1]] += 1 # plus last char bc we kept the first char in each pair

    minkey, minval, maxkey, maxval = minmax_count(chars)
    print(maxval - minval)

solB()
