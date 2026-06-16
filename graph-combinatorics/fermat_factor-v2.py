import math

#def fermat_factor(n):
def fermat_factor(n):
    x = math.isqrt(n) + 1
    while True:
        y_square = x**2 - n
        y = math.isqrt(y_square)
        if y**2 == y_square:
            factor1 = x - n
            factor2 = x + n
            return factor1, factor2
        x = x + 1
print(fermat_factor(65))