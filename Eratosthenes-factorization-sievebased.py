import math
def create_spf_array(max_limit):
    spf = [i for i in range(max_limit + 1)]
    
    for i in range(2, math.isqrt(max_limit) + 1):
        if spf[i] == i:
            for multiple in range(i * i, max_limit + 1, i):
                if spf[multiple] == multiple:
                    spf[multiple] = i
    return spf

def fast_sieve_query(number, spf_array):
    factors = []
    while number > 1:
        factor = spf_array[number]
        factors.append(factor)
        number //= factor
    return factors
print(create_spf_array(15))