import time

def quadratic_test(n):
    print(f"Testing Quadratic with n = {n}...")
    start = time.time()
    
    for i in range(n):
        for j in range(n):
            pass
            
    end = time.time()
    print(f"Time taken: {end - start:.4f} seconds")

quadratic_test(1000)
quadratic_test(10000)
quadratic_test(50000)