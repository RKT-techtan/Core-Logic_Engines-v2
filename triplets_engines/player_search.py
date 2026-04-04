players = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Zelda"]
target = "Zelda"

low = 0
high = len(players) - 1

while low <= high:
    mid = (low + high)  // 2
    print(f"Checking: {players[mid]}")

    if players[mid] == target:
        print(f"Found {target} at index {mid}!")
        break
    elif players[mid] < target:
        low = mid + 1
    else:
        high = mid - 1