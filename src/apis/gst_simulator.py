# src/apis/gst_simulator.py

import csv
import os
import random
import logging
from src.apis  import data_loader # Make sure the dataset is downloaded

# --- Run the dataset setup first! ---
data_loader.setup_dataset()

# --- Load the CSV Dataset into Memory ---
_MOCK_GST_DATABASE = []
DATA_FILE_PATH = os.path.join(os.getcwd(), 'src', 'apis', 'companies.csv')

try:
    with open(DATA_FILE_PATH, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('name') and row.get('type'):
                _MOCK_GST_DATABASE.append({
                    "legal_name": row['name'].strip(),
                    "industry": row['type'].strip(),
                })
    logging.info(f"Successfully loaded {len(_MOCK_GST_DATABASE)} companies from CSV.")
except Exception as e:
    logging.error(f"Error loading companies.csv: {e}")
    # Add a fallback so the app doesn't crash
    _MOCK_GST_DATABASE = [
        {"legal_name": "Fallback Cafe", "industry": "Restaurant"}
    ]

# --- The NEW Simulator Function ---

def simulate_gst_api_call(gstin: str) -> dict:
    """
    Simulates a call to a real GST API using our CSV dataset.
    This is now a "dumb" function. It only returns raw data.
    """
    logging.info(f"Simulating API lookup for GSTIN: {gstin}")
    
    if not _MOCK_GST_DATABASE:
        return { "status": "Error", "message": "Simulation database is empty." }

    # Pick a random company profile
    company_profile = random.choice(_MOCK_GST_DATABASE)

    # Combine data and return
    response = {
        "gstin": gstin,
        "status": "Active",  # We'll just assume "Active"
        "legal_name": company_profile["legal_name"],
        "business_type": company_profile["industry"], # Return the raw industry
    }
    return response