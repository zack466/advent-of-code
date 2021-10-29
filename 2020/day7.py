import re
container = re.compile("([a-z]+ [a-z]+) bag") # re.match
contains = re.compile("(\\d) ([a-z]+ [a-z]+) bag") # re.findall

with open("input", 'r') as f:
    lines = f.readlines()

def parse(line):
    color = re.match(container, line)
    colors = re.findall(contains, line)
    return color.group(1), colors

# part 1
# G = {} # directed graph
# for line in lines:
#     color, colors = parse(line)
#     colors = [tup[1] for tup in colors]
#     for c in colors: # G[A] = [B, C] means B and C are able to contain A
#         if c not in G.keys():
#             G[c] = [color]
#         else:
#             G[c].append(color)

# seen = set()
# def dfs(col):
#     if col in seen:
#         return
#     seen.add(col)
#     for color in G[col]:
#         if color in G.keys():
#             dfs(color)
#         seen.add(color)

# dfs("shiny gold")
# print(G["shiny gold"])
# print(len(seen))
# > 188, < 301
# ITS 1 LESS BC I INCLuDED SHINY GOLD facepalm

# part 2
G = {}
for line in lines:
    color, colors = parse(line)
    G[color] = colors # G[A] = [B, C] means A has to include B and C

seen = {}
def num_bags(col):
    # returns the number of bags included in a color
    total = 0
    if col not in G.keys():
        return 1
    for num, color in G[col]:
        total += int(num) * (1 + num_bags(color))
    return total

print(num_bags("shiny gold"))
