bits = 4
combinations = 2

print(f"For {bits} bits, there are {combinations} possibilites.")

for i in range(1, 21):
    print(f"Bits: {i} | options: {2**i}")