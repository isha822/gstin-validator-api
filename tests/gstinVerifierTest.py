from src.core.gstinVerifier import verify_gstin
test_cases = [
    ("27AAEPM1234C1Z5", True),  
    ("07ABCDE1234F1Z5", True),  
    ("29AAEPM1234C1Z5", True),
    ("19AAEPM1234C1Z5", True),
    ("10AAEPM1234C1Z5", True),
    ("99AAEPM1234C1Z5", False),
    ("27AAEPM1234C1Z", False),
    ("27AAEPM1234C1Z55", False),
    ("27AAEPM1234C1Z@", False),
    ("27AAEPM1234C1Z!", False),
    ("27AAEPM1234C1Z$", False),
    ("27AAEPM1234C1Z*", False),
    ("27AAEPM1234C1Z ", False),
    ("27AAEPM1234C1Z", False),
]

for gst in test_cases:
    result = verify_gstin(gst[0])
    print(gst, "->", result)
    