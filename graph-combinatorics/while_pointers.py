nums = [2, 4, 5, 7, 10, 12]
target = 0

left = 0
right = len(nums) - 1

while left < right:
    current_sum = nums[left] + nums[right]

    if current_sum == target:
        return [nums[left], nums[right]]
    
    elif current_sum < target:
        left += 1
    else:
        right -= 1