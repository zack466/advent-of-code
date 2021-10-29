with open("input_day12", 'r') as f:
    lines = f.readlines()

direction = 1 # N:0, E:1, S:2, W:3
x = 0
y = 0

def move(op, arg):
    global x
    global y
    if op == 'N':
        y += arg
    elif op == 'W':
        x -= arg
    elif op == 'S':
        y -= arg
    elif op == 'E':
        x += arg
# part 1
# for line in lines:
#     # print(x, y, direction)
#     op = line[0]
#     arg = int(line[1:])
#     # print(op, arg)
#     if op in "NESW":
#         move(op, arg)
#     elif op == 'F':
#         if direction == 0:
#             move("N", arg)
#         elif direction == 1:
#             move("E", arg)
#         elif direction == 2:
#             move("S", arg)
#         elif direction == 3:
#             move("W", arg)
#     elif op == 'R':
#         num = arg // 90
#         direction += num
#         direction %= 4
#     elif op == 'L':
#         num = arg // 90
#         direction -= num
#         direction %= 4
# print(abs(x) + abs(y))

actual_x = 0
actual_y = 0
x = 10
y = 1

def rotater(num):
    global x
    global y
    num = num % 4
    if num == 0:
        pass
    elif num == 1:
        x, y = y, -x
    elif num == 2:
        x, y = -x, -y
    elif num == 3:
        x, y = -y, x


def rotatel(num):
    global x
    global y
    num = num % 4
    if num == 0:
        pass
    elif num == 1:
        x, y = -y, x
    elif num == 2:
        x, y = -x, -y
    elif num == 3:
        x, y = y, -x


for i, line in enumerate(lines):
    # print(x, y, direction)
    op = line[0]
    arg = int(line[1:])
    print(op, arg)
    if op in "NESW":
        move(op, arg)
    elif op == 'F':
        actual_x += x * arg
        actual_y += y * arg
    elif op == 'R':
        num = arg // 90
        rotater(num)
    elif op == 'L':
        num = arg // 90
        rotatel(num)
    # print(actual_x, actual_y, '\t', x, y)
    # if i > 10:
    #     break
print(abs(actual_x) + abs(actual_y))
