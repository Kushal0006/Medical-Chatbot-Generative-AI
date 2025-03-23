import os 
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')


list_of_files = [
    "src/_init_.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "test.py",
    "research/trials.ipynb"
]


for filepath in list_of_files:
    filepath = Path(filepath)  # Convert to Path object for compatibility
    filedir, filename = os.path.split(filepath)  # Get directory and filename

    # Create directory if it does not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create an empty file if it does not exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")