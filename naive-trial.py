def naive_factors(n):
    factors = []
    for i in range(2, n):
        if n % i == 0:
            factors.append(i)
    return factors
#Likely to take so much time, code not built for this kind of large number
print(naive_factors(2000000000000))