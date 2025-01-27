import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "MedicalBot"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/helper.py",
    f"src/{project_name}/prompt.py",
    f".env",
    "app.py",
    "setup.py",
    "research/trials.ipynb"

]


for filepath in list_of_files:
    filepath = Path(filepath)  #to autodetect and implement detect the file path from any OS-MAC,Win or Linux
    filedir, filename = os.path.split(filepath)     #split the folders and file according to my specifications given in the list_of_files

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")