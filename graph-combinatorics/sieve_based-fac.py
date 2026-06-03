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
print(create_spf_sieve(200))