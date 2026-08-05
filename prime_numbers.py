def get_prime_factors(n):
    factors = []

    d = 2
    temp = n

    while d * d <= temp:
        while temp % d == 0: