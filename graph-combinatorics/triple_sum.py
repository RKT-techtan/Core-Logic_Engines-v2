nums = [-2, -2, 1, 1]
target = 0
left = 0
right = len(nums) - 1

for i in range (len(nums)):
    if i > 0 and nums[i] == nums[i-1]:
        continue

if target < 0:
    left += 1

    if target > 0:
        right -+ 1

    else:
        print("Found a trio!")