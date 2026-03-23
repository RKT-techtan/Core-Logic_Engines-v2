# Dataset: Target 1000
data = [100, 400, 200, 300, 500]
data.sort() # O(n log n)

for i in range(len(data)):
    Left = i + 1
    Right = len(data) - 1
    
    while Left < Right:
        current_sum = data[i] + data[Left] + data[Right]
        if current_sum == 1000:
            print(f"Found: {data[i]}, {data[Left]}, {data[Right]}")
            break
        elif current_sum < 1000:
            Left += 1
        else:
            Right -= 1
