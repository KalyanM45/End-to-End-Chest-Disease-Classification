from Respire.Config.configuration import ConfigurationManager
from Respire.Components.Model_Trainer import Training

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()         

if __name__ == "__main__":
    pipeline = ModelTrainingPipeline()
    pipeline.main()