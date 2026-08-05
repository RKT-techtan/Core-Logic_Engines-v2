# Decimal interger
num = 218

# Decimal -> binary or hexadecimal strings
bin_str = bin(num) # Returns '0b11011010'
hex_str = hex(num) # Returns 'Oxda'

# Custom string formatting (Clean padding without prefixes)
formatted_bin = f"{num:08b}" # '11011010' (8-bit padded)
formatted_hex = f"{num:02X}" # 'DA' (Uppercase, 2-character padded)

# String -> decimal interger (parsing with base)
dec_from_bin = int("11011010", 2) # Returns 218
dec_from_hex = int("DA", 16)      # Returns 218