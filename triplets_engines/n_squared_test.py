data = [1, 2, 3, 4, 5]
target = 9

for i in data:
    for j in data:
        if i + j == target:
            print(f"Found: {i} + {j}")