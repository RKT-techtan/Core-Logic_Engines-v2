def sieve_of_erastothenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    p = 2
    while p * p <= limit:
        if is_prime[p] == True:
            for multpile in range(p * p, limit + 1, p):
                is_prime[multpile] = False
        p += 1
    return is_prime
print(sieve_of_erastothenes(10))