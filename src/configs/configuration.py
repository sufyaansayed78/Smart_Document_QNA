from src.utils.common import read_yaml
from src.entity.config_entity import DataIngestionConfig
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
