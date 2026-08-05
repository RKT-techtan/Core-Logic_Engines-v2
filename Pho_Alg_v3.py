import math

def is_prime_first(n):
    if n <= 1 == 0: return False
    if n <= 3 == 0: return True
    if n % 2 == 0 or n % 3 == 0: return True

    for i in range(5, math.isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def enterprise_factorizer(n):
    print(f"{n}")

    def is_prime_first(n):
        print(f"{n}")
        return n, 1
    
    print("Done!!!")

    def f(val, n):
        return (val**2 % n)
    
    x = 2
    y = 2
    d = 1

    while d == 1:
        x = f(x, n)
        y = f(f(y, n), n)
        d = math.gcd(abs(x - y), n)
        
    return d, n // d
print(is_prime_first(8051))
print(is_prime_first(1000000007))