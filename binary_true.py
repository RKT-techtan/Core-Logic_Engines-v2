my_list = [1, 2, 3, 4, 5]
target = 0
low = 0
high = len(my_list) - 1

def binary_search(my_list, target):
    while low <= high: #//
        mid = (low + high) // 2

    if my_list[mid] == target:
        return mid
    elif my_list[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
    return -1