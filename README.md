# GSTIN Validator API

A Python FastAPI API designed for validating Indian Goods and Services Tax Identification Numbers (GSTIN) and Harmonized System of Nomenclature (HSN) codes. It includes a GSTIN checksum algorithm and provides basic citizen guidance based on simulated business data.

## Features

* *GSTIN Validation:* Validates the format and checksum of 15-digit GSTIN codes according to official standards.
* *HSN Validation:* Validates the format (4, 6, or 8 digits) and checks against a sample registry.
* *Simulated Data Integration:* Looks up business details (name, type) from a simulated dataset (derived from a Kaggle CSV) for valid GSTINs.
* *Citizen Guidance:* Provides basic GST rate information and citizen advice based on the simulated business type.
* *API Documentation:* Automatically generates interactive API documentation (Swagger UI) via FastAPI.

## Setup & Installation

Follow these steps to set up and run the project locally.

1.  *Clone the Repository:*
    bash
    git clone [https://github.com/isha822/gstin-validator-api.git](https://github.com/isha822/gstin-validator-api.git)
    cd gstin-validator-api
    

2.  *Create and Activate a Virtual Environment:*
    (Recommended to isolate project dependencies)
    bash
    # Create the environment
    python3 -m venv venv

    # Activate on Linux/macOS
    source venv/bin/activate

    # Activate on Windows (Git Bash or WSL)
    # source venv/Scripts/activate

    # Activate on Windows (Command Prompt)
    # venv\Scripts\activate.bat
    

3.  *Install Dependencies:*
    This command installs all required Python packages listed in requirements.txt.
    bash
    pip install -r requirements.txt
    

4.  *Set Up Kaggle API Key:*
    The data loader requires Kaggle API credentials to download the initial dataset.
    * Download your kaggle.json API token from your Kaggle account settings.
    * Create a .kaggle directory in your home folder if it doesn't exist:
        bash
        mkdir -p ~/.kaggle
        
    * Move your downloaded token to the correct location and set permissions:
        bash
        # Adjust the source path if needed (e.g., if using WSL)
        mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json
        chmod 600 ~/.kaggle/kaggle.json
        

## Running the API

1.  *Run the Data Loader (One Time Only):*
    This script downloads the dataset from Kaggle and prepares the companies.csv file. You only need to run this the first time you set up the project.
    bash
    PYTHONPATH=. python3 -m src.apis.data_loader
    

2.  *Start the FastAPI Server:*
    This command runs the API using Uvicorn. The --reload flag automatically restarts the server when you save code changes.
    bash
    PYTHONPATH=. uvicorn src.validators.api.main:app --reload
    

## Usage

Once the server is running:

* Access the interactive API documentation (Swagger UI) in your browser at: *http://127.0.0.1:8000/docs*
* Send POST requests to the /verify endpoint with a JSON body like:
    json
    {
      "code_type": "GSTIN",
      "code": "29AAFCD5862R1Z5"
    }
    
    or
    json
    {
      "code_type": "HSN",
      "code": "0401"
    }
