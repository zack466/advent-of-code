with open("input_day9", "r") as f:
    lines = f.readlines()

nums = dict()
sums = dict()


def dadd(d, num):
    if num in d.keys():
        d[num] += 1
    else:
        d[num] = 1


def dremove(d, num):
    if num in d.keys():
        if d[num] == 1:
            d.pop(num)
        else:
            d[num] -= 1


# part 1
# for i in range(26):
#     num = int(lines[i])
#     dadd(nums, num)

# # initial sums
# for i in nums.keys():
#     for j in nums.keys():
#         if i == j:
#             if nums[i] <= 1:
#                 continue
#         s = i + j
#         dadd(sums, s)

# # loop
# for i, line in enumerate(lines[26:]):
#     num = int(line)
#     if num in sums:
#         # remove 26th before, adjust sums
#         to_remove = int(lines[i-26])
#         dremove(nums, to_remove)
#         for n in nums:
#             dremove(sums, n+to_remove)
#         for n in nums:
#             dadd(sums, num + n)
#         dadd(nums, num)
#     else:
#         # 466456641
#         print(num)
#         break

# part 2
nlines = list(map(int, lines))
i = 0
j = 1
rsum = nlines[i] + nlines[j]
ans = 466456641
while i < j:
    if rsum == ans:
        print(min(nlines[i:j+1]) + max(nlines[i:j+1]))
        break
    elif rsum < ans:
        j += 1
        rsum += nlines[j]
    else:
        rsum -= nlines[i]
        i += 1
