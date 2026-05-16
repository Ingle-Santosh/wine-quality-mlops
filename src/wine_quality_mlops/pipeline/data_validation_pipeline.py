from wine_quality_mlops.config.configuration import (
    ConfigurationManager
)

from wine_quality_mlops.components.data_validation import (
    DataValidation
)

from wine_quality_mlops.utils.logger import logger


STAGE_NAME = "DATA VALIDATION STAGE"

class DataValidationPipeline:
    
    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")

        obj = DataValidationPipeline()
        obj.initiate_data_validation()
        logger.info(f"Completed {STAGE_NAME}")

    except Exception as e:
        logger.exception(f"Error occurred in {STAGE_NAME}")
        raise e