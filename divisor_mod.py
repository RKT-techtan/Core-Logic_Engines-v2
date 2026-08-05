# Checking if a divisor is a factor of a number:
def check_divisibility(divisor, number):
    if number % divisor == 0:
        return True
    else:
        return False
print(check_divisibility(5, 25))