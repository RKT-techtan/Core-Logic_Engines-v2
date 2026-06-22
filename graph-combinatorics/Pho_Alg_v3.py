import math

def is_prime_fast(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    
    for i in range(5, math.isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def enterprise_factorizer(n):
    print(f"[SYSTEM] Analyzing payload: {n}")
    
    if is_prime_fast(n):
        print(f"[GUARD RAIL] Payload {n} is PRIME. Aborting factorization to save CPU.")
        return n, 1
        
    print("[ENGINE] Payload is composite. Launching Pollard's Rho Engine...")
    
    def f(val, n):
        return (val**2 + 1) % n

    x, y, d = 2, 2, 1
    while d == 1:
        x = f(x, n)
        y = f(f(y, n), n)
        d = math.gcd(abs(x - y), n)
        
    return d, n // d

print(enterprise_factorizer(1000000007))
print(enterprise_factorizer(8051))