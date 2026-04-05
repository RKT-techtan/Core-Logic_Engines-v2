level = 8
nodes = 2 ** level

print(f"At level {level}, we have {nodes} items.")
for i in range(1, 5):
    result = 2 ** i
    print(f"2 to the power of {i} is {result}")