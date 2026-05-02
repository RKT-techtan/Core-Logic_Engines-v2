my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
target = 10
left = 0
right = len(my_list) - 1

def binary_pointer(my_list, target):
    while left < right:
        current_sum = my_list[left] + my_list[right]

        if current_sum == target:
            return [my_list[left], my_list[high]]
        elif current_sum < target:
            left = left + 1
        else:
            high = high - 1
            
    return None