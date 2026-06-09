import math

def fermat_factor(n):
    # Calculate starting value of X
    x = math.isqrt(n) + 1

    while True:
        # Calculate square of y potential
        y_square = x**2 - n
        # Check if square of y is a whole number
        y = math.sqrt(y_square)

        # Check if y is a whole interger
        if y % 1 == 0:

            # Now calculate the two factors
            factor1 = int(x - y)
            factor2 = int(x + y)
            return factor1, factor2
        x = x + 1
print(fermat_factor(1000000000000000003))