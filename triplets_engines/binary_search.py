data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 70

low = 0
high = len(data) - 1

while low <= high:
    mid = (low + high) // 2
    
    if data[mid] == target:
        print(f"Found {target} at index {mid}")
        break
    elif data[mid] < target:
        low = mid + 1
    else:
        high = mid - 1