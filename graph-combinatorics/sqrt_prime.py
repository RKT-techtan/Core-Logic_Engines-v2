def optimized_prime_factors(n):
    factors = []
    i = 2
    
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 1
        
    if n > 1:
        factors.append(n)
        
    return factors
print(optimized_prime_factors(34))