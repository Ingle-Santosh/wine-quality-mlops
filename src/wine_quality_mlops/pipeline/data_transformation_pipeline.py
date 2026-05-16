from wine_quality_mlops.config.configuration import ConfigurationManager
from wine_quality_mlops.components.data_transformation import DataTransformation
from wine_quality_mlops.utils.logger import logger
from pathlib import Path


STAGE_NAME = "DATA TRANSFORMATION STAGE"


class DataTransformationPipeline:

    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),"r") as f:
                status = f.read().split(" ")[-1]
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = (config.get_data_transformation_config())
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception(
                    "Your data schema is not valid"
                )

        except Exception as e:
            logger.exception(f"Error occurred in {STAGE_NAME}")
            raise e


if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")

        obj = DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f"Completed {STAGE_NAME}")

    except Exception as e:
        logger.exception(f"Error occurred in {STAGE_NAME}")
        raise e