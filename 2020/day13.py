# part 1
# with open("input_day13", 'r') as f:
#     lines = f.readlines()
#     time = int(lines[0])
#     buses = list(map(int, filter(lambda x: x!='x', lines[1].split(','))))
# mintime = 9999
# minbus = -1
# print(buses)
# for bus in buses:
#     if bus - (time % bus) < mintime:
#         mintime = bus - (time % bus)
#         minbus = bus

# print(mintime * minbus)

# part 2
with open("input_day13", 'r') as f:
    lines = f.readlines()
    buses = lines[1].split(',')

for i, bus in enumerate(buses):
    if bus != 'x':
        print(i, bus)
    # use ChineseRemainderTheorem.jl from https://github.com/zack466/ChineseRemainderTheorem.jl
