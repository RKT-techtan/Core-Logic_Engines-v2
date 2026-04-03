data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
work_done = 0

for i in data:
    for j in data:
        work_done += 1
        print(f"Checking {i} and {j}...")
        print(f"Total items: {len(data)}")
        print(f"Total work done: {work_done}")