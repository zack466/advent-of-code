with open("day10.in", "r") as f:
    lines = map(lambda x: x.strip(), f.readlines())

matches = { ")": "(", "]": "[", "}": "{", ">": "<"}
score = {")": 3, "]": 57, "}": 1197, ">": 25137}
scoreB = {"(": 1, "[": 2, "{": 3, "<": 4}

def solA():
    total = 0
    for line in lines:
        stack = []
        i = 0
        while i < len(line):
            if line[i] in "]}>)" and len(stack) > 0:
                if stack[-1] == matches[line[i]]:
                    stack.pop()
                else:
                    total += score[line[i]]
                    break
            else:
                stack.append(line[i])
            i += 1
    print(total)

def solB():
    scores = []
    for line in lines:
        stack = []
        i = 0
        corrupt = False
        while i < len(line):
            if line[i] in "]}>)" and len(stack) > 0:
                if stack[-1] == matches[line[i]]:
                    stack.pop()
                else:
                    corrupt = True
                    break
            else:
                stack.append(line[i])
            i += 1
        if corrupt:
            continue
        total = 0
        for c in stack[::-1]:
            total *= 5
            total += scoreB[c]
        scores.append(total)
    scores.sort()
    print(scores[len(scores) // 2])

solB()
