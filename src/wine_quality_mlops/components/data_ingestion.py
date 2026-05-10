import zipfile
import urllib.request as request

from pathlib import Path

from wine_quality_mlops.utils.logger import logger

from wine_quality_mlops.entity.config_entity import (
    DataIngestionConfig
)


class DataIngestion:

    def __init__(self, config: DataIngestionConfig):

        self.config = config

    def download_file(self):

        """
        Download dataset zip file.
        """

        try:

            if not self.config.local_data_file.exists():

                logger.info("Downloading dataset...")

                filename, headers = request.urlretrieve(
                    url=self.config.source_url,
                    filename=self.config.local_data_file
                )

                logger.info(
                    f"Downloaded file: {filename}\n"
                    f"Headers: {headers}"
                )

            else:

                logger.info(
                    f"File already exists at: "
                    f"{self.config.local_data_file}"
                )

        except Exception as e:

            logger.exception("Failed to download dataset")

            raise e

    def extract_zip_file(self):

        """
        Extract zip file into target directory.
        """

        try:

            unzip_path = self.config.unzip_dir

            unzip_path.mkdir(parents=True, exist_ok=True)

            logger.info("Extracting zip file...")

            with zipfile.ZipFile(
                self.config.local_data_file,
                "r"
            ) as zip_ref:

                zip_ref.extractall(unzip_path)

            logger.info(
                f"Files extracted to: {unzip_path}"
            )

        except Exception as e:

            logger.exception("Failed to extract zip file")

            raise e