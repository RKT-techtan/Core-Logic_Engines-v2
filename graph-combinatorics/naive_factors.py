def naive_prime_factors(n):
    factors = []
    
    for i in range(2, n):
        while n % i == 0:
            factors.append(i)
            n = n // i
    return factors
print (naive_prime_factors(28))