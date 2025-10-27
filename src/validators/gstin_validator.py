# gstin_validator.py

import re

GSTIN_CODEPOINTS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def calculate_checksum(gstin_without_checksum):
    factor = 2
    total = 0

    for char in reversed(gstin_without_checksum):
        codepoint_value = GSTIN_CODEPOINTS.index(char)
        addend = factor * codepoint_value
        addend = (addend // 36) + (addend % 36)
        total += addend
        factor = 1 if factor == 2 else 2

    checksum_value = (36 - (total % 36)) % 36
    return GSTIN_CODEPOINTS[checksum_value]

def is_valid_gstin(gstin):
    gstin = gstin.upper()
    if not re.match(r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][1-9A-Z]Z[0-9A-Z]$', gstin):
        return False, "Invalid GSTIN structure"

    expected_checksum = calculate_checksum(gstin[:-1])
    if gstin[-1] != expected_checksum:
        return False, f"Invalid checksum. Expected {expected_checksum}, got {gstin[-1]}"
    
    return True, "Valid GSTIN"