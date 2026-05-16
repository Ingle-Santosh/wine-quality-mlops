from pathlib import Path

from wine_quality_mlops.constants import (
    CONFIG_FILE_PATH,
    PARAMS_FILE_PATH,
    SCHEMA_FILE_PATH,
)

from wine_quality_mlops.utils.io_utils import (
    read_yaml,
    create_directories,
)

from wine_quality_mlops.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig,
)


class ConfigurationManager:

    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH,
        schema_filepath: Path = SCHEMA_FILE_PATH,
    ):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        self.artifacts_root = Path(self.config["artifacts_root"])

        create_directories([self.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config["data_ingestion"]

        root_dir = self.artifacts_root / config["root_dir"]

        create_directories([root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=root_dir,
            source_url=config["source_url"],
            local_data_file=root_dir / config["local_data_file"],
            unzip_dir=root_dir / config["unzip_dir"],
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:

        config = self.config["data_validation"]

        root_dir = self.artifacts_root / config["root_dir"]

        create_directories([root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=root_dir,
            status_file=root_dir / config["status_file"],
            unzip_data_dir=Path(config["data_file"]),
            all_schema=self.schema["COLUMNS"],
        )

        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:

        config = self.config["data_transformation"]

        root_dir = self.artifacts_root / config["root_dir"]

        create_directories([root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=root_dir,
            data_path=Path(config["data_path"]),
            train_path=root_dir / config["train_path"],
            test_path=root_dir / config["test_path"],
        )

        return data_transformation_config 

    def get_model_trainer_config(self) -> ModelTrainerConfig:

        config = self.config["model_trainer"]

        params = self.params["ElasticNet"]

        schema = self.schema["TARGET_COLUMN"]

        root_dir = self.artifacts_root / config["root_dir"]

        create_directories([root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=root_dir,
            train_data_path=Path(config["train_data_path"]),
            test_data_path=Path(config["test_data_path"]),
            model_name=config["model_name"],
            alpha=params["alpha"],
            l1_ratio=params["l1_ratio"],
            target_column=schema["name"],
        )

        return model_trainer_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:

        config = self.config["model_evaluation"]

        params = self.params["ElasticNet"]

        schema = self.schema["TARGET_COLUMN"]

        root_dir = self.artifacts_root / config["root_dir"]

        create_directories([root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=root_dir,
            test_data_path=Path(config["test_data_path"]),
            model_path=Path(config["model_path"]),
            all_params=params,
            metric_file_name=root_dir / config["metric_file_name"],
            target_column=schema["name"],
            mlflow_uri="https://dagshub.com/krishnaik06/datascienceproject.mlflow",
        )

        return model_evaluation_config