from wine_quality_mlops.config.configuration import (
    ConfigurationManager
)

from wine_quality_mlops.components.model_evaluation import (
    ModelEvaluation
)

from wine_quality_mlops.utils.logger import logger


STAGE_NAME = "MODEL EVALUATION STAGE"

class ModelEvaluationPipeline:
    
    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")

        obj = ModelEvaluationPipeline()
        obj.initiate_model_trainer()
        logger.info(f"Completed {STAGE_NAME}")

    except Exception as e:
        logger.exception(f"Error occurred in {STAGE_NAME}")
        raise e