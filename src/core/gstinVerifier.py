from src.validators.gstin_validator import is_valid_gstin

MOCK_GSTINS = {
    "07ABCDE1234F1Z5":{"business_name": "Delight Foods", "status": "Active"},
    "27AAEPM1234C1Z5":{"business_name": "Tech Solutions", "status": "Active"},
    "29AAEPM1234C1Z5":{"business_name": "Retail Mart", "status": "Inactive"},
    "19AAEPM1234C1Z5":{"business_name": "HealthCare Inc", "status": "Active"},
    "10AAEPM1234C1Z5":{"business_name": "EduWorld", "status": "Active"},
}

def verify_gstin(gstin):
    """Verifies the GSTIN and returns business details if valid."""
    is_valid, message = is_valid_gstin(gstin)
    if not is_valid:
        return False, {"error": message}
    
    result = MOCK_GSTINS.get(gstin)
    if result:
        return True, {"message": "GSTIN is valid", "details": result}
    else:
        return False, {"error": "GSTIN not found in records"}