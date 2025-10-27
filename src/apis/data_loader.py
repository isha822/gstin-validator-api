# src/apis/data_loader.py

import kaggle
import os
import zipfile
import logging

# The dataset we want from Kaggle
DATASET_ID = 'akakshay/list-of-companies'

# The path where we will store the final, clean CSV
# This is os.path.dirname(_file_) which means "the same folder as this file"
DATA_DIR = os.path.join(os.getcwd(), 'src', 'apis')
FINAL_CSV_PATH = os.path.join(DATA_DIR, 'companies.csv')
# The original file name inside the zip
ORIGINAL_CSV_NAME = 'Companies_list.csv' 

def setup_dataset():
    """
    Ensures the 'companies.csv' dataset is downloaded and ready to be used.
    """
    # 1. Check if the file already exists. If yes, we don't need to do anything.
    if os.path.exists(FINAL_CSV_PATH):
        logging.info(f"Dataset '{FINAL_CSV_PATH}' already exists. Skipping download.")
        return

    # 2. If it doesn't exist, download it from Kaggle
    logging.warning(f"Dataset not found. Downloading from Kaggle: {DATASET_ID}")
    try:
        # Authenticate with kaggle.json
        kaggle.api.authenticate()
        
        # Download the dataset files into our DATA_DIR
        kaggle.api.dataset_download_files(DATASET_ID, path=DATA_DIR, unzip=False)
        
        # 3. Unzip the downloaded file
        zip_path = os.path.join(DATA_DIR, f'{DATASET_ID.split("/")[1]}.zip')
        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            logging.info(f"Unzipping '{zip_path}'...")
            zip_ref.extractall(DATA_DIR)
            
        # 4. Rename the extracted file to our standard 'companies.csv'
        original_file_path = os.path.join(DATA_DIR, ORIGINAL_CSV_NAME)
        os.rename(original_file_path, FINAL_CSV_PATH)
        
        # 5. Clean up the .zip file
        os.remove(zip_path)
        
        logging.info("Dataset setup complete.")
        
    except Exception as e:
        logging.error(f"Failed to download or process dataset: {e}")
        logging.error("Please ensure your kaggle.json is in ~/.kaggle/kaggle.json")
        # As a fallback, create an empty file so the app doesn't crash
        # or you could raise the exception
        if not os.path.exists(FINAL_CSV_PATH):
            open(FINAL_CSV_PATH, 'a').close() 
            logging.warning("Created empty 'companies.csv' as a fallback.")

# --- Run the setup when this module is imported ---
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Running dataset setup...")
    setup_dataset()
    logging.info("Setup finished.")