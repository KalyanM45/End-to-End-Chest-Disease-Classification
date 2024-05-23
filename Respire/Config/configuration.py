import os
from Respire.Utils import *
from Respire.Constants import *
from Respire.Entity import DataIngestionConfig, PrepareBaseModelConfig, TrainingConfig, EvaluationConfig


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
    

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.Base_Model
        
        create_directories([config.Root_Dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            Root_Dir = Path(config.Root_Dir),
            Base_Model_Path = Path(config.Base_Model_Path),
            Updated_Model_Path = Path(config.Updated_Model_Path),
            params_image_size = self.params.IMAGE_SIZE,
            params_learning_rate = self.params.LEARNING_RATE,
            params_include_top = self.params.INCLUDE_TOP,
            params_weights = self.params.WEIGHTS,
            params_classes = self.params.CLASSES
        )

        return prepare_base_model_config