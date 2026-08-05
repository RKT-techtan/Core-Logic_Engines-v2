def create_spf_sieve(n):
    spf = [i for i in range(n + 1)]
    
    for i in range(2, n + 1):
        if spf[i] == i:
            for multiple in range(i * 2, n + 1, i):
                if spf[multiple] == multiple:
                    spf[multiple] = i
    return spf
print(create_spf_sieve(15))

def sieve_factorize(number, spf_array):
    factors = []
    
    while number > 1:
        factor = spf_array[number]
        
        factors.append(factor)
        
        number = number // factor
        
    return factors
database = create_spf_sieve(15)
print(sieve_factorize(12, database))
print(sieve_factorize(13, database))