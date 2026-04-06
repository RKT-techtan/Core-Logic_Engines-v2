import time

SECRET_KEY = 1000000000

def crack_key(max_bits):
    print(f"Starting brute force for {max_bits} bits...")
    start_time = time.time()
    
    combinations = 2 ** max_bits
    
    for guess in range(combinations):
        if guess == SECRET_KEY:
            end_time = time.time()
            print(f"MATCH FOUND: {guess}")
            print(f"Time taken: {end_time - start_time:.6f} seconds")
            return
            
    print("No match found.")

crack_key(30)