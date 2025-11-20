from dataclasses import dataclass

@dataclass
class DataIngestionConfig: 
    text_path: str
    token_path : str
    embedded_vectors_path : str 

@dataclass
class DataTransformationConfig:
  root_dir : str
  chunks_path : str
  embedded_vectors_path : str
