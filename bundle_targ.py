prices = [10, 20, 30, 40, 50, 60, 70]
target = 50

def find_prices(prices, target):
    low = 0
    high = len(prices) - 1
    while low <= high:
        mid = (low + high) // 2

        if prices[mid] == target:
            return mid
        elif prices[mid] < target:
            high = mid - 1
        else:
            low = mid + 1
            return -1