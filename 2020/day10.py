with open("input_day10", 'r') as f:
    nums = list(map(int, f.readlines()))

# part 1
# nums.append(0)
# nums.append(max(nums) + 3)
# nums.sort()
# differences = {}
# for i in range(len(nums)-1):
#     diff = nums[i+1] - nums[i]
#     if diff in differences.keys():
#         differences[diff] += 1
#     else:
#         differences[diff] = 1

# print(differences)

# part 2
import sys
sys.setrecursionlimit(5000)

nums.append(0)
nums.sort()
dp = {}
nmax = nums[-1]

def num_ways(idx):
    if idx == len(nums)-1:
        return 1
    if idx in dp.keys():
        return dp[idx]
    total = 0
    for i in range(1,4):
        if idx + i < len(nums):
            if 1 <= nums[idx+i] - nums[idx] <= 3:
                total += num_ways(idx+i)
        elif idx + i == len(nums):
            total += num_ways(idx+i)
    dp[idx] = total
    return total


print(num_ways(0))
