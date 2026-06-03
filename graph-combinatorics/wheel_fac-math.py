def wheel_factorization(n):
    # Basic primes
    for base_prime in [2, 3, 5]:
        while n % base_prime == 0:
            print(base_prime)
            # Shrinking number till completely divisible
            n //= base_prime
            
            # Wheel factorization basic order
            gaps = [4, 2, 4, 2, 4, 6, 2, 6]
            i = 0
            factor = 7

            # Get the square root
            while factor * factor <= n:
                while n % factor == 0:
                    print(factor)
                    #Shrinking number till completely divisible
                    n //= factor

                    # Move to next number and save in lists
                    factor += gaps[i]
                    i = (i + 1) % 8

                # A just in case handle of left over prime if it exists
                if n > 1:
                    return(n)
print(wheel_factorization(200))