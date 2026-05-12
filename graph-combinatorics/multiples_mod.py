data_points = [3, 6, 7, 9, 12, 14, 18]

def find_multiples(numbers):
    for n in numbers:
        if n % 2 == 0 & n % 3 == 0:
            print(f"{n} is a multiple of 3 and 2!")

find_multiples(data_points)