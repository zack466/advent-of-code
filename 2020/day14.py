import re
from copy import deepcopy
from pprint import pprint
with open("input_day14", 'r') as f:
    lines = f.readlines()

reg_mask = re.compile("mask = ([X01]{36})")
reg_arr = re.compile("mem\\[(\\d+)\\] = (\\d+)")
mem = {}

# part 1
# def get_val(mask, val):
#     for i, c in enumerate(mask[::-1]):
#         if c == 'X':
#             pass
#         elif c == '1':
#             val |= (1 << i)
#         elif c == '0':
#             val &= ~(1 << i)
#     return val

# for i, line in enumerate(lines):
#     if r := reg_mask.match(line):
#         mask = r.group(1)
#     else:
#         r = reg_arr.match(line)
#         idx, val = r.group(1), r.group(2)
#         mem[idx] = get_val(mask, int(val))

# print(sum(mem.values()))

# part 2
def base2(num):
    ls = []
    while num > 0:
        ls.append(str(num % 2))
        num //= 2
    return ['0'] * (36 - len(ls)) + list(reversed(ls))

def base10(num):
    total = 0
    for i, c in enumerate(num[::-1]):
        total += int(c) << i
    return total

def generate_nums(bits):
    # print(bits)
    stack = [bits]
    # print(stack)
    for i in range(bits.count('X')):
        new_stack = []
        for arr in stack:
            temp = arr[::-1]
            idx = temp.index('X')
            temp[idx] = '0'
            new_stack.append(deepcopy(temp[::-1]))
            temp[idx] = '1'
            new_stack.append(deepcopy(temp[::-1]))
        stack = new_stack
    return stack

def get_val(mask, val):
    bits = base2(val)
    for i, c in enumerate(mask):
        if c == 'X':
            bits[i] = 'X'
        elif c == '1':
            bits[i] = '1'
    return generate_nums(bits)   

for i, line in enumerate(lines):
    if r := reg_mask.match(line):
        mask = r.group(1)
    else:
        r = reg_arr.match(line)
        idx, val = r.group(1), r.group(2)
        idxs = get_val(mask, int(idx))
        for j in idxs:
            mem[base10(j)] = val

# print(mem)
print(sum(map(int, mem.values())))

