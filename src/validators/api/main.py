# src/api/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from src.validators.unified_validator import validate_input

# Import the ONE master function from our "brain"
from src.core.gst_logic import get_full_gst_details
class CodeInput(BaseModel): # Define input model
    code_type: str
    code: str

# Set up logging
logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Civic Platform API",
    description="API for validating Indian civic codes and providing citizen advice.",
    version="1.0.0"
)

@app.post("/verify")
async def verify_code(input: CodeInput):

    # 1. Call the unified validator FIRST
    validation_result = validate_input(input.code)

    # 2. If the code is invalid, just return the error
    if not validation_result["valid"]:
        return validation_result

    # 3. If the code is valid, check its type
    if validation_result["type"] == "GSTIN":
        # Only GSTINs get the "full details" logic
        gst_details = get_full_gst_details(validation_result) # Pass the whole result
        return gst_details

    elif validation_result["type"] == "HSN":
        # HSNs get a simple "valid" response
        return validation_result # This will return {"type": "HSN", ... "valid": True}

    else:
        # This should not happen, but just in case
        raise HTTPException(status_code=400, detail="Unknown valid code type")
@app.get("/")
def read_root():
    return {"message": "Welcome to the Civic Platform API"}