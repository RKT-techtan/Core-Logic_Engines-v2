def find_slice(arr, target):
    left = 0
    current_sum = 0
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        while current_sum > target and left <= right:
            current_sum -= arr[left]
            left += 1
            
        if current_sum == target:
            return arr[left : right + 1]
            
    return "No slice found"

data = [1, 4, 2, 10, 2, 3, 1, 0, 20]
print(find_slice(data, 33))