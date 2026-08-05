current_time = 22
hours_passed = 5

new_time = (current_time + hours_passed) % 24
print(f"The clock now shows: {new_time}:00")