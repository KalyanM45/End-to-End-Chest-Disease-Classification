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


    def get_training_config(self) -> TrainingConfig:
        training = self.config.Model_Training
        prepare_base_model = self.config.Base_Model
        params = self.params
        training_data = os.path.join(self.config.Data_Ingestion.Unzip_Dir, "Chest-CT-Scan-data")
        create_directories([
            Path(training.Root_Dir)
        ])

        training_config = TrainingConfig(
            Root_Dir = Path(training.Root_Dir),
            Trained_Model_Path = Path(training.Trained_Model_Path),
            Updated_Model_Path = Path(prepare_base_model.Updated_Model_Path),
            Training_Data = Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config
    
    def get_evaluation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            Path_of_Model = Path(self.config.Model_Training.Trained_Model_Path),
            Training_Data = Path(self.config.Data_Ingestion.Unzip_Dir),
            mlflow_uri="https://dagshub.com/HemaKalyan45/End-to-End-Chest-Disease-Classification.mlflow",
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
        return eval_config