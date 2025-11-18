import yaml 
from box   import Box
import os 
from src import logger

def read_yaml(path : str)->Box:
    with open(path, 'r') as yaml_file:
        logger.info(f"Reading yaml file from path : {path}")
        content = yaml.safe_load(yaml_file)
        return Box(content)
    
def create_directories(path_list):
    for path in path_list:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Created directory at : {path}")

def save_text(path: str, text: str) -> None:
    with open(path, 'w') as text_file:
        text_file.write(text)
        logger.info(f"Saved text data at : {path}")





