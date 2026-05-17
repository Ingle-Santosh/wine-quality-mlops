import sys
from wine_quality_mlops.utils.logger import logger
from wine_quality_mlops.utils.exceptions import (CustomException)
from wine_quality_mlops.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from wine_quality_mlops.pipeline.data_validation_pipeline import DataValidationPipeline
from wine_quality_mlops.pipeline.data_transformation_pipeline import DataTransformationPipeline
from wine_quality_mlops.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from wine_quality_mlops.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline

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


STAGE_NAME = "DATA VALIDATION STAGE"

try:

    logger.info(f"Starting {STAGE_NAME}")

    data_ingestion = DataValidationPipeline()

    data_ingestion.initiate_data_validation()

    logger.info(f"Completed {STAGE_NAME}")

except Exception as e:

    logger.exception(
        f"Error occurred in {STAGE_NAME}"
    )

    raise CustomException(e, sys)


STAGE_NAME = "DATA TRANSFORMATION STAGE"

try:

    logger.info(f"Starting {STAGE_NAME}")

    data_ingestion = DataTransformationPipeline()

    data_ingestion.initiate_data_transformation()

    logger.info(f"Completed {STAGE_NAME}")

except Exception as e:

    logger.exception(
        f"Error occurred in {STAGE_NAME}"
    )

    raise CustomException(e, sys)

STAGE_NAME = "MODEL TRAINER STAGE"

try:

    logger.info(f"Starting {STAGE_NAME}")

    data_ingestion = ModelTrainerPipeline()

    data_ingestion.initiate_model_trainer()

    logger.info(f"Completed {STAGE_NAME}")

except Exception as e:

    logger.exception(
        f"Error occurred in {STAGE_NAME}"
    )

    raise CustomException(e, sys)


STAGE_NAME = "MODEL EVALUATION STAGE"

try:

    logger.info(f"Starting {STAGE_NAME}")

    data_ingestion = ModelEvaluationPipeline()

    data_ingestion.initiate_model_evaluation()

    logger.info(f"Completed {STAGE_NAME}")

except Exception as e:

    logger.exception(
        f"Error occurred in {STAGE_NAME}"
    )

    raise CustomException(e, sys)