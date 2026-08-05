packet_ids = [102, 305, 408, 901, 202]

def audit_packets(ids):
    for p_id in ids:
        if p_id % 2 != 0:
            print(f"Hey, odd alert: {p_id}")
        else:
            print(f"Yes, even, relax: {p_id}")
            
audit_packets(packet_ids)