import time

def count_test(n):
    print(f"Testing with n = {n}...")
    start = time.time()
    
    for i in range(n):
        pass
    
    end = time.time()
    print(f"Time taken: {end - start:.4f} seconds\n")

count_test(1000)
count_test(1000000)
count_test(100000000)