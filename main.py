import sys
from wine_quality_mlops.utils.logger import logger
from wine_quality_mlops.utils.exceptions import (CustomException)
from wine_quality_mlops.pipeline.data_ingestion_pipeline import DataIngestionPipeline
# from src.wine_quality_mlops.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
# from src.wine_quality_mlops.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
# from src.wine_quality_mlops.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
# from src.wine_quality_mlops.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline

STAGE_NAME = "DATA INGESTION STAGE"

try:

    logger.info(f"Starting {STAGE_NAME}")

    data_ingestion = DataIngestionPipeline()

    data_ingestion.initiate_data_ingestion()

    logger.info(f"Completed {STAGE_NAME}")

except Exception as e:

    logger.exception(
        f"Error occurred in {STAGE_NAME}"
    )

    raise CustomException(e, sys)