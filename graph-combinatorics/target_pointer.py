n = [2, 4, 7, 11, 15]
target = 13

low = 0

def range_test(numbers, goal):
    high = numbers 
    while low < high:
        current_sum = numbers[low] + numbers[high]

    if current_sum == goal:
        high = high - 1
    elif n < target:
        low = low + 1
    else:
        n == target
        print(f"{n}")