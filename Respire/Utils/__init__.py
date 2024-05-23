import os
import yaml
import json
import joblib
import base64
from typing import Any
from pathlib import Path
from box import ConfigBox
from Respire.Logger import logging
from ensure import ensure_annotations
from Respire.Exception import CustomException



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"Yaml file: {path_to_yaml} loaded")
            return ConfigBox(content)

    except Exception as e:
        raise CustomException(e)
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logging.info(f"Directory created at: {path}")
    
    except Exception as e:
        raise CustomException(e)


@ensure_annotations
def save_json(path: Path, data: dict):
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

        logging.info(f"json file saved at: {path}")
    
    except Exception as e:
        raise CustomException(e)


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    try:
        with open(path) as f:
            content = json.load(f)

        logging.info(f"json file loaded succesfully from: {path}")
        return ConfigBox(content)
    
    except Exception as e:
        raise CustomException(e)


@ensure_annotations
def save_bin(data: Any, path: Path):
    try:
        joblib.dump(value=data, filename=path)
        logging.info(f"binary file saved at: {path}")
    
    except Exception as e:
        raise CustomException(e)


@ensure_annotations
def load_bin(path: Path) -> Any:
    try:
        data = joblib.load(path)
        logging.info(f"binary file loaded from: {path}")
        return data
    except Exception as e:
        raise CustomException(e)
    

@ensure_annotations
def get_size(path: Path) -> str:
    try:

        size_in_kb = round(os.path.getsize(path)/1024)
        return f"~ {size_in_kb} KB"
    
    except Exception as e:
        raise CustomException(e)


def decodeImage(imgstring, fileName):
    try:
        imgdata = base64.b64decode(imgstring)
        with open(fileName, 'wb') as f:
            f.write(imgdata)
            f.close()

    except Exception as e:
        raise CustomException(e)


def encodeImageIntoBase64(croppedImagePath):
    try:
        with open(croppedImagePath, "rb") as f:
            return base64.b64encode(f.read())
    except Exception as e:
        raise CustomException(e)