daily_sales = [100, 200, 300, 400, 100, 500]
k = 3

def max_streaku(daily_sales, k):
    current_window_sum = sum(daily_sales[:k])
    max_sum = current_window_sum

    for i in range(k, len(daily_sales)):
        current_window_sum += daily_sales
        current_window_sum -= daily_sales[i - k]
        if current_window_sum > max_sum:
            max_sum = current_window_sum

            return max_sum