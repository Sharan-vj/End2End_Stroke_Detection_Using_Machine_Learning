# Import Dependencies
from strokePredictor.constants import *
from strokePredictor.entity.config_entity import *
from strokePredictor.utils.common import create_directory, yaml_reader

# Config Manager
class ConfigManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH,
                 schema_filepath = SCHEMA_FILE_PATH):
        
        self.config = yaml_reader(filepath=config_filepath, log=True)
        self.params = yaml_reader(filepath=params_filepath, log=True)
        self.schema = yaml_reader(filepath=schema_filepath, log=True)
        create_directory(directory_path=[self.config.artifacts_root], log=True)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directory(directory_path=[config.root_dir], log=True)

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            dataset_url=config.dataset_url,
            dataset_raw=config.dataset_raw
        )
        return data_ingestion_config
