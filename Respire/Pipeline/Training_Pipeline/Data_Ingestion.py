from Respire.Config.configuration import ConfigurationManager
from Respire.Components.Data_Ingestion import DataIngestion

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()      

if __name__ == "__main__":
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()