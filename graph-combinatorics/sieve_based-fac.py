def create_spf_sieve(n):

    # spf[i] = i code
    spf = [i for i in range(n + 1)]
    
    # Loop and start from 2
    for i in range(2, n + 1):
        if spf[i] == i:
            for multiple in range(i * 2, n + 1, i):
                # Overwrite if it hasnt been touched yet
                if spf[multiple] == multiple:
                    spf[multiple] = i
    return spf
#print(create_spf_sieve(200))

# Breaking the numbers into prime factors
def sieve_factorize(number, spf_array):
    factors = []

    # Keep looking for the number and break it down till one.
    while number > 1:
        # smallest prime factor starts here
        factor = spf_array[number]

        # Add it to the rest of the factors
        factors.append(factor)

        # Keep on shrinking the number
        number = number // factor
    return factors

my_spf_database = create_spf_sieve(900)
print(sieve_factorize(12, my_spf_database))
print(sieve_factorize(45, my_spf_database))
print(sieve_factorize(89, my_spf_database))