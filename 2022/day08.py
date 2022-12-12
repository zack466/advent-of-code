with open("day08.in", 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    lines = list(map(lambda x: list(map(int, x)), lines))
    N = len(lines)

total = 0

# for i in range(N):
#     for j in range(N):
#         if i == 0 or j == 0 or i == N - 1 or j == N - 1:
#             total += 1
#             continue
#         if lines[i][j] > max(lines[i][:j]) or lines[i][j] > max(lines[i][j+1:]):
#             total += 1
#             continue
#         colbefore = [lines[z][j] for z in range(i)]
#         colafter = [lines[z][j] for z in range(i+1, N)]
#         if lines[i][j] > max(colbefore) or lines[i][j] > max(colafter):
#             total += 1
#             continue

# print(total)

best = 0

for i in range(N):
    for j in range(N):
        score_left = 1
        left_idx = j-1
        while left_idx >= 0 and lines[i][left_idx] < lines[i][j]:
            left_idx -= 1
            score_left += 1
        if left_idx < 0:
            score_left -= 1

        score_right = 1
        right_idx = j+1
        while right_idx < N and lines[i][right_idx] < lines[i][j]:
            right_idx += 1
            score_right += 1
        if right_idx == N:
            score_right -= 1

        score_up = 1
        up_idx = i-1
        while up_idx >= 0 and lines[up_idx][j] < lines[i][j]:
            up_idx -= 1
            score_up += 1
        if up_idx < 0:
            score_up -= 1

        score_down = 1
        down_idx = i+1
        while down_idx < N and lines[down_idx][j] < lines[i][j]:
            down_idx += 1
            score_down += 1
        if down_idx == N:
            score_down -= 1

        score = score_left * score_right * score_up * score_down
        if score > best:
            # print(i, j)
            # print(score_left, score_right, score_up, score_down)
            best = score

print(best)
