target = 200

def finding_factors(number):
    print(f"Finding factors for {number}:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(f"{i} is a factor!")
finding_factors(target)