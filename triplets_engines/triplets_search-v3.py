# Dataset: Target 1000
data = [-1, 0, 1, 2, -1, -4]
# Target: 0

data.sort() # O(n log n)

# Changed 1000 to target that is equal to 1000.
target = 0

for i in range(len(data)):
    # Prevents unnessecary repetetions
    if i > 0 and data[i] == data[i - 1]:
        continue
    Left = i + 1
    Right = len(data) - 1
    
    while Left < Right:
        current_sum = data[i] + data[Left] + data[Right]
        if current_sum == target:
            print(f"Found: {data[i]}, {data[Left]}, {data[Right]}")

            # Prevents duplicate data collions
            while Left < Right and data[Left] == data[Left + 1]:
                Left += 1
            while Left < Right and data[Right] == data[Right - 1]:
                Right -= 1
            # (Break) removed (Left and right added)
            Left += 1
            Right -= 1

        elif current_sum < target:
            Left += 1
        else:
            Right -= 1
