packets = [101, 102, 103, 104, 105, 106]

def health_audit(data):
    for i, p_id in enumerate(data):
        position = i + 1
        
        if position % 3 == 0:
            print(f"Position {position}: LATENCY CHECK REQUIRED")
            
        if p_id % 2 == 0:
            print(f"ID {p_id}: SECURITY AUDIT REQUIRED")

health_audit(packets)