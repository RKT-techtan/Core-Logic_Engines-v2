# Dataset: Target 1000
data = [100, 100, 400, 200, 300, 500, 200, 200]
data.sort() # O(n log n)

for i in range(len(data)):
    # Prevents unnessecary repetetions
    if i > 0 and data[i] == data[i - 1]:
        continue
    Left = i + 1
    Right = len(data) - 1
    
    while Left < Right:
        current_sum = data[i] + data[Left] + data[Right]
        if current_sum == 1000:
            print(f"Found: {data[i]}, {data[Left]}, {data[Right]}")

            # Prevents duplicate data collions
            while Left < Right and data[Left] == data[Left + 1]:
                Left += 1
            while Left < Right and data[Right] == data[Right - 1]:
                Right -= 1
            break
        elif current_sum < 1000:
            Left += 1
        else:
            Right -= 1