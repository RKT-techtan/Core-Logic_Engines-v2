my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = 10
left = 0
high = len(my_list) - 1

def two_sum_sorted(my_list, target):
    while left < high:
        current_sum = my_list[left] + my_list[high]
        if current_sum == target:
            return [my_list[left], my_list[high]]
        elif current_sum < target:
            left = left + 1
        else:
            high = high - 1
            return None