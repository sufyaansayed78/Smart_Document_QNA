import pydoc_data
from PyPDF2 import PdfReader
from src.entity.config_entity import DataIngestionConfig
from src.utils.common import read_yaml , create_directories,save_text
import os
from typing import IO
import pandas as pd 
from src import logger

class DataIngestion:
    def __init(self,config : DataIngestionConfig):
        self.config = config

    
def extract_text_from_pdf( self,pdf : IO[bytes]) -> str :
        logger.info("Extracting text from PDF")
        pdf_reader = PdfReader(pdf)
        text = ""
        pdf.seek(0)

        reader = PdfReader(pdf)
        text = ""
        
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content
        create_directories([os.path.dirname(self.config.text_path)])
        save_text(self.config.text_path, text)
        logger.info(f"Text extraction completed at path {self.config.text_path}")

def chunk_text(self, chunk_size: int = 300, overlap: int = 50) -> list:
        from nltk.tokenize import word_tokenize
        logger.info(f"Chunking text into smaller segments from {self.config.text_path}")
        with open(self.config.text_path, 'r') as file:
            text = file.read()
        words = word_tokenize(text)
        chunks = []
        start = 0
        text_length = len(words)

        while start < text_length:
            end = min(start + chunk_size, text_length)
            chunk = ' '.join(words[start:end])
            chunks.append(chunk)
            start += chunk_size - overlap
        df = pd.DataFrame(chunks, columns=['chunks'])
        create_directories([os.path.dirname(self.config.token_path)])

        df.to_csv(self.config.token_path, index=False)
        logger.info(f"Text chunking completed and saved at {self.config.token_path}")

        


    

  