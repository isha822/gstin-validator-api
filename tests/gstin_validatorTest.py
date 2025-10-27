import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.validators.gstin_validator import is_valid_gstin

test_cases = [
    ("27AAEPM1234C1Z5", True, "Valid GSTIN"),
    ("07AAEPM1234C1Z5", True, "Valid GSTIN"),
    ("99AAEPM1234C1Z5", False, "Invalid state code"),
    ("27AAEPM1234C1Z", False, "GSTIN must be 15 characters long"),
    ("27AAEPM1234C1Z55", False, "GSTIN must be 15 characters long"),
    ("27AAEPM1234C1Z@", False, "GSTIN format is invalid"),
    ("27AAEPM1234C1Z!", False, "GSTIN format is invalid"),
    ("27AAEPM1234C1Z$", False, "GSTIN format is invalid"),
    ("27AAEPM1234C1Z*", False, "GSTIN format is invalid"),
    ("27AAEPM1234C1Z ", False, "GSTIN format is invalid"),
    ("27AAEPM1234C1Z", False, "GSTIN must be    15 characters long"),
]

for gst in test_cases:
    valid, message = is_valid_gstin(gst[0])
    print(gst, "->", valid, message)