def find_prime_factors(n):
    factor = []
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            factor.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    return factor
print(find_prime_factors(28))