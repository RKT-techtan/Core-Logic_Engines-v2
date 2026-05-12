codes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def security_audit(all_codes):
    for n in all_codes:
        if n % 2 != 0 and n % 3 != 0:
            print(f"Clean code {n}: not a multiple of 2 and 3")
        else:
            pass
security_audit(codes)