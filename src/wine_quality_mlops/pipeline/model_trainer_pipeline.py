from wine_quality_mlops.config.configuration import (
    ConfigurationManager
)

from wine_quality_mlops.components.model_trainer import (
    ModelTrainer
)

from wine_quality_mlops.utils.logger import logger


STAGE_NAME = "MODEL TRAINER STAGE"

class ModelTrainerPipeline:
    
    def initiate_model_trainer(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()


if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")

        obj = ModelTrainerPipeline()
        obj.initiate_model_trainer()
        logger.info(f"Completed {STAGE_NAME}")

    except Exception as e:
        logger.exception(f"Error occurred in {STAGE_NAME}")
        raise e