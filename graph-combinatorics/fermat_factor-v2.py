import math

# We add a safety cap parameter: max_iterations
def fermat_factor_safe(n, max_iterations=10000):
    x = math.isqrt(n) + 1
    
    # Step 1: Initialize an iteration tracker
    loop_count = 0
    
    while True:
        # Step 2: Track how many times this loop has spun
        loop_count += 1
        
        # Step 3: Trigger the Circuit Breaker if we exceed our safety budget
        if loop_count > max_iterations:
            print(f"[SYSTEM ALERT] Iteration budget limit of {max_iterations} breached! Failing fast.")
            return None
            
        y_square = x**2 - n
        
        if y_square < 0:
            x = x + 1
            continue
            
        y = math.isqrt(y_square)
        
        if y**2 == y_square:
            return int(x - y), int(x + y)
            
        x = x + 1
        result = fermat_factor_safe(1000000000000000003, max_iterations=10000)
        print(f"Result: {result}")