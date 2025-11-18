from src.components.Data_Ingestion import DataIngestion
from src.configs.configuration import ConfigurationManager
from PyPDF2 import PdfReader
import io
from src.utils.common import save_text
from typing import IO


        
with open("sample.pdf","rb") as pdf:
      pdf_bytes = pdf.read()
pdf_stream = io.BytesIO(pdf_bytes)
extract_text_from_pdf( pdf_stream)
