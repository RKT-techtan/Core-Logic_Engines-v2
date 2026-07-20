import random

def miller_rabin(n, k=5):

    # Step 1
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False  # Evens are handled instantly

    # Step 2
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    # Step 3
    for _ in range(k):
        a = random.randint(2, n - 2)
        
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
            
        is_composite = True
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                is_composite = False
                break
                
            if x == 1:
                break
                
        if is_composite:
            return False

    return True
print("Is 1000000007 prime?", miller_rabin(1000000007))
print("Is 8051 prime?", miller_rabin(8051))
