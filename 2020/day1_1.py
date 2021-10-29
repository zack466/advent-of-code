with open("day1_input", "r") as f:
    nums = list(map(int, f.readlines()))
# two sum
# seen = set()
# for num in nums:
#     for x in seen:
#         if x == 2020 - num:
#             print(num * x)
#             break
#     seen.add(num)

# three sum
for num1 in nums:
    if num1 > 2020:
        pass
    target = 2020 - num1
    seen = set()
    for num2 in nums:
        if num1 + num2 > 2020:
            break
        for x in seen:
            if num2 + x == target:
                print("found")
            print(num1, num2, x)
        seen.add(num2)
