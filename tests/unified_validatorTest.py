import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.validators.unified_validator import validate_input

def test_unified_validator():
    test_cases = [
        # Valid GSTIN and HSN
        ("27AAEPM1234C1Z5", "1001", True, True),
        # Invalid GSTIN structure
        ("27AAEPM1234C1Z", "1001", False, True),
        # Invalid GSTIN checksum
        ("27AAEPM1234C1Z6", "1001", False, True),
        # Invalid HSN format
        ("27AAEPM1234C1Z5", "12A4", True, False),
        # HSN not in registry
        ("27AAEPM1234C1Z5", "9999", True, False),
        # Both GSTIN and HSN invalid
        ("27AAEPM1234C1Z", "12A4", False, False),
    ]

    for code, code_type, expected_valid_gstin, expected_valid_hsn in test_cases:
        result = validate_input(code)
        print(result)


if __name__ == "__main__":
    test_unified_validator()