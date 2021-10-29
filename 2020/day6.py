with open("input", 'r') as f:
    lines = f.read().split("\n\n")

count = 0
for line in lines:
    ls = line.split('\n')
    letters = {}
    for c in line:
        if c != ' ':
            if c not in letters.keys():
                letters[c] = 1
            else:
                letters[c] += 1
    for c in letters.keys():
        if letters[c] == len(ls):
            count += 1
print(count)