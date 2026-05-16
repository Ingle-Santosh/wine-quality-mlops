from wine_quality_mlops.config.configuration import (
    ConfigurationManager
)

from wine_quality_mlops.components.data_ingestion import (
    DataIngestion
)

from wine_quality_mlops.utils.logger import logger


STAGE_NAME = "DATA INGESTION STAGE"


class DataIngestionPipeline:

    def initiate_data_ingestion(self):

        config = ConfigurationManager()

        data_ingestion_config = (
            config.get_data_ingestion_config()
        )

        data_ingestion = DataIngestion(
            config=data_ingestion_config
        )

        data_ingestion.download_file()

        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")

        obj = DataIngestionPipeline()
        obj.initiate_data_ingestion()
        logger.info(f"Completed {STAGE_NAME}")

    except Exception as e:
        logger.exception(f"Error occurred in {STAGE_NAME}")
        raise e