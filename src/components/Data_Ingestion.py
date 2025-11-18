import pydoc_data
from PyPDF2 import PdfReader
import nltk 
from src.entity.config_entity import DataIngestionConfig
from src.utils.common import read_yaml , create_directories,save_text
import os
from typing import IO
import Pandas as pd 

class DataIngestion:
    def __init(self,config : DataIngestionConfig):
        self.config = config

    
def extract_text_from_pdf( self,pdf : IO[bytes]) -> str :
        pdf_reader = PdfReader(pdf)
        text = ""
        pdf.seek(0)

        reader = PdfReader(pdf)
        text = ""

        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content

        save_text(self.config.text_path, text)

def chunk_text(self, text: str, chunk_size: int = 500, overlap: int = 50) -> list:
        from nltk.tokenize import word_tokenize

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
        df.to_csv(self.config.token_path, index=False)

        


    

  