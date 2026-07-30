def decimal_to_binary_buggy(n: int) -> str:
    if n == 0:
        return "0"

    binary_str = ""
    while n > 0:
        remainder = n % 2
        # Bug!!!
        # Was: binary_str = binary_str + str(remainder)
        # Changed to:
        binary_str = str(remainder) + binary_str
        n = n // 2

    # Or you could use:
    # return binary_str[::-1]
    return binary_str
print(decimal_to_binary_buggy(13))