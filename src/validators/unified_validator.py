
# 1. Use ABSOLUTE paths from 'src'
from src.core.hsn_verifier import hsn_verifier
from src.core.gstinVerifier import verify_gstin

def validate_input(code: str):
    code = code.strip().upper()

    if len(code) == 15 and code.isalnum():
        # 2. Use your ORIGINAL function name: verify_gstin
        # 3. Correctly unpack the tuple
        is_valid, message = verify_gstin(code) 
        return {"type": "GSTIN", "input": code, "valid": is_valid, "message": message}
    
    elif code.isdigit() and len(code) in [4, 6, 8]:
        # 2. Use your ORIGINAL function name: hsn_verifier
        # 3. Correctly unpack the tuple
        is_valid, message = hsn_verifier(code)
        return {"type": "HSN", "input": code, "valid": is_valid, "message": message}
    
    else:
        return {"type": "Unknown", "input": code, "valid": False, "message": "Invalid input format"}


