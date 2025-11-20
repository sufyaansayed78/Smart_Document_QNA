from src.entity.config_entity import DataTransformationConfig
from src.utils.common import create_directories 
from src.components.Data_Transformation import DataTransformation
from src import logger



class DataTransformationPipeline:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def initiate_data_transformation(self):
        data_transformation = DataTransformation(config=self.config)
        logger.info("Starting data transformation process")
        data_transformation.embedding()
        logger.info("Embedding process completed")
        data_transformation.store_to_vector_db()
        logger.info("Storing to vector database completed")
        embedded_query = data_transformation.question_to_query()
        logger.info("Query embedding completed")
        return embedded_query
    

















