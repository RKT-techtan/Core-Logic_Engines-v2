def find_gcd(a, b):
    start_point = min(a, b)
    for i in range(start_point, 0, -1):
        if a % i == 0 and b % i == 0:
            print(f"{i}")
print(find_gcd(12, 18))
