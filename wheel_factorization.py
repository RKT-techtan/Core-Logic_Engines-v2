def wheel_factorize(n):
    #Handling the basic primes.
    for base_prime in [2, 3, 5]:
        while n % base_prime == 0:
            print(base_prime)
            n //= base_prime

            # Wheel factorization comes into play.
            gaps = [4, 2, 4, 2, 4, 6, 2, 6]
            i = 0
            factor = 7 # Starter number.

            # Loop repetition for the numbers.
            while factor * factor <= n:
                while n % factor == 0:
                    print(factor)
                    n //= factor

                    # Spinning the wheel back
                    factor += gaps[i]
                    i = (i + 1) % 8

                    #Handling the unknown left numbers
                    if n > 1:
                        print(n)
print(wheel_factorize(280))