def fast_gcd(a, b):
    while b != 0:
        a, b = b, a % b
        return a
print(f"The gcd of 13 and 17 is: {fast_gcd(13, 17)}")