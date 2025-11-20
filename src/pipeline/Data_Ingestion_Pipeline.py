from src.entity.config_entity import DataIngestionConfig
from src.components.Data_Ingestion import DataIngestion
from src.configs.configuration import ConfigurationManager
from typing import IO
from src import logger


class DataIngestionPipeline():
    def __init__(self):
        self.config = ConfigurationManager()
        self.data_ingestion_config = self.config.get_data_ingestion_config()

    def initiate_data_ingestion(self, pdf : IO[bytes] ):
        logger.info("Starting data ingestion process")
        data_ingestion = DataIngestion(config = self.data_ingestion_config)
        data_ingestion.extract_text_from_pdf(pdf=pdf)
        data_ingestion.chunk_text()
        logger.info("Data ingestion process completed")

        











