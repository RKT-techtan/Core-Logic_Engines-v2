data = [10, 20, 30, 40, 50]
target = 40

low = 0
high = len(data) - 1

while low <= high:
    mid = (low + high) // 2

    if data[mid] == target:
        print(f"Found it at index {mid}!")
        break

    elif data[mid] < target:
        low = mid + 1

    else:
        high = mid - 1