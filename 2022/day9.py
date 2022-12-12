with open("day9.in", 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

H_x = 0
H_y = 0
T_x, T_y = 0, 0

# def adj():
#     return abs(H_x - T_x) <= 1 and abs(H_y - T_y) <= 1

# positions = set()
# positions.add((0, 0))

# for l in lines:
#     direction = l[0] # L, D, R, U
#     num = int(l[2:])
#     for _ in range(num):
#         if direction == "L":
#             H_x -= 1
#         elif direction == "R":
#             H_x += 1
#         elif direction == "U":
#             H_y += 1
#         elif direction == "D":
#             H_y -= 1
#         # update T
#         if not adj():
#             if H_x > T_x and H_y == T_y:
#                 T_x += 1
#             elif H_x < T_x and H_y == T_y:
#                 T_x -= 1
#             elif H_y > T_y and H_x == T_x:
#                 T_y += 1
#             elif H_y < T_y and H_x == T_x:
#                 T_y -= 1
#             elif H_x > T_x and H_y > T_y:
#                 T_x += 1
#                 T_y += 1
#             elif H_x > T_x and H_y < T_y:
#                 T_x += 1
#                 T_y -= 1
#             elif H_x < T_x and H_y > T_y:
#                 T_x -= 1
#                 T_y += 1
#             elif H_x < T_x and H_y < T_y:
#                 T_x -= 1
#                 T_y -= 1
#         positions.add((T_x, T_y))

# print(len(positions))

def adj(H_x, H_y, T_x, T_y):
    return abs(H_x - T_x) <= 1 and abs(H_y - T_y) <= 1

positions = set()
positions.add((0, 0))

Hs = [[0, 0] for _ in range(10)]
for l in lines:
    direction = l[0] # L, D, R, U
    num = int(l[2:])
    for _ in range(num):
        if direction == "L":
            Hs[0][0] -= 1
        elif direction == "R":
            Hs[0][0] += 1
        elif direction == "U":
            Hs[0][1] += 1
        elif direction == "D":
            Hs[0][1] -= 1
        # update T
        for i in range(1, 10):
            T_x, T_y = Hs[i]
            H_x, H_y = Hs[i-1]
            if not adj(H_x, H_y, T_x, T_y):
                if H_x > T_x and H_y == T_y:
                    Hs[i][0] += 1
                elif H_x < T_x and H_y == T_y:
                    Hs[i][0] -= 1
                elif H_y > T_y and H_x == T_x:
                    Hs[i][1] += 1
                elif H_y < T_y and H_x == T_x:
                    Hs[i][1] -= 1
                elif H_x > T_x and H_y > T_y:
                    Hs[i][0] += 1
                    Hs[i][1] += 1
                elif H_x > T_x and H_y < T_y:
                    Hs[i][0] += 1
                    Hs[i][1] -= 1
                elif H_x < T_x and H_y > T_y:
                    Hs[i][0] -= 1
                    Hs[i][1] += 1
                elif H_x < T_x and H_y < T_y:
                    Hs[i][0] -= 1
                    Hs[i][1] -= 1
            positions.add((Hs[9][0], Hs[9][1]))

print(len(positions))
