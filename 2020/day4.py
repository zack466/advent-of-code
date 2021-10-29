import re
lines = []
with open("input", "r") as f:
    s = f.read()
    lines = s.split("\n\n")
count = 0
# part 1
# regex = re.compile("([a-z]+):")
# for i, entry in enumerate(lines):
#     result = re.findall(regex,entry)
#     c = 0
#     for id in result:
#         if id != "cid":
#             c += 1
#     if c == 7:
#         count += 1

# part 2
patterns = [
    re.compile("byr:(\\d{4})"), # 1920 - 2002
    re.compile("iyr:(\\d{4})"), # 2010 - 2020
    re.compile("eyr:(\\d{4})"), # 2020 - 2030
    re.compile("hgt:(\\d+)(cm|in)"), # 150-193 cm, 59-76 in
    re.compile("hcl:#[a-f0-9]{6}"),
    re.compile("ecl:(amb|blu|brn|gry|grn|hzl|oth)"),
    re.compile("pid:\\d{9}")
]

for i,entry in enumerate(lines):
    data = list(map(lambda a: re.findall(a, entry), patterns))
    flag = True
    if not (len(data[0]) != 0 and 1920 <= int(data[0][0]) <= 2002):
        flag = False
        #print("set false 0")
    if not (len(data[1]) != 0 and 2010 <= int(data[1][0]) <= 2020):
        flag = False
        ##print("set false 1")
    if not (len(data[2]) != 0 and 2020 <= int(data[2][0]) <= 2030):
        flag = False
        #print("set false 2")
    if len(data[3]) == 0:
        flag = False
        #print("set false 3")
    elif len(data[3][0]) == 2:
        if data[3][0][1] == 'cm':
            if not (150 <= int(data[3][0][0]) <=193):
                flag = False
                #print("set false cm")
        elif data[3][0][1] == 'in':
            if not (59 <= int(data[3][0][0]) <=76):
                flag = False
                #print("set false in")
        else:
            flag = False
    else:
        flag = False
        #print("set false 3")
    if not (len(data[4]) != 0):
        flag = False
        #print("set false 4")
    if not (len(data[5]) != 0):
        flag = False
        #print("set false 5")
    if not (len(data[6]) != 0):
        flag = False
        #print("set false 6")
    if flag:
        count += 1
        print(data)
    #print(data, flag)
print(count)
# count - 1