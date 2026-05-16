import os
import sys
from wine_quality_mlops.utils.logger import logger
from wine_quality_mlops.utils.exceptions import (
    CustomException
)
from sklearn.model_selection import train_test_split
import pandas as pd
from wine_quality_mlops.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config


    def train_test_splitting(self):

        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets
        train, test = train_test_split(
            data,
            test_size=0.25,
            random_state=42
        )

        train.to_csv(self.config.train_path, index=False)

        test.to_csv(self.config.test_path, index=False)

        logger.info("Split data into training and test sets")

        logger.info(f"Train shape: {train.shape}")
        logger.info(f"Test shape: {test.shape}")

        print(train.shape)
        print(test.shape)