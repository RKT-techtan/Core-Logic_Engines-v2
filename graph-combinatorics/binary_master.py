import time

data = list(range(1000000))

def binary_search_range(target):
    low = 0
    high = len(data) - 1
    steps = 0

    while low <= high:
        steps += 1