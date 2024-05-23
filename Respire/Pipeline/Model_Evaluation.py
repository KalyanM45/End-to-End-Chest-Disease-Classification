from Respire.Config.configuration import ConfigurationManager
from Respire.Components.Model_Evaluation import Evaluation

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()            

if __name__ == "__main__":
    pipeline = EvaluationPipeline()
    pipeline.main()