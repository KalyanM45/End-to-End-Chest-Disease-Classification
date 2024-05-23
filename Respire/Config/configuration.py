import os
from Respire.Utils import *
from Respire.Constants import *
from Respire.Entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.Artifacts_Root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.Data_Ingestion

        create_directories([config.Root_Dir])

        data_ingestion_config = DataIngestionConfig(
            Root_Dir=config.Root_Dir,
            Source_URL=config.Source_URL,
            Local_Data_File=config.Local_Data_File,
            Unzip_Dir=config.Unzip_Dir 
        )

        return data_ingestion_config