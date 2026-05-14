def fast_gcd(a, b): #def fast_gcd(a, b):
    while b != 0: #while b != 0:
        a, b = b, a % b #a, b = b, a % b
        return a #return a
    print(fast_gcd(5, 100))

def fast_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print(fast_gcd(5, 100))