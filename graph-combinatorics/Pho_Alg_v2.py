import math
def pollard_rho(n):
    if n % 2 == 0:
        return 2
    
    def f(val, n):
        return(val**2 + 1) % n

    x = 2
    y = 2
    d = 1
    
    while d == 1:
        x = f(x, n)
        y = f(f(y, n), n)
        
        d = math.gcd(abs(x - y), n)

    if d == n:

        return None
    return d
print(pollard_rho(8051))