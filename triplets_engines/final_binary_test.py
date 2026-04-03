data = [10, 20, 30, 40, 50, 60, 70]
target = 60

low = 0
high = len(data) # Error

while low < high: # Error
    mid = (low + high) / 2 # Error

    if data[mid] == target:
        print("Found it!")
        break
    elif data[mid] < target:
        low = mid
    else:
        high = mid