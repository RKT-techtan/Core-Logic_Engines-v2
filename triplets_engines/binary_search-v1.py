data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 75

low = 0
high = len(data) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if data[mid] == target:
        print(f"Found at {mid}")
        found = True
        break
    elif data[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print(f"75 not found.")
    print(f"It should be between {data[high]} and {data[low]}")