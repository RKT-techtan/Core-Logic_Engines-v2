# Manual conversions/algorithms for base 10, base 2, base 16
# Decimal, Binary, Hexadecimal

Hex_LOOKUP = "0123456789ABCDEF"

def decimal_to_binary(n: int) -> str:
    # 1. Converting a positive decimal interger to a binary string(base 2)
    if n == 0:
        return "0"

    bits = []
    while n > 0:
        remainder = n % 2
        bits.append(str(remainder)) # Collect LSB first
        n = n // 2
    return "".join(reversed(bits))

def decimal_to_hex(n: int) -> str:
    # 2. Converts a positive decimal interger to a hexadecimal string(base 16)
    if n == 0:
        return "0x0"

    hex_digits = []
    while n > 0:
        remainder = n % 16
        hex_digits.append(Hex_LOOKUP[remainder])
        n = n // 16
    return "0x" + "".join(reversed(hex_digits))

def binary_to_decimal(binary_str: str) -> int:
    # 3. Converts binary string to a decimal interger(base10)
    decimal_val = 0
    clean_str = binary_str.replace("0b", "")

    for char in clean_str:
        digit = int(char)
        decimal_val = (decimal_val * 2) + digit
    return decimal_val

def hex_to_decimal(hex_str: str) -> int:
    # 4. Converts hexadecimal string to decimal interger(base10)
    decimal_val = 0
    clean_str = hex_str.replace("0x", "").upper()

    for char in clean_str:
        digit = Hex_LOOKUP.index(char)
        decimal_val = (decimal_val * 16) + digit
    return decimal_val

if __name__ == "__main__":
    # Testing suite verification
    test_val = 218
    print(f"Decimal input: {test_val}")

    bin_res = decimal_to_binary(test_val)
    print(f"Binary output: 0b{bin_res}")

    hex_res = decimal_to_hex(test_val)
    print(f"Hex output: {hex_res}")

    print(f"Back to decimal from binary: {binary_to_decimal(bin_res)}")
    print(f"Back to decimal from Hex: {hex_to_decimal(hex_res)}")