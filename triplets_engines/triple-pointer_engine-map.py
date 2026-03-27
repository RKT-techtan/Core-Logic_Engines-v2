data = [100, 200, 300, 400, 500]
target = 900

data.sort()

for i in range(len(data)):
    Left = i + 1
    Right = len(data) - 1
    
    while Left < Right:
        current_sum = data[i] + data[Left] + data[Right]
        
        if current_sum == target:
            print(f"Match Found: {data[i]}, {data[Left]}, {data[Right]}")
            Left += 1
            Right -= 1
        elif current_sum < target:
            Left += 1
        else:
            Right -= 1