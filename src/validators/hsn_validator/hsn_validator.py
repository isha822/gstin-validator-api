DELHI_HSN_CODES = {"1901", "1902", "2101", "2201", "2401", "2501", "2701", "3001", "3201", "3301", "3401", "3501", "3601", "3701", "3801", "3901", "4001", "4101", "4201", "4301", "4401", "4501", "4601", "4701", "4801", "4901", "5001", "5101", "5201", "5301", "5401", "5501", "5601", "5701", "5801", "5901", "6001", "6101", "6201", "6301"}

def is_valid_hsn(hsn):
    hsn = str(hsn)

    if len(hsn) not in {4, 6, 8}:
        return False, "HSN code must be 4, 6, or 8 digits long"
    if not hsn.isdigit():
        return False, "HSN code must be numeric"
    if hsn not in DELHI_HSN_CODES:
        return False, "HSN code not valid for Delhi"
    return True, "Valid HSN code"
