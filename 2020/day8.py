with open('input', 'r') as f:
    lines = f.readlines()

def parse(line):
    ins = line.split(' ')[0]
    arg = int(line.split(' ')[1])
    return ins, arg

for i,line in enumerate(lines):
    lines[i] = i, *parse(lines[i])

line_number = 0
acc = 0
seen = set()
# part 1
# while True:
#     print(line_number, acc)
#     if line_number in seen:
#         print(acc)
#         break
#     seen.add(line_number)
#     _, ins, arg = lines[line_number]
#     if ins == 'acc':
#         acc += arg
#         line_number += 1
#     elif ins == 'jmp':
#         line_number = line_number + arg
#     else:
#         line_number += 1

# part 2
def test():
    line_number = 0
    acc = 0
    seen = set()
    while line_number != len(lines):
        # print(line_number, acc)
        if line_number in seen:
            return False, 0
        seen.add(line_number)
        _, ins, arg = lines[line_number]
        if ins == 'acc':
            acc += arg
            line_number += 1
        elif ins == 'jmp':
            line_number = line_number + arg
        else:
            line_number += 1
    return True, acc

for i in range(len(lines)):
    # just brute force each jmp/nop
    if lines[i][1] == 'nop':
        print(f'replacing {i}')
        lines[i] = lines[i][0], 'jmp', lines[i][2]
        tf, n = test()
        if tf:
            print(n)
            break
        else:
            lines[i] = lines[i][0], 'nop', lines[i][2]
    elif lines[i][1] == 'jmp':
        print(f'replacing {i}')
        lines[i] = lines[i][0], 'nop', lines[i][2]
        tf, n = test()
        if tf:
            print(n)
            break
        else:
            lines[i] = lines[i][0], 'jmp', lines[i][2]
