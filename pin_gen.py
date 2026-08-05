codes = [22, 55, 98, 104]

def security_rotator(all_codes):
    for code in all_codes:
        rotated_val = code % 10
        if rotated_val > 5:
            print(f"Code {rotated_val}: High security")
        else:
            print(f"Code {rotated_val} standard")
            
security_rotator(codes)