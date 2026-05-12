packet_ids = [101, 102, 103, 104, 105, 106, 107, 108]

def paginate(ids):
    for i, p_id in enumerate(ids):
        print(f"Loading packet {p_id}...")
        
        if (i + 1) % 5 == 0:
            print("--- Click for next page ---")

paginate(packet_ids)