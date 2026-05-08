prices = [10, 20, 30, 40, 50, 60, 70]
target = 50
low = 0
high = len(prices) - 1
mid = (low + high) // 2

def find_price(prices, target):
    
    while low <= high:
        mid = (low + high) // 2
        
        if prices[mid] == target:
            return mid
        elif prices[mid] < target:
            mid = high =+ 1
        else:
            mid = high =- 1
            
    return -1
print(f"{mid}")