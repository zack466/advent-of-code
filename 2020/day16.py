import re
import functools
from itertools import permutations
from tqdm import tqdm

rule_regex = re.compile("\\w+(?: \\w+)?: (\\d+)-(\\d+) or (\\d+)-(\\d+)")
ticket_regex = re.compile("(\\d+)") # use findall

def parse_rule(line):
    a, b, c, d = list(map(int, rule_regex.search(line).groups()))
    return a, b, c, d

def parse_ticket(line):
    return tuple(map(int, ticket_regex.findall(line)))

with open("input_day16", 'r') as f:
    lines = f.readlines()

rules = []
total = 0 
successful = []


def error_rate(nums):
    total = 0
    # print(nums)
    for num in nums:
        valid = False
        for rule in rules:
            if (rule[0] <= num <= rule[1] or rule[2] <= num <= rule[3]):
                valid = True
                break
        if not valid:
            total += num
    return total

# for part 1
def check(nums, rule_order):
    tf = True
    for i, num in enumerate(nums):
        r = rules[rule_order[i]]
        if r[0] <= num <= r[1] or r[2] <= num <= r[3]:
            pass
        else:
            tf = False
            break
    return tf


for i in range(20):
    rules.append(parse_rule(lines[i]))

ans = 0
for i in tqdm(range(25, len(lines))):
    total += 1
    t = parse_ticket(lines[i])
    e = error_rate(t)
    if e == 0:
        pass

# print(test(parse_ticket(lines[25]), [False for _ in range(20)], 0))
# print(successful, total)
# print(ans)
