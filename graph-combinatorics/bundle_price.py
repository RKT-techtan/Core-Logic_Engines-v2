prices = [10, 20, 30, 40, 50, 60, 70]
target = 90

def bundle_price(prices, target):
    left = 0
    right = len(prices) - 1

    while left < right:
        current_price = prices[left] + prices[right]

        if current_price == target:
            return [prices[left], prices[right]]
        elif current_price < target:
            left = left + 1
        else:
            right = right - 1