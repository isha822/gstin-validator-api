import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src.validators.hsn_validator.hsn_validator import is_valid_hsn   

test_cases = [
    ("1901", True, "Valid HSN code"),
    ("2101", True, "Valid HSN code"),
    ("9999", False, "HSN code not valid for Delhi"),
    ("123", False, "HSN code must be 4, 6, or 8 digits long"),
    ("12345", False, "HSN code must be 4, 6, or 8 digits long"),
    ("1234567", False, "HSN code must be 4, 6, or 8 digits long"),
    ("123456789", False, "HSN code must be 4, 6, or 8 digits long"),
    ("12A4", False, "HSN code must be numeric"),
]

for hsn in test_cases:
    valid, message = is_valid_hsn(hsn[0])
    print(hsn, "=>", valid, message)