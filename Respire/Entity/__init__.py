from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    Root_Dir: Path
    Source_URL: str
    Local_Data_File: Path
    Unzip_Dir: Path



@dataclass(frozen=True)
class PrepareBaseModelConfig:
    Root_Dir: Path
    Base_Model_Path: Path
    Updated_Model_Path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int



@dataclass(frozen=True)
class TrainingConfig:
    Root_Dir: Path
    Trained_Model_Path: Path
    Updated_Model_Path: Path
    Training_Data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list



@dataclass(frozen=True)
class EvaluationConfig:
    Path_of_Model: Path
    Training_Data: Path
    all_params: dict
    mlflow_uri: str
    params_image_size: list
    params_batch_size: int