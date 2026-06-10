import math

def fermat_fact(n, max_iterations=1000):
    # Solving the starting point
    # x starts at sqrt of n (greater than or equal to n)
    x = math.isqrt(n) + 1
    iterations = 0
    while True:
        iterations += 1
        # Check just to be sure if y is a perfect square
        if iterations > max_iterations:
            print(f"[System alert] Limit reached!")
            return None
        y_square = x**2 - n
        
        if y_square < 0:
            x = x + 1
            continue
        y = math.isqrt(y_square)

        if y**2 == y_square:
            return int(x - y), int(y + y)
        x = x + 1
result = fermat_fact(1000000000000000003, max_iterations=10000)
print(f"Result: {result}")