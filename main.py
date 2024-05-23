from Respire.Logger import logging
from Respire.Pipeline.Data_Ingestion import DataIngestionTrainingPipeline
#from Respire.Pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
#from Respire.Pipeline.stage_03_model_trainer import ModelTrainingPipeline
#from Respire.Pipeline.stage_04_model_evaluation import EvaluationPipeline



try:
    logging.info("<----------------- Data Ingestion Initiated ----------------->")

    obj = DataIngestionTrainingPipeline()
    obj.main()

    logging.info("<----------------- Data Ingestion completed ----------------->")

    '''
    logging.info("<----------------- Base Model Preparation Initiated ----------------->")

    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()

    logging.info("<----------------- Base Model Preparation completed ----------------->")


    logging.info("<----------------- Model Training Initiated ----------------->")

    model_trainer = ModelTrainingPipeline()
    model_trainer.main()

    logging.info("<----------------- Model Training completed ----------------->")

    logging.info("<----------------- Model Evaluation Initiated ----------------->")

    model_evalution = EvaluationPipeline()
    model_evalution.main()

    logging.info("<----------------- Model Evaluation completed ----------------->")

    '''
except Exception as e:
    
    logging.exception(e)
    raise e