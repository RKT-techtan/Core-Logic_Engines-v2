import math
def optimized_trial_division(n):
    factors = []

    for i in range(n, math.isqrt(n) + 1):
        if n % i == 0:
            while n % i == 0:
                factors.append(i)
                n //= i
    if n > 1:
        factors.append
    return factors
print(optimized_trial_division(15))