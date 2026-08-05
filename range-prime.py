def naive_prime_factors(n):
    factors = []

    for i in range(2, n):
        if n % i == 0:
            factors.append(i)
    return factors
print(naive_prime_factors(12))