from src.utils.common import read_yaml
from src.entity.config_entity import DataIngestionConfig, DataTransformationConfig, RetrieveVectorsConfig
from src.utils.common import create_directories

class ConfigurationManager:
    def __init__(self,CONFIG_FILE_PATH = "config\config.yaml") :
        config = read_yaml(CONFIG_FILE_PATH)
        create_directories([config.artifacts_root])
        pass

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = read_yaml("config\config.yaml")
        data_ingestion_config = config.Data_Ingestion

        create_directories(
            [data_ingestion_config.root_dir]
        )

        data_ingestion_config = DataIngestionConfig(
            text_path = data_ingestion_config.text_path,
            token_path = data_ingestion_config.token_path,
            embedded_vectors_path = data_ingestion_config.embedded_vectors_path
        )

        return data_ingestion_config
    def get_transformation_config(self):
        config = read_yaml("config\config.yaml")
        data_transformation_config = config.Data_Transformation

        create_directories([data_transformation_config.root_dir])
        data_transformation_config = DataTransformationConfig(
            root_dir = data_transformation_config.root_dir,
            chunks_path = data_transformation_config.chunks_path,
            embedded_vectors_path = data_transformation_config.embedded_vectors_path,
            embedded_query_path = data_transformation_config.embedded_query_path)
        return data_transformation_config
    def get_retrieve_vectors_config(self):
        config = read_yaml("config\config.yaml")
        retrieve_vectors_config = config.Retrieve_Vectors

        create_directories([retrieve_vectors_config.root_dir])
        retrieve_vectors_config = RetrieveVectorsConfig(
            root_dir = retrieve_vectors_config.root_dir,
            embedded_query_path = retrieve_vectors_config.embedded_query_path,
            similar_vectors_path = retrieve_vectors_config.similar_vectors_path)
        return retrieve_vectors_config

