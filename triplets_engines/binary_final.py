data = [100, 200, 300, 400, 500, 600, 700]
target = 600

low = 0
high = len(data) - 1

while low <= high:
    mid = (low + high) // 2
    print(f"Checking index {mid}: {data[mid]}")
    if data[mid] == target:
        break
    elif data[mid] < target:
        low = mid + 1
    else:
        high = mid - 1