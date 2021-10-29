from pprint import pprint
from tqdm import tqdm

stack = [0,8,15,2,12,1,4] # 0,8,15,2,12,1,4
# part 1
def search_back(stack, target):
    i = len(stack) - 2
    while i >= 0:
        if stack[i] == target:
            return len(stack) -1 - i
        else:
            i -= 1
    return 0

def efficient_search(target, seen, total):
    if seen[target] != 0:
        tmp = seen[target]
        seen[target] = total - 1
        return total - 1 - tmp
    else:
        seen[target] = total - 1
        return 0

seen = [0 for _ in range(30000000)]
for i, x in enumerate(stack):
    seen[x] = i

# while len(stack) < 30000000: # 30,000,000
top = stack[-1]
total = len(stack)
for i in tqdm(range(30000000 - len(stack))):
    # stack.append(search_back(stack, top))
    top = efficient_search(top, seen, total)
    total += 1

# print(stack)
# print(stack[-1])
print(top)
