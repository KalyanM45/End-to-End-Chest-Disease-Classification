from Respire.Config.configuration import ConfigurationManager
from Respire.Components.Base_Model import PrepareBaseModel


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model() 

if __name__ == "__main__":
    pipeline = PrepareBaseModelTrainingPipeline()
    pipeline.main()