import pydoc_data
from PyPDF2 import PdfReader
import nltk 
from src.entity.config_entity import DataIngestionConfig
from src.utils.common import read_yaml , create_directories,save_text
import os
from typing import IO

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

def preprocess_text(self):
    with open(self.config.text_path, 'r') as file:
         text = file.read()
    stopwords = nltk.corpus.stopwords.words('english')
    text_as_list = text.splitlines()
    

    

  