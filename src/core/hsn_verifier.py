import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("file is running")
from src.validators.hsn_validator.hsn_validator import is_valid_hsn  

HSN_registry = {
    "1001": "Wheat and meslin",
    "1002": "Rye",
    "1003": "Barley",
    "1004": "Oats",
    "8517": "mobile phones"
    # Add more HSN codes and their descriptions as needed

}

def hsn_verifier(hsn_code):
    """validates the HSN code and returns its description if valid.
    CHECK IF IT EXISTS IN REGISTRY
    return structured response
    """
    result = {"hsn": hsn_code, "valid": False, "description": None, "message": ""}
    if not is_valid_hsn(hsn_code):
      
        return (False, "invalid HSN code format")

    result["valid"] = True
    if hsn_code in HSN_registry:
        result["found"] = True
        result["description"] = HSN_registry[hsn_code]
        return (True, "HSN code is valid and found in registry")
    else:
        result["found"] = False
      
        return (False, "HSN code not found in registry")




if __name__ == "__main__":
    test_hsns = ["1001", "1002", "9999", "abcd", "123"]
    for h in test_hsns:
        print(hsn_verifier(h))
