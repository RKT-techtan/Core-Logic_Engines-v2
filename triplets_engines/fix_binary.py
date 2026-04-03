data = [10, 20, 30, 40, 50, 60, 70]
target = 60

low = 0
high = len(data) - 1 # ERROR

while low <= high: # ERROR
    mid = (low + high) // 2 # ERROr
    
    if data[mid] == target:
        print("Found it!")
        break
    elif data[mid] < target:
        low = mid + 1
    else:
        high = mid - 1