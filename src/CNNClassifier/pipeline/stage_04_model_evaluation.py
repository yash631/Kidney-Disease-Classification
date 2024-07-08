try:
  from src.CNNClassifier.config.configuration import ConfigurationManager
except ImportError:
  from CNNClassifier.config.configuration import ConfigurationManager

try:
  from src.CNNClassifier.components.model_evaluation import Evaluation
except ImportError:
  from CNNClassifier.components.model_evaluation import Evaluation

try:
  from src.CNNClassifier import logger
except ImportError:
  from CNNClassifier import logger




STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        # evaluation.log_into_mlflow()




if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
            