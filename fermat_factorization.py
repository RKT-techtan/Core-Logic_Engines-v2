import math
def fermat_factor(n):
    # Checks for even no.
    if (n & 1) == 0:
        return 2, n // 2
    # Jumps straight to sqrt boundary
    x = math.isqrt(n) + 1

    while True:
        y_square = x**2 - n

        if y_square < 0:
            x = x + 1
            continue
        y = math.isqrt(y_square)

        if y**2 == y_square:
            return int(x - y), int(x + y)
        x = x + 1
if __name__ == "__main__":
    target_payload = 1000000000000000003
    factor1, factor2 = fermat_factor(target_payload)

    print(f"Extraction Successful!")
    print(f"Factor 1: {factor1}")
    print(f"Factor 2: {factor2}")
    print(f"Verification Check: {factor1} * {factor2} = {factor1 * factor2}")