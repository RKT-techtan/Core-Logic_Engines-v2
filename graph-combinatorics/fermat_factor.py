# n = n^2 - y^2,
import math

def fermat_factor(n):
    # 1. Starting boundary for x,
    x = math.isqrt(n) + 1
    # 2. Search Loop,
    while True:
        # 3. Difference of y^2 = x^2 - n,
        y_square = x**2 - n
        y = math.isqrt(y_square)
        # 4. Verify if y is a clean whole number,
        if y**2 == y_square:
            factor1 = x - y
            factor2 = x + y
            return factor1, factor2
        # 5. If not a perfect square shift up,
        x = x + 1
# 6. Example outcome.
print(fermat_factor(65))