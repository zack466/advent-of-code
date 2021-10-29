from copy import deepcopy
from pprint import pprint

with open("input_day11", 'r') as f:
    l = list(map(lambda x: list(x.rstrip()), f.readlines()))

#print(l)

# def new_char(arr, i, j):
#     rows = len(arr)
#     cols = len(arr[0])
#     if arr[i][j] == '.':
#         return '.'
#     adj = []
#     for offset in list(zip([-1,0,1,-1,1,-1,0,1], [-1,-1,-1,0,0,1,1,1])):
#         new_i = i + offset[0]
#         new_j = j + offset[1]
#         if 0 <= new_i < rows and 0 <= new_j < cols:
#             adj.append(arr[new_i][new_j])
#     if arr[i][j] == 'L':
#         if all(map(lambda x: x != '#', adj)):
#             return '#'
#         else:
#             return 'L'
#     else:
#         if list(map(lambda x: x == '#', adj)).count(True) >= 4:
#             return 'L'
#         else:
#             return '#'

# # print(new_char(l, 0, 0))
# counter = 0
# while True:
#     a = deepcopy(l)
#     # pprint(a)
#     for i in range(len(l)):
#         for j in range(len(l[0])):
#             a[i][j] = new_char(l, i, j)
#     counter += 1
#     if a == l:
#         print(sum([r.count('#') for r in a]))
#         break
#     else:
#         l = a

def new_char(arr, i, j):
    rows = len(arr)
    cols = len(arr[0])
    if arr[i][j] == '.':
        return '.'
    adj = []
    for offset in list(zip([-1,0,1,-1,1,-1,0,1], [-1,-1,-1,0,0,1,1,1])):
        new_i = i + offset[0]
        new_j = j + offset[1]
        while 0 <= new_i < rows and 0 <= new_j < cols:
            adj.append(arr[new_i][new_j])
            if arr[new_i][new_j] != '.':
                break
            else:
                pass
            new_i += offset[0]
            new_j += offset[1]
    if arr[i][j] == 'L':
        # if none visible are occupied
        if all(map(lambda x: x != '#', adj)):
            return '#'
        else:
            return 'L'
    else:
        if list(map(lambda x: x == '#', adj)).count(True) >= 5:
            return 'L'
        else:
            return '#'

# print(new_char(l, 0, 0))
counter = 0
while True:
    a = deepcopy(l)
    # pprint(a)
    for i in range(len(l)):
        for j in range(len(l[0])):
            a[i][j] = new_char(l, i, j)
    counter += 1
    if a == l:
        print(sum([r.count('#') for r in a]))
        break
    else:
        l = a
