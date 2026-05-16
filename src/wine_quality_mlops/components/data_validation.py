import sys
import pandas as pd
from wine_quality_mlops.utils.logger import logger

from wine_quality_mlops.utils.exceptions import (
    CustomException
)

from wine_quality_mlops.entity.config_entity import (
    DataValidationConfig
)


class DataValidation:

    def __init__(self,config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:

            validation_status = True
            logger.info("Starting data validation")
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = list(self.config.all_schema.keys())

            missing_cols = []

            for col in all_schema:
                if col not in all_cols:
                    validation_status = False
                    missing_cols.append(col)

            if missing_cols:
                logger.warning(f"Missing columns: {missing_cols}")

            else:
                logger.info("All columns validated successfully")

            with open(self.config.status_file,"w") as f:
                f.write(
                    f"Validation status: "
                    f"{validation_status}"
                )
            return validation_status

        except Exception as e:
            logger.exception("Error during data validation")
            raise CustomException(e, sys)