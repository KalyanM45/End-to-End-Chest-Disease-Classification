import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    f"src/__init__.py",
    f"src/Components/__init__.py",
    f"src/Utils/__init__.py",
    f"src/Config/__init__.py",
    f"src/Config/configuration.py",
    f"src/Pipeline/__init__.py",
    f"src/Entity/__init__.py",
    f"src/Constants/__init__.py",
    "Config/config.yaml",
    ".gitignore",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "Notebook_Experiments/Model_Training.ipynb",
    "templates/index.html",
    "app.py"
]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")