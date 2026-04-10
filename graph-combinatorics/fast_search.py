import time

n = 100000000
target = 99999999

# Linear search - O(n) the slow way
def slow_search():
    start = time.time()
    for i in range(n):
        if i == target:
            break
    print(f"Slow Search: {time.time() - start:.4f} seconds")

# Constant search - O(1) the faster way
def fast_search():
    start = time.time()
    if target < n: 
        pass 
    print(f"Fast Search: {time.time() - start:.8f} seconds")

slow_search()
fast_search()